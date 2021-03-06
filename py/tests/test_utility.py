#!/usr/bin/env python3

"""test_utility.py

Unit test for the 'utility' common module.
"""
from typing import Mapping, Optional, Set

__author__ = 'Curtis Belmonte'

import unittest

import common.utility as util
from common.utility import Graph, MinPQ, memoized, simple_equality


class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = Graph()

    def test_nodes(self) -> None:
        self.assertEqual(self.graph.num_nodes(), 0)
        self.assertCountEqual(self.graph.nodes(), [])
        self.assertFalse(self.graph.has_node('node_1'))
        self.assertFalse(self.graph.has_node('node_2'))

        self.graph.add_node('node_1')
        self.assertEqual(self.graph.num_nodes(), 1)
        self.assertCountEqual(self.graph.nodes(), ['node_1'])
        self.assertTrue(self.graph.has_node('node_1'))
        self.assertFalse(self.graph.has_node('node_2'))

        self.graph.add_node('node_2')
        self.assertEqual(self.graph.num_nodes(), 2)
        self.assertCountEqual(self.graph.nodes(), ['node_1', 'node_2'])
        self.assertTrue(self.graph.has_node('node_1'))
        self.assertTrue(self.graph.has_node('node_2'))

        with self.assertRaises(ValueError):
            self.graph.add_node('node_1')
        self.assertEqual(self.graph.num_nodes(), 2)
        self.assertTrue(self.graph.has_node('node_1'))
        self.assertTrue(self.graph.has_node('node_2'))

    def test_edges(self) -> None:
        self.graph.add_node(0)
        self.graph.add_node(1)
        self.assertEqual(self.graph.num_edges(), 0)
        self.assertFalse(self.graph.has_edge(0, 0))
        self.assertFalse(self.graph.has_edge(1, 1))
        with self.assertRaises(ValueError):
            self.graph.has_edge(0, 2)
        with self.assertRaises(ValueError):
            self.graph.has_edge(2, 1)

        self.graph.add_edge(0, 1)
        self.assertEqual(self.graph.num_edges(), 1)
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertFalse(self.graph.has_edge(1, 0))

        with self.assertRaises(ValueError):
            self.graph.add_edge(0, 1)

        self.graph.update_edge(0, 1, 2)
        with self.assertRaises(ValueError):
            self.graph.update_edge(1, 0, 2)
        self.assertEqual(self.graph.num_edges(), 1)
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertFalse(self.graph.has_edge(1, 0))
        self.assertEqual(self.graph.edge_weight(0, 1), 2)
        with self.assertRaises(ValueError):
            self.graph.edge_weight(1, 0)

        self.graph.add_edge(1, 0, 3)
        self.assertEqual(self.graph.num_edges(), 2)
        self.assertTrue(self.graph.has_edge(0, 1))
        self.assertTrue(self.graph.has_edge(1, 0))
        self.assertEqual(self.graph.edge_weight(0, 1), 2)
        self.assertEqual(self.graph.edge_weight(1, 0), 3)

        self.graph.add_edge(1, 1)
        self.assertEqual(self.graph.num_edges(), 3)
        self.assertFalse(self.graph.has_edge(0, 0))
        self.assertTrue(self.graph.has_edge(1, 1))

    def test_neighbors(self) -> None:
        for i in range(6):
            self.graph.add_node(i)
        self.graph.add_edge(0, 0)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 4)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 0)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(3, 2)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(5, 3)
        self.graph.add_edge(5, 4)

        self.assertCountEqual(self.graph.neighbors(0), [0, 1, 4])
        self.assertCountEqual(self.graph.neighbors(1), [2])
        self.assertCountEqual(self.graph.neighbors(2), [0, 1])
        self.assertCountEqual(self.graph.neighbors(3), [2])
        self.assertCountEqual(self.graph.neighbors(4), [5])
        self.assertCountEqual(self.graph.neighbors(5), [3, 4])

    def test_reverse(self) -> None:
        for i in range(4):
            self.graph.add_node(i)
        self.graph.add_edge(0, 0)
        self.graph.add_edge(0, 3)
        self.graph.add_edge(1, 0)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 0)
        self.graph.add_edge(3, 1)

        rev_graph = self.graph.reverse()
        self.assertEqual(rev_graph.num_edges(), 7)
        self.assertTrue(rev_graph.has_edge(0, 0))
        self.assertTrue(rev_graph.has_edge(3, 0))
        self.assertTrue(rev_graph.has_edge(0, 1))
        self.assertTrue(rev_graph.has_edge(2, 1))
        self.assertTrue(rev_graph.has_edge(3, 2))
        self.assertTrue(rev_graph.has_edge(0, 3))
        self.assertTrue(rev_graph.has_edge(1, 3))

        self.assertEqual(self.graph.num_edges(), 7)
        self.assertTrue(self.graph.has_edge(0, 0))
        self.assertTrue(self.graph.has_edge(0, 3))
        self.assertTrue(self.graph.has_edge(1, 0))
        self.assertTrue(self.graph.has_edge(1, 2))
        self.assertTrue(self.graph.has_edge(2, 3))
        self.assertTrue(self.graph.has_edge(3, 0))
        self.assertTrue(self.graph.has_edge(3, 1))

    def test_postorder(self) -> None:
        for i in range(5):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)

        postorder = self.graph.postorder()
        self.assertEqual(len(postorder), 5)
        self.assertCountEqual(postorder[:2], [3, 4])
        self.assertCountEqual(postorder[2:4], [1, 2])
        self.assertEqual(postorder[4], 0)

        self.graph.add_edge(3, 0)
        with self.assertRaises(RuntimeError):
            self.graph.postorder()

    def _verify_reverse_path(
            self,
            prev: Mapping[object, object],
            source: object,
            node: object,
            dist: Optional[float] = None,
            seen: Optional[Set[object]] = None) -> None:

        """Tests if prev contains a reverse path from source to node.

        prev: Should map nodes to the previous node along a path from source
        source: The node that should be reached by following the reverse path
        node: The node which should have a reverse path in prev to source
        dist: If not None, the expected total cost of the path
        seen: If not None, the set of nodes already seen along the path

        This method fails if following nodes in prev starting from node does
        not lead to source along an existing path in self.graph.reverse(), or
        if dist is not None and the total cost of the path does not equal dist.
        """

        if seen is None:
            seen = set()

        if node == source:
            if dist is not None and dist > 0:
                self.fail('Distance along path less than expected')
            return

        if node in seen:
            self.fail('Cycle detected: Node {0} was already seen'.format(node))

        if node not in prev:
            self.fail('No previous node specified for ' + str(node))

        if not self.graph.has_edge(prev[node], node):
            self.fail('No edge {0}->{1} in graph'.format(prev[node], node))

        if dist is not None:
            dist -= self.graph.edge_weight(prev[node], node)
            if dist < 0:
                self.fail('Distance along path greater than expected')

        seen.add(node)
        self._verify_reverse_path(prev, source, prev[node], dist, seen)

    def test_bfs(self) -> None:
        for i in range(8):
            self.graph.add_node(i)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(1, 5)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(2, 6)
        self.graph.add_edge(3, 2)
        self.graph.add_edge(3, 7)
        self.graph.add_edge(4, 0)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(5, 6)
        self.graph.add_edge(6, 5)
        self.graph.add_edge(7, 3)
        self.graph.add_edge(7, 6)

        dist, prev = self.graph.bfs(0)
        self.assertCountEqual(dist.keys(), range(8))
        for node in prev:
            self._verify_reverse_path(prev, 0, node)

        dist, prev = self.graph.bfs(3)
        self.assertCountEqual(dist.keys(), [2, 3, 5, 6, 7])
        for node in prev:
            self._verify_reverse_path(prev, 3, node)

        dist, prev = self.graph.bfs(5)
        self.assertCountEqual(dist.keys(), [5, 6])
        for node in prev:
            self._verify_reverse_path(prev, 5, node)

    def test_dijkstra(self) -> None:
        labels = ['P', 'Q', 'R', 'S', 'T', 'U']
        for label in labels:
            self.graph.add_node(label)
        self.graph.add_edge('P', 'P', 1)
        self.graph.add_edge('P', 'Q', 1)
        self.graph.add_edge('P', 'S', 6)
        self.graph.add_edge('P', 'T', 7)
        self.graph.add_edge('Q', 'R', 1)
        self.graph.add_edge('Q', 'S', 4)
        self.graph.add_edge('R', 'S', 2)
        self.graph.add_edge('R', 'U', 1)
        self.graph.add_edge('S', 'R', 3)
        self.graph.add_edge('S', 'S', 0)
        self.graph.add_edge('S', 'T', 3)
        self.graph.add_edge('S', 'U', 2)
        self.graph.add_edge('T', 'U', 2)

        dist, prev = self.graph.dijkstra('P')
        self.assertCountEqual(dist.keys(), labels)
        self.assertEqual(dist['P'], 0)
        self.assertEqual(dist['Q'], 1)
        self.assertEqual(dist['R'], 2)
        self.assertEqual(dist['S'], 4)
        self.assertEqual(dist['T'], 7)
        self.assertEqual(dist['U'], 3)
        for node in prev:
            self._verify_reverse_path(prev, 'P', node, dist[node])

    def test_prim_mst(self) -> None:
        for label in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'):
            self.graph.add_node(label)
        self.graph.add_edge('A', 'B', 4, bidirectional=True)
        self.graph.add_edge('A', 'H', 8, bidirectional=True)
        self.graph.add_edge('B', 'C', 8, bidirectional=True)
        self.graph.add_edge('B', 'H', 11, bidirectional=True)
        self.graph.add_edge('C', 'D', 7, bidirectional=True)
        self.graph.add_edge('C', 'F', 4, bidirectional=True)
        self.graph.add_edge('C', 'I', 2, bidirectional=True)
        self.graph.add_edge('D', 'E', 9, bidirectional=True)
        self.graph.add_edge('D', 'F', 14, bidirectional=True)
        self.graph.add_edge('E', 'F', 10, bidirectional=True)
        self.graph.add_edge('F', 'G', 2, bidirectional=True)
        self.graph.add_edge('G', 'H', 1, bidirectional=True)
        self.graph.add_edge('G', 'I', 6, bidirectional=True)
        self.graph.add_edge('H', 'I', 7, bidirectional=True)

        mst_edges = list(self.graph.prim_mst())
        self.assertEqual(len(mst_edges), 8)
        self.assertEqual(
            sum(self.graph.edge_weight(u, v) for (u, v) in mst_edges), 37)


