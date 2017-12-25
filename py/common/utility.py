#!/usr/bin/env python3

"""utility.py

Various common utility functions, classes and decorators.
"""

__author__ = 'Curtis Belmonte'

import heapq
import itertools
import random
from collections import deque
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
)

from common.types import Comparable, IntMatrix


class Graph(object):
    """Class representing a directed graph with weighted edges."""

    def __init__(self) -> None:
        self._adj = {} # type: Dict[object, Dict[object, float]]
        self._node_count = 0
        self._edge_count = 0

    def num_nodes(self) -> int:
        """Returns the number of vertices in the graph."""
        return self._node_count

    def num_edges(self) -> int:
        """Returns the number of edges in the graph."""
        return self._edge_count

    def nodes(self) -> Iterable[Any]:
        """Returns an iterable of the unique vertices in the graph."""
        return self._adj.keys()

    def add_node(self, label: object) -> None:
        """Adds a node with a given label to the graph."""

        if label in self._adj:
            raise ValueError('node {0} already in graph'.format(label))

        self._adj[label] = {}
        self._node_count += 1

    def has_node(self, label: object) -> bool:
        """Determines if the graph contains a vertex with the given label."""
        return label in self._adj

    def _assert_node(self, label: object) -> None:
        if label not in self._adj:
            raise ValueError('no node {0} in graph'.format(label))

    def add_edge(
            self,
            source: object,
            dest: object,
            weight: float = 1,
            bidirectional: bool = False) -> None:

        """Adds edge (source, dest) with specified weight to the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest in self._adj[source]:
            raise ValueError(
                'edge ({0}, {1}) already in graph'.format(source, dest))

        self._adj[source][dest] = weight
        self._edge_count += 1
        if bidirectional:
            self._adj[dest][source] = weight
            self._edge_count += 1

    def has_edge(self, source: object, dest: object) -> bool:
        """Determines if the graph contains an edge from source to dest."""

        self._assert_node(source)
        self._assert_node(dest)

        return dest in self._adj[source]

    def update_edge(self, source: object, dest: object, weight: float) -> None:
        """Updates the weight of edge (source, dest) in the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest not in self._adj[source]:
            raise ValueError(
                'edge ({0}, {1}) not in graph'.format(source, dest))

        self._adj[source][dest] = weight

    def neighbors(self, label: object) -> Iterable[object]:
        """Returns an iterable of the vertices adjacent to the vertex with
        specified label in the graph.
        """

        self._assert_node(label)

        return self._adj[label].keys()

    def edge_weight(self, source: object, dest: object) -> float:
        """Returns the weight of edge (source, dest) in the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest not in self._adj[source]:
            raise ValueError('no such edge ({0}, {1})'.format(source, dest))

        return self._adj[source][dest]

    def try_add_matrix_edge(
            self, matrix: IntMatrix, node: object, row: int, col: int) -> None:

        """Adds edge from node to (row, col) if a valid matrix index."""

        n = len(matrix)
        m = 0 if n == 0 else len(matrix[0])
        if 0 <= row < n and 0 <= col < m:
            self.add_edge(node, (row, col), matrix[row][col])

    def reverse(self) -> 'Graph':
        """Returns a copy of the graph with all edge directions reversed."""

        # add all nodes to reverse graph
        rev_graph = Graph()
        for node in self._adj:
            rev_graph.add_node(node)

        # add reverse of all edges
        for node, edges in self._adj.items():
            for neighbor, weight in edges.items():
                rev_graph._adj[neighbor][node] = weight
                rev_graph._edge_count += 1

        return rev_graph

    def postorder(self) -> Sequence[object]:
        """Returns a postorder traversal of all nodes in the graph."""

        post = [] # type: List[object]

        # run DFS from each unvisited node in the graph
        visited = set() # type: Set[object]
        for node in self._adj:
            if node not in visited:
                self._postorder_dfs(node, set(), visited, post)

        return post

    def _postorder_dfs(
            self,
            node: object,
            path: Set[object],
            visited: Set[object],
            post: List[object]) -> None:
        
        """Helper function for postorder that runs DFS from a given node."""

        path.add(node)
        visited.add(node)

        for neighbor in self._adj[node]:
            # has a cycle if neighbor is an earlier node on path
            if neighbor in path:
                raise RuntimeError('graph contains a cycle')

            # continue searching from neighbors of node
            if neighbor not in visited:
                self._postorder_dfs(neighbor, path.copy(), visited, post)

        post.append(node)

    def bfs(self, source: object)\
            -> Tuple[Mapping[object, float], Mapping[object, object]]:
        
        """Runs breadth-first search from a source node in the graph.

        Returns two dicts that map each node to its distance from source and
        to the previous node along the search path from source to that node.
        """

        self._assert_node(source)

        distance = {source: 0} # type: Dict[object, float]
        previous = {} # type: Dict[object, object]
        visited = {source} # type: Set[object]

        # queue of nodes to be visited in order
        frontier = deque() # type: deque
        frontier.append(source)

        # visit each node in FIFO order, adding its neighbors
        while frontier:
            node = frontier.popleft()
            for neighbor in self._adj[node]:
                if neighbor not in visited:
                    distance[neighbor] = distance[node] + 1
                    previous[neighbor] = node
                    visited.add(neighbor)
                    frontier.append(neighbor)

        return distance, previous

    def dijkstra(self, source: object)\
            -> Tuple[Mapping[object, float], Mapping[object, object]]:

        """Runs Djikstra's shortest path algorithm from a source node.

        Returns two dicts that map each node to its distance from source and
        to the previous node along a shortest path from source to that node.
        """

        self._assert_node(source)

        distance = {source: 0} # type: Dict[object, float]
        previous = {} # type: Dict[object, object]

        # initialize node distances to positive infinity
        pq = MinPQ()
        for node in self._adj:
            if node != source:
                distance[node] = float('inf')
                previous[node] = None

            pq.put(node, distance[node])

        # visit nodes in priority order along explored paths
        while not pq.is_empty():
            node = pq.pop_min()
            for neighbor in self._adj[node]:
                path_cost = distance[node] + self._adj[node][neighbor]

                # update distance to node when shorter path found
                if path_cost < distance[neighbor]:
                    distance[neighbor] = path_cost
                    previous[neighbor] = node
                    pq.put(neighbor, path_cost)

        return distance, previous

    def prim_mst(self) -> Iterable[Tuple[object, object]]:
        """Runs Prim's minimum spanning tree algorithm for an undirected graph.

        Returns the edges in a minimum spanning tree for this graph if one
        exists. Otherwise, returns the edges in a minimum spanning forest,
        formed from minimum spanning trees in each component of the graph.
        """

        is_added = {} # type: Dict[object, bool]
        distance = {} # type: Dict[object, float]
        mst_edge = {} # type: Dict[object, object]

        # start with no tree and infinite distance to all nodes
        for node in self._adj:
            is_added[node] = False
            distance[node] = float('inf')

        # run algorithm from each vertex in the graph
        pq = MinPQ()
        for source in self._adj:
            # vertex already included in tree
            if is_added[source]:
                continue

            # enqueue source vertex with distance 0
            distance[source] = 0
            pq.put(source, 0)

            # repeatedly grow tree by picking adjacent edge with min weight
            while not pq.is_empty():
                node = pq.pop_min()
                is_added[node] = True
                for neighbor in self._adj[node]:
                    # don't add edge if it was already rejected
                    if is_added[neighbor]:
                        continue

                    # add edge if it gives best current distance to node
                    if self._adj[node][neighbor] < distance[neighbor]:
                        distance[neighbor] = self._adj[node][neighbor]
                        mst_edge[neighbor] = node
                        pq.put(neighbor, distance[neighbor])

        # yield all edges (u, v) in tree
        for edge in mst_edge.items():
            yield edge


class MinPQ(object):
    """Class representing a minimum priority queue that supports update-key.

    Adapted from: https://docs.python.org/3/library/heapq.html
    """

    def __init__(self) -> None:
        self._heap = [] # type: List[List[object]]
        self._entry_map = {} # type: Dict[object, List[object]]
        self._counter = itertools.count()

    def __len__(self) -> int:
        return len(self._entry_map)

    def is_empty(self) -> bool:
        """Determines if the priority queue is empty."""
        return not self._entry_map

    def put(self, value: object, priority: Comparable = 0) -> None:
        """Inserts a value with priority into the queue, or updates the value's
        priority if it is already contained in the priority queue.
        """

        if value in self._entry_map:
            self.delete(value)

        entry = [priority, next(self._counter), value]
        self._entry_map[value] = entry
        heapq.heappush(self._heap, entry)

    def delete(self, value: object) -> None:
        """Removes the given value from the priority queue."""

        if value not in self._entry_map:
            raise KeyError('value {0} not present in MinPQ'.format(value))

        entry = self._entry_map.pop(value)
        entry[-1] = None

    def pop_min(self) -> object:
        """Deletes and returns the minimum element in the priority queue."""
        while self._heap:
            value = heapq.heappop(self._heap)[-1]
            if value is not None:
                del self._entry_map[value]
                return value
        raise KeyError('cannot pop from an empty MinPQ')


def bisect_index(
        check: Callable[[int], bool],
        known_f: int = 0,
        known_t: Optional[int] = None) -> int:

    """Given a function that bisects indices >= known_f into False and True
    regions, finds the first index for which it flips from False to True."""

    # if only a False index is known, search for a True index
    if known_t is None:
        step_size = 1
        i = known_f + 1
        while not check(i):
            # search forward with increasingly large step size
            step_size *= 2
            i += step_size
        known_t = i

    # binary search over indices to find first True index
    while known_f < known_t - 1:
        mid = (known_f + known_t) // 2
        if not check(mid):
            known_f = mid
        else:
            known_t = mid

    return known_t


def memoized(func: Callable) -> Callable:
    """Decorator that caches the result of calling func with a particular set
    of arguments and returns this result for subsequent calls to function with
    the same arguments.
    """

    memo = {} # type: Dict[Any, Any]

    def memo_func(*args: Any) -> Any:
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return memo_func


def simple_equality(cls: Type) -> Type:
    """Decorator that defines a missing equality operation as the inverse of
    one provided for a class."""

    # Check for existence of user-defined equality operations
    eq_attr = '__eq__'
    ne_attr = '__ne__'
    has_eq = getattr(cls, eq_attr, None) is not getattr(object, eq_attr, None)
    has_ne = getattr(cls, ne_attr, None) is not getattr(object, ne_attr, None)

    if has_eq == has_ne:
        raise ValueError('must define exactly one equality operation: == !=')
    elif has_eq:
        def __ne__(a: object, b: object) -> bool:
            return not a.__eq__(b)
        setattr(cls, ne_attr, __ne__)
    else:
        def __eq__(a: object, b: object) -> bool:
            return not a.__ne__(b)
        setattr(cls, eq_attr, __eq__)
    return cls
