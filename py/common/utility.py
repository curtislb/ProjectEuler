#!/usr/bin/env python3

"""utility.py



Author: Curtis Belmonte
"""

import collections
import heapq
import itertools


class Graph(object):
    """Class representing a directed graph with weighted edges."""

    def __init__(self):
        self._adj = {}
        self._node_count = 0
        self._edge_count = 0

    def num_nodes(self):
        """Returns the number of vertices in the graph."""
        return self._node_count

    def num_edges(self):
        """Returns the number of edges in the graph."""
        return self._edge_count

    def nodes(self):
        """Returns an iterable of the unique vertices in the graph."""
        return self._adj.keys()

    def add_node(self, label):
        """Adds a node with a given label to the graph."""

        if label in self._adj:
            raise ValueError('Node ' + str(label) + ' already in graph')

        self._adj[label] = {}
        self._node_count += 1

    def has_node(self, label):
        """Determines if the graph contains a vertex with the given label."""
        return label in self._adj

    def _assert_node(self, label):
        if label not in self._adj:
            raise ValueError('No node ' + str(label) + ' in graph')

    def add_edge(self, source, dest, weight=1):
        """Adds edge (source, dest) with specified weight to the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest in self._adj[source]:
            raise ValueError(
                'Edge ({}, {}) already in graph'.format(source, dest))

        self._adj[source][dest] = weight
        self._edge_count += 1

    def has_edge(self, source, dest):
        """Determines if the graph contains an edge from source to dest."""

        self._assert_node(source)
        self._assert_node(dest)

        return dest in self._adj[source]

    def update_edge(self, source, dest, weight):
        """Updates the weight of edge (source, dest) in the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest not in self._adj[source]:
            raise ValueError(
                'Edge ({}, {}) not in graph'.format(source, dest))

        self._adj[source][dest] = weight

    def neighbors(self, label):
        """Returns an iterable of the vertices adjacent to the vertex with
        specified label in the graph."""

        self._assert_node(label)

        return self._adj[label].keys()

    def edge_weight(self, source, dest):
        """Returns the weight of edge (source, dest) in the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest not in self._adj[source]:
            raise ValueError('No such edge ({}, {})'.format(source, dest))

        return self._adj[source][dest]

    def reverse(self):
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

    def postorder(self):
        """Returns a postorder traversal of all nodes in the graph."""

        post = []

        # run DFS from each unvisited node in the graph
        visited = set()
        for node in self._adj:
            if node not in visited:
                self._postorder_dfs(node, set(), visited, post)

        return post

    def _postorder_dfs(self, node, path, visited, post):
        """Helper function for postorder that runs DFS from a given node."""

        path.add(node)
        visited.add(node)

        for neighbor in self._adj[node]:
            # has a cycle if neighbor is an earlier node on path
            if neighbor in path:
                raise RuntimeError('Graph contains a cycle')

            # continue searching from neighbors of node
            if neighbor not in visited:
                self._postorder_dfs(neighbor, path.copy(), visited, post)

        post.append(node)

    def bfs(self, source):
        """Runs breadth-first search from a source node in the graph.

        Returns two dicts that map each node to its distance from source and
        to the previous node along the search path from source to that node."""

        self._assert_node(source)

        distance = {source: 0}
        previous = {}
        visited = {source}

        # queue of nodes to be visited in order
        frontier = collections.deque()
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

    def dijkstra(self, source):
        """Runs Djikstra's shortest path algorithm from a source node.

        Returns two dicts that map each node to its distance from source and
        to the previous node along a shortest path from source to that node."""

        self._assert_node(source)

        distance = {source: 0}
        previous = {}

        # initialize node distances to positive inifnity
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

    def try_add_matrix_edge(self, matrix, node, row, col):
        """Adds edge from node to (row, col) if a valid matrix index."""
        n = len(matrix)
        if 0 <= row < n and 0 <= col < n:
            self.add_edge(node, (row, col), matrix[row][col])


class MinPQ(object):
    """Class representing a minimum priority queue that supports update-key.

    Adapted from: https://docs.python.org/3/library/heapq.html"""

    def __init__(self):
        self._heap = []
        self._entry_map = {}
        self._counter = itertools.count()

    def __len__(self):
        return len(self._entry_map)

    def is_empty(self):
        """Determines if the priority queue is empty."""
        return not self._entry_map

    def put(self, value, priority=0):
        """Inserts a value with priority into the queue, or updates the value's
        priority if it is already contained in the priority queue."""

        if value in self._entry_map:
            self.delete(value)

        entry = [priority, next(self._counter), value]
        self._entry_map[value] = entry
        heapq.heappush(self._heap, entry)

    def delete(self, value):
        """Removes the given value from the priority queue."""

        if value not in self._entry_map:
            raise KeyError('Value {0} not present in MinPQ'.format(value))

        entry = self._entry_map.pop(value)
        entry[-1] = None

    def pop_min(self):
        """Deletes and returns the minimum element in the priority queue."""

        if self.is_empty():
            raise KeyError('Cannot pop from an empty MinPQ')

        while self._heap:
            value = heapq.heappop(self._heap)[-1]
            if value is not None:
                del self._entry_map[value]
                return value


def memoized(func):
    """Decorator that caches the result of calling func with a particular set
    of arguments and returns this result for subsequent calls to function with
    the same arguments.
    """

    memo = {}

    def memo_func(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return memo_func