class TestMinPQ(unittest.TestCase):
    def setUp(self) -> None:
        self.min_pq = MinPQ()

    def test_empty(self) -> None:
        self.assertEqual(len(self.min_pq), 0)
        self.assertTrue(self.min_pq.is_empty())

    def test_put(self) -> None:
        self.min_pq.put('val_1')
        self.assertEqual(len(self.min_pq), 1)
        self.assertFalse(self.min_pq.is_empty())

        self.min_pq.put('val_2', 1)
        self.assertEqual(len(self.min_pq), 2)
        self.assertFalse(self.min_pq.is_empty())

        self.min_pq.put('val_1')
        self.assertEqual(len(self.min_pq), 2)
        self.assertFalse(self.min_pq.is_empty())

        self.min_pq.put('val_2', -1)
        self.assertEqual(len(self.min_pq), 2)
        self.assertFalse(self.min_pq.is_empty())

    def test_delete(self) -> None:
        for i in range(1, 4):
            self.min_pq.put(i)
        self.assertEqual(len(self.min_pq), 3)
        self.assertFalse(self.min_pq.is_empty())

        self.min_pq.delete(1)
        self.assertEqual(len(self.min_pq), 2)
        self.assertFalse(self.min_pq.is_empty())

        self.min_pq.delete(3)
        self.assertEqual(len(self.min_pq), 1)
        self.assertFalse(self.min_pq.is_empty())

        with self.assertRaises(KeyError):
            self.min_pq.delete(0)

        self.assertEqual(self.min_pq.pop_min(), 2)
        self.assertEqual(len(self.min_pq), 0)
        self.assertTrue(self.min_pq.is_empty())

    def test_pop_min(self) -> None:
        with self.assertRaises(KeyError):
            self.min_pq.pop_min()

        self.min_pq.put('A', 18)
        self.min_pq.put('B', 15)
        self.min_pq.put('C', 18)
        self.min_pq.put('D', 10)
        self.min_pq.put('E', 5)
        self.min_pq.put('F', 24)
        self.min_pq.put('G', 21)
        self.min_pq.put('H', 13)
        self.min_pq.put('I', 16)
        self.min_pq.put('J', 12)
        self.min_pq.put('K', 23)
        self.min_pq.put('A', 18)
        self.min_pq.put('G', 1)
        self.min_pq.put('D', 20)
        self.min_pq.put('K', 5)

        self.assertEqual(len(self.min_pq), 11)
        self.assertFalse(self.min_pq.is_empty())

        self.assertEqual(self.min_pq.pop_min(), 'G')
        self.assertCountEqual(
            [self.min_pq.pop_min(), self.min_pq.pop_min()],
            ['E', 'K'])
        self.assertEqual(self.min_pq.pop_min(), 'J')
        self.assertEqual(self.min_pq.pop_min(), 'H')
        self.assertEqual(self.min_pq.pop_min(), 'B')
        self.assertEqual(self.min_pq.pop_min(), 'I')
        self.assertCountEqual(
            [self.min_pq.pop_min(), self.min_pq.pop_min()],
            ['A', 'C'])
        self.assertEqual(self.min_pq.pop_min(), 'D')
        self.assertEqual(self.min_pq.pop_min(), 'F')

        with self.assertRaises(KeyError):
            self.min_pq.pop_min()
        self.assertEqual(len(self.min_pq), 0)
        self.assertTrue(self.min_pq.is_empty())


class TestUtility(unittest.TestCase):
    def test_bisect_index(self):
        self.assertEqual(util.bisect_index(lambda i: i > 0), 1)
        self.assertEqual(util.bisect_index(lambda i: i > 0, 0, 1), 1)
        self.assertEqual(util.bisect_index(lambda i: i > 0, 0, 2), 1)
        self.assertEqual(util.bisect_index(lambda i: i > 0, 0, 100), 1)
        self.assertEqual(util.bisect_index(lambda i: i > 5), 6)
        self.assertEqual(util.bisect_index(lambda i: i > 5, 2), 6)
        self.assertEqual(util.bisect_index(lambda i: i > 5, 3, 7), 6)
        self.assertEqual(
            util.bisect_index(lambda i: i < 4 or i > 20, 6), 21)
        self.assertEqual(
            util.bisect_index(lambda i: i < 4 or i > 20, 4, 34), 21)
        self.assertEqual(
            util.bisect_index(lambda i: i >= 78557, 12345, 82000), 78557)

    def test_memoized(self) -> None:
        @memoized
        def fib(n: int) -> int:
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)

        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(100), 354224848179261915075)

    def test_min_present(self) -> None:
        self.assertIsNone(util.min_present(None, None))
        self.assertEqual(util.min_present(0, None), 0)
        self.assertEqual(util.min_present(None, 0), 0)
        self.assertEqual(util.min_present(4, None), 4)
        self.assertEqual(util.min_present(None, 3), 3)
        self.assertEqual(util.min_present(-7, None), -7)
        self.assertEqual(util.min_present(None, -8), -8)
        self.assertEqual(util.min_present(-2, -2), -2)
        self.assertEqual(util.min_present(90, 82), 82)
        self.assertEqual(util.min_present(0, 2**32), 0)
        self.assertEqual(util.min_present(-41466, -75153), -75153)
        self.assertEqual(util.min_present('alpha', None), 'alpha')
        self.assertEqual(util.min_present(None, 'beta'), 'beta')
        self.assertEqual(util.min_present('alpha', 'beta'), 'alpha')

    def test_simple_equality(self) -> None:
        with self.assertRaises(ValueError):
            # noinspection PyUnusedLocal
            @simple_equality
            class NoEqualOps(object):
                pass

        with self.assertRaises(ValueError):
            # noinspection PyUnusedLocal
            @simple_equality
            class BothEqualOps(object):
                def __eq__(self, other: object) -> bool:
                    return False

                def __ne__(self, other: object) -> bool:
                    return True

        @simple_equality
        class EqualOp(object):
            def __eq__(self, other: object) -> bool:
                return isinstance(other, int)

        eq_object = EqualOp()
        self.assertTrue(eq_object == 0)
        self.assertFalse(eq_object == '0')
        self.assertFalse(eq_object == eq_object)
        self.assertFalse(eq_object != 0)
        self.assertTrue(eq_object != '0')
        self.assertTrue(eq_object != eq_object)

        @simple_equality
        class NotEqualOp(object):
            def __ne__(self, other: object) -> bool:
                return isinstance(other, int)

        ne_object = NotEqualOp()
        self.assertFalse(ne_object == 0)
        self.assertTrue(ne_object == '0')
        self.assertTrue(ne_object == ne_object)
        self.assertTrue(ne_object != 0)
        self.assertFalse(ne_object != '0')
        self.assertFalse(ne_object != ne_object)


if __name__ == '__main__':
    unittest.main()
