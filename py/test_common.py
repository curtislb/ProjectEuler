#!/usr/bin/env python3

"""test_common.py

Module for unit testing of functions and classes in the common module.

Author: Curtis Belmonte
"""

import unittest
from fractions import Fraction

import common as com
from common import Graph, MinPQ


# TEST CLASSES ################################################################


class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_nodes(self):
        self.assertEqual(self.graph.num_nodes(), 0)
        self.assertEqual(len(self.graph.nodes()), 0)
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

    def test_edges(self):
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

    def test_neighbors(self):
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

    def test_reverse(self):
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

    def test_postorder(self):
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

    def _verify_reverse_path(self, prev, source, node, dist=None, seen=None):
        """Tests if prev contains a reverse path from source to node.

        prev    Should map nodes to the previous node along a path from source
        source  The node that should be reached by following the reverse path
        node    The node which should have a reverse path in prev to source
        dist    If not None, the expected total cost of the path
        seen    If not None, the set of nodes already seen along the path

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

    def test_bfs(self):
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

    def test_dijkstra(self):
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


class TestMinPQMethods(unittest.TestCase):

    def setUp(self):
        self.min_pq = MinPQ()

    def test_empty(self):
        self.assertEqual(len(self.min_pq), 0)
        self.assertTrue(self.min_pq.is_empty())

    def test_put(self):
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

    def test_delete(self):
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

    def test_pop_min(self):
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


# TEST FUNCTIONS ##############################################################


class TestCommonFunctions(unittest.TestCase):

    def test_alpha_char_lower(self):
        self.assertEqual(com.alpha_char_lower(1), 'a')
        self.assertEqual(com.alpha_char_lower(11), 'k')
        self.assertEqual(com.alpha_char_lower(26), 'z')

    def test_alpha_char_upper(self):
        self.assertEqual(com.alpha_index_upper('A'), 1)
        self.assertEqual(com.alpha_index_upper('Q'), 17)
        self.assertEqual(com.alpha_index_upper('Z'), 26)

    def test_argmax(self):
        self.assertEqual(com.argmax([[]]), 0)
        self.assertEqual(com.argmax('LOOOL'), 1)
        self.assertEqual(com.argmax(range(5)), 4)
        self.assertEqual(com.argmax([12, 34, 39, 5, 30]), 2)
        self.assertEqual(com.argmax([-1, 6, -8, 6, -8]), 1)

    def test_argmin(self):
        self.assertEqual(com.argmin([[]]), 0)
        self.assertEqual(com.argmin('LOOOL'), 0)
        self.assertEqual(com.argmin(range(5)), 0)
        self.assertEqual(com.argmin([12, 34, 39, 5, 30]), 3)
        self.assertEqual(com.argmin([-1, 6, -8, 6, -8]), 2)

    def test_arithmetic_product(self):
        self.assertEqual(com.arithmetic_product(3, 1), 3)
        self.assertEqual(com.arithmetic_product(3, 1, 1), 3)
        self.assertEqual(com.arithmetic_product(3, 1, 2), 3)
        self.assertEqual(com.arithmetic_product(1, 2, -1), 0)
        self.assertEqual(com.arithmetic_product(19, 5, 4), 12801915)
        self.assertEqual(com.arithmetic_product(13, 6, -3), -7280)
        self.assertEqual(com.arithmetic_product(-2, 6, 3), -7280)

    def test_arithmetic_series(self):
        self.assertEqual(com.arithmetic_series(4, 1), 4)
        self.assertEqual(com.arithmetic_series(4, 1, 1), 4)
        self.assertEqual(com.arithmetic_series(4, 1, 2), 4)
        self.assertEqual(com.arithmetic_series(1, 2, -1), 1)
        self.assertEqual(com.arithmetic_series(19, 5, 4), 135)
        self.assertEqual(com.arithmetic_series(7, 8, -3), -28)
        self.assertEqual(com.arithmetic_series(-14, 8, 3), -28)

    def test_binary_search(self):
        self.assertIsNone(com.binary_search([], 0))
        self.assertIsNone(com.binary_search([], 'x'))
        self.assertIsNone(com.binary_search([], None))

        self.assertIsNone(com.binary_search(['xy'], 'x'))
        self.assertEqual(com.binary_search(['xy'], 'xy'), 0)
        self.assertEqual(com.binary_search('xy', 'x'), 0)
        self.assertEqual(com.binary_search('xy', 'y'), 1)
        self.assertIsNone(com.binary_search('xy', 'z'))

        seq = [[0],  [0, 1], [1, 0], [1, 1, 0]]
        self.assertEqual(com.binary_search(seq, [1, 0]), 2)
        self.assertIsNone(com.binary_search(seq, [0, 0]))
        self.assertIsNone(com.binary_search(seq, []))

        seq = [0, 5, 5, 13, 19, 22, 41, 55, 68, 68, 72, 81, 98]
        self.assertEqual(com.binary_search(seq, 55), 7)
        self.assertIn(com.binary_search(seq, 5), [1, 2])
        self.assertEqual(com.binary_search(seq, 0), 0)
        self.assertEqual(com.binary_search(seq, 98), 12)
        self.assertIsNone(com.binary_search(seq, 23))

    def test_choose(self):
        self.assertEqual(com.choose(0, 0), 1)
        self.assertEqual(com.choose(1, 0), 1)
        self.assertEqual(com.choose(1, 1), 1)
        self.assertEqual(com.choose(2, 0), 1)
        self.assertEqual(com.choose(2, 1), 2)
        self.assertEqual(com.choose(2, 2), 1)
        self.assertEqual(com.choose(3, 0), 1)
        self.assertEqual(com.choose(3, 1), 3)
        self.assertEqual(com.choose(3, 2), 3)
        self.assertEqual(com.choose(3, 3), 1)
        self.assertEqual(com.choose(4, 0), 1)
        self.assertEqual(com.choose(4, 1), 4)
        self.assertEqual(com.choose(4, 2), 6)
        self.assertEqual(com.choose(4, 3), 4)
        self.assertEqual(com.choose(4, 4), 1)
        self.assertEqual(com.choose(12, 5), 792)
        self.assertEqual(com.choose(84, 26), 3496176570135581124912)
        self.assertEqual(
            com.choose(309, 254),
            41885714195904323564014555767112516232542200976007970465503616)

    def test_collatz_step(self):
        self.assertEqual(com.collatz_step(1), 4)
        self.assertEqual(com.collatz_step(2), 1)
        self.assertEqual(com.collatz_step(4), 2)
        self.assertEqual(com.collatz_step(-1), -2)
        self.assertEqual(com.collatz_step(-2), -1)
        self.assertEqual(com.collatz_step(23), 70)
        self.assertEqual(com.collatz_step(42), 21)
        self.assertEqual(com.collatz_step(1337), 4012)
        self.assertEqual(com.collatz_step(2048), 1024)

    def test_combination_sums(self):
        with self.assertRaises(ValueError):
            com.combination_sums(1, [1, 0, 2])
        with self.assertRaises(ValueError):
            com.combination_sums(2, [1, 2, -1])
        with self.assertRaises(ValueError):
            com.combination_sums(0, [1])
        with self.assertRaises(ValueError):
            com.combination_sums(-1, [1])
        with self.assertRaises(ValueError):
            com.combination_sums(-1, [-1])

        self.assertEqual(com.combination_sums(1, []), 0)
        self.assertEqual(com.combination_sums(1, [1]), 1)
        self.assertEqual(com.combination_sums(1, [1, 2]), 1)
        self.assertEqual(com.combination_sums(1, [2, 1]), 1)
        self.assertEqual(com.combination_sums(2, [1, 2]), 2)
        self.assertEqual(com.combination_sums(2, [1, 1]), 3)
        self.assertEqual(com.combination_sums(3, [1, 2]), 2)
        self.assertEqual(com.combination_sums(3, [3, 1, 2]), 3)
        self.assertEqual(com.combination_sums(100, [1, 5, 10, 25, 50]), 292)
        self.assertEqual(com.combination_sums(100, (25, 50, 10, 1, 5)), 292)
        self.assertEqual(
            com.combination_sums(500, [1, 5, 10, 25, 50, 100, 200, 500]),
            111023)

    def test_compute_chain_lengths(self):
        lengths = {}
        values = [0] + list(range(3, 9))

        def incr(x):
            return (2 if x == 0 else
                    4 if x == 3 else
                    6 if x == 5 else
                    x - 1)

        def is_valid(x):
            return x != 6

        com.compute_chain_lengths(lengths, values, incr, is_valid)

        self.assertEqual(lengths[0], 3)
        self.assertEqual(lengths[1], 3)
        self.assertEqual(lengths[2], 3)
        self.assertEqual(lengths[3], 2)
        self.assertEqual(lengths[4], 2)
        self.assertFalse(5 in lengths)
        self.assertFalse(6 in lengths)
        self.assertFalse(7 in lengths)
        self.assertFalse(8 in lengths)

    def test_concat_digits(self):
        self.assertEqual(com.concat_digits([0]), 0)
        self.assertEqual(com.concat_digits([1]), 1)
        self.assertEqual(com.concat_digits([0, 1]), 1)
        self.assertEqual(com.concat_digits([1, 2]), 12)
        self.assertEqual(com.concat_digits((3, 2, 1)), 321)
        self.assertEqual(com.concat_digits(range(0, 7, 2)), 246)
        self.assertEqual(com.concat_digits([1, 0, 0, 1], 2), 9)
        self.assertEqual(com.concat_digits([1, 7, 3, 4], 8), 988)
        self.assertEqual(com.concat_digits([3, 'D', 'c', 0], 16), 15808)

    def test_concat_numbers(self):
        self.assertEqual(com.concat_numbers(0, 1), 1)
        self.assertEqual(com.concat_numbers(1, 0), 10)
        self.assertEqual(com.concat_numbers(2, 3), 23)
        self.assertEqual(com.concat_numbers(-2, 3), -23)
        self.assertEqual(com.concat_numbers(123, 45), 12345)
        self.assertEqual(com.concat_numbers(1, 2345), 12345)
        with self.assertRaises(ValueError):
            com.concat_numbers(2, -3)

    def test_count_digits(self):
        self.assertEqual(com.count_digits(0), 1)
        self.assertEqual(com.count_digits(1), 1)
        self.assertEqual(com.count_digits(9), 1)
        self.assertEqual(com.count_digits(10), 2)
        self.assertEqual(com.count_digits(1337), 4)
        self.assertEqual(com.count_digits(63184285379), 11)

    def test_count_divisors(self):
        div_cts = [1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2, 6]
        for i, n in enumerate(div_cts):
            self.assertEqual(com.count_divisors(i + 1), n)
        self.assertEqual(com.count_divisors(4200), 48)
        self.assertEqual(com.count_divisors(15485863), 2)

    def test_count_divisors_up_to(self):
        self.assertEqual(com.count_divisors_up_to(0), [0])
        self.assertEqual(com.count_divisors_up_to(1), [0, 1])
        self.assertEqual(com.count_divisors_up_to(2), [0, 1, 2])
        self.assertEqual(com.count_divisors_up_to(3), [0, 1, 2, 2])
        self.assertEqual(com.count_divisors_up_to(4), [0, 1, 2, 2, 3])
        self.assertEqual(
            com.count_divisors_up_to(43),
            [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, 4, 5, 2, 6, 2, 6, 4,
             4, 2, 8, 3, 4, 4, 6, 2, 8, 2, 6, 4, 4, 4, 9, 2, 4, 4, 8, 2, 8, 2])

    def test_count_prime_factors(self):
        self.assertEqual(com.count_prime_factors(1), 0)
        self.assertEqual(com.count_prime_factors(1, []), 0)
        self.assertEqual(com.count_prime_factors(2), 1)
        self.assertEqual(com.count_prime_factors(2, [2]), 1)
        self.assertEqual(com.count_prime_factors(3), 1)
        self.assertEqual(com.count_prime_factors(3, [2, 3]), 1)
        self.assertEqual(com.count_prime_factors(3, [2, 3, 5]), 1)
        self.assertEqual(com.count_prime_factors(4), 1)
        self.assertEqual(com.count_prime_factors(4, [2]), 1)
        self.assertEqual(com.count_prime_factors(4, [2, 3, 5]), 1)
        self.assertEqual(com.count_prime_factors(12), 2)
        self.assertEqual(com.count_prime_factors(12, [2, 3]), 2)
        self.assertEqual(com.count_prime_factors(12, [2, 3, 5, 7, 11]), 2)
        self.assertEqual(
            com.count_prime_factors(30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
            3)
        self.assertEqual(com.count_prime_factors(360), 3)
        self.assertEqual(com.count_prime_factors(1327), 1)
        self.assertEqual(com.count_prime_factors(4200), 4)

    def test_cross_product_3d(self):
        self.assertEqual(com.cross_product_3d((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(com.cross_product_3d([0, 0, 0], [0, 0, 0]), (0, 0, 0))
        self.assertEqual(
            com.cross_product_3d((2, 3, 4), (5, 6, 7)),
            (-3, 6, -3))
        self.assertEqual(
            com.cross_product_3d((3, -3, 1), (4, 9, 2)),
            (-15, -2, 39))
        self.assertEqual(
            com.cross_product_3d((3, -3, 1), (-12, 12, -4)),
            (0, 0, 0))

    def test_cumulative_partial_sum(self):
        self.assertEqual(com.cumulative_partial_sum([1]), [1])
        self.assertEqual(com.cumulative_partial_sum([1, 2, 3]), [1, 3, 6])
        self.assertEqual(com.cumulative_partial_sum([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(com.cumulative_partial_sum([1, 2, 3], 2), [1, 3, 5])
        self.assertEqual(com.cumulative_partial_sum([-1, 2, -3]), [-1, 1, -2])
        self.assertEqual(
            com.cumulative_partial_sum(
                [9, -7, -1, 18, 25, -6, 14, -20, 0, 4, -18, 12, -3, 11, 6, -5],
                8),
            [9, 2, 1, 19, 44, 38, 52, 32, 23, 34, 17, 11, -17, 0, -8, 7])

    def test_dice_probability(self):
        self.assertEqual(com.dice_probability(1, 1, 1), 1)
        self.assertEqual(com.dice_probability(0, 1, 1), 0)
        self.assertEqual(com.dice_probability(2, 1, 1), 0)
        self.assertEqual(com.dice_probability(1, 1, 6), Fraction(1, 6))
        self.assertEqual(com.dice_probability(6, 1, 6), Fraction(1, 6))
        self.assertEqual(com.dice_probability(7, 1, 6), 0)
        self.assertEqual(com.dice_probability(2, 2, 6), Fraction(1, 36))
        self.assertEqual(com.dice_probability(7, 2, 6), Fraction(1, 6))
        self.assertEqual(com.dice_probability(18, 5, 7), Fraction(190, 2401))

    def test_digit_counts(self):
        self.assertEqual(com.digit_counts(1), [0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(com.digit_counts(9), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(com.digit_counts(10), [1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(com.digit_counts(99), [0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
        self.assertEqual(com.digit_counts(1234567890), [1] * 10)
        self.assertEqual(
            com.digit_counts(490473284389948786968728452),
            [1, 0, 3, 2, 5, 1, 2, 3, 6, 4])

    def test_digit_function_sum(self):
        self.assertEqual(com.digit_function_sum(0, lambda x: x), 0)
        self.assertEqual(com.digit_function_sum(1, lambda x: x), 1)
        self.assertEqual(com.digit_function_sum(123, lambda x: x), 6)
        self.assertEqual(com.digit_function_sum(123, lambda x: x + 1), 9)
        self.assertEqual(com.digit_function_sum(123, lambda x: x**2), 14)
        self.assertEqual(
            com.digit_function_sum(7948531, lambda x: -x if x % 2 == 1 else x),
            -13)

    def test_digit_permutations(self):
        self.assertCountEqual(com.digit_permutations(1), [1])
        self.assertCountEqual(com.digit_permutations(2), [2])
        self.assertCountEqual(com.digit_permutations(10), [10])
        self.assertCountEqual(com.digit_permutations(11), [11])
        self.assertCountEqual(com.digit_permutations(12), [12, 21])
        self.assertCountEqual(
            com.digit_permutations(123),
            [123, 132, 213, 231, 312, 321])
        self.assertCountEqual(
            com.digit_permutations(1337),
            [1337, 1373, 1733, 3137, 3173, 3317, 3371, 3713, 3731, 7133, 7313,
             7331])

    def test_digit_rotations(self):
        self.assertCountEqual(com.digit_rotations(1), [1])
        self.assertCountEqual(com.digit_rotations(2), [2])
        self.assertCountEqual(com.digit_rotations(10), [1, 10])
        self.assertCountEqual(com.digit_rotations(11), [11])
        self.assertCountEqual(com.digit_rotations(12), [12, 21])
        self.assertCountEqual(com.digit_rotations(123), [123, 231, 312])
        self.assertCountEqual(
            com.digit_rotations(600316),
            [600316, 3166, 31660, 316600, 166003, 660031])

    def test_digit_truncations_left(self):
        self.assertCountEqual(com.digit_truncations_left(1), [1])
        self.assertCountEqual(com.digit_truncations_left(2), [2])
        self.assertCountEqual(com.digit_truncations_left(10), [10, 0])
        self.assertCountEqual(com.digit_truncations_left(12), [12, 2])
        self.assertCountEqual(com.digit_truncations_left(1002), [1002, 2])
        self.assertCountEqual(com.digit_truncations_left(123), [123, 23, 3])
        self.assertCountEqual(
            com.digit_truncations_left(600316),
            [600316, 316, 16, 6])

    def test_digit_truncations_right(self):
        self.assertCountEqual(com.digit_truncations_right(1), [1])
        self.assertCountEqual(com.digit_truncations_right(2), [2])
        self.assertCountEqual(com.digit_truncations_right(10), [10, 1])
        self.assertCountEqual(com.digit_truncations_right(12), [12, 1])
        self.assertCountEqual(com.digit_truncations_right(123), [123, 12, 1])
        self.assertCountEqual(
            com.digit_truncations_right(1002),
            [1002, 100, 10, 1])
        self.assertCountEqual(
            com.digit_truncations_right(600316),
            [600316, 60031, 6003, 600, 60, 6])

    def test_digits(self):
        self.assertEqual(com.digits(1), [1])
        self.assertEqual(com.digits(2), [2])
        self.assertEqual(com.digits(123), [1, 2, 3])
        self.assertEqual(com.digits(1337), [1, 3, 3, 7])
        self.assertEqual(
            com.digits(698873214754301820),
            [6, 9, 8, 8, 7, 3, 2, 1, 4, 7, 5, 4, 3, 0, 1, 8, 2, 0])

    def test_dot_product(self):
        self.assertEqual(com.dot_product((2,), (3,)), 6)
        self.assertEqual(com.dot_product([2], [3]), 6)
        self.assertEqual(com.dot_product((1, 2), (3, 4)), 11)
        self.assertEqual(com.dot_product((2, 3, 4), (5, 6, 7)), 56)
        self.assertEqual(
            com.dot_product((10, -3, -10, 8, 1), (7, 5, -1, -9, 8)),
            1)

    def test_factorial(self):
        self.assertEqual(com.factorial(0), 1)
        self.assertEqual(com.factorial(1), 1)
        self.assertEqual(com.factorial(2), 2)
        self.assertEqual(com.factorial(3), 6)
        self.assertEqual(com.factorial(4), 24)
        self.assertEqual(com.factorial(13), 6227020800)
        self.assertEqual(
            com.factorial(45),
            119622220865480194561963161495657715064383733760000000000)

    def test_fibonacci(self):
        self.assertEqual(com.fibonacci(0), 1)
        self.assertEqual(com.fibonacci(1), 1)
        self.assertEqual(com.fibonacci(2), 2)
        self.assertEqual(com.fibonacci(3), 3)
        self.assertEqual(com.fibonacci(4), 5)
        self.assertEqual(com.fibonacci(13), 377)
        self.assertEqual(com.fibonacci(37), 39088169)
        self.assertEqual(
            com.fibonacci(273),
            818706854228831001753880637535093596811413714795418360007)

    def test_flatten_matrix(self):
        self.assertEqual(com.flatten_matrix([[]]), [])
        self.assertEqual(com.flatten_matrix([[]], keep_indices=True), [])
        self.assertEqual(com.flatten_matrix([[1]]), [1])
        self.assertEqual(
            com.flatten_matrix([[1]], keep_indices=True),
            [(1, 0, 0)])
        self.assertEqual(com.flatten_matrix([[4, 3], [2, 1]]), [4, 3, 2, 1])
        self.assertEqual(
            com.flatten_matrix([['4', 3], [2, '1']], keep_indices=True),
            [('4', 0, 0), (3, 0, 1), (2, 1, 0), ('1', 1, 1)])
        self.assertEqual(
            com.flatten_matrix([[1, 2], [3], [4, 5, 6]], keep_indices=True),
            [(1, 0, 0), (2, 0, 1), (3, 1, 0), (4, 2, 0), (5, 2, 1), (6, 2, 2)])

    def test_gcd(self):
        self.assertEqual(com.gcd(2, 1), 1)
        self.assertEqual(com.gcd(2, 3), 1)
        self.assertEqual(com.gcd(2, 2), 2)
        self.assertEqual(com.gcd(2, 4), 2)
        self.assertEqual(com.gcd(20, 16), 4)
        self.assertEqual(com.gcd(54, 24), 6)
        self.assertEqual(com.gcd(45, 54), 9)
        self.assertEqual(com.gcd(30, 105), 15)
        self.assertEqual(com.gcd(452713601, 662853843), 3581)

    def test_get_digit(self):
        self.assertEqual(com.get_digit(1, 1), 1)
        self.assertEqual(com.get_digit(2, 1), 2)
        self.assertEqual(com.get_digit(123, 2), 2)
        self.assertEqual(com.get_digit(4567, 4), 7)
        self.assertEqual(com.get_digit(89, 0), 9)
        self.assertEqual(com.get_digit(201709364, 7), 3)

    def test_hexagonal(self):
        hex_nums = [0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325]
        for i, n in enumerate(hex_nums):
            self.assertEqual(com.hexagonal(i), n)
        self.assertEqual(com.hexagonal(42), 3486)
        self.assertEqual(com.hexagonal(6438), 82889250)

    def test_int_log(self):
        self.assertEqual(com.int_log(1), 0)
        self.assertEqual(com.int_log(2), 1)
        self.assertEqual(com.int_log(3), 1)
        self.assertEqual(com.int_log(0.9), 0)
        self.assertEqual(com.int_log(4.2), 1)
        self.assertEqual(com.int_log(1, 2), 0)
        self.assertEqual(com.int_log(2, 2), 1)
        self.assertEqual(com.int_log(3, 2), 2)
        self.assertEqual(com.int_log(0.9, 2), 0)
        self.assertEqual(com.int_log(4.2, 2), 2)
        self.assertEqual(com.int_log(317), 6)
        self.assertEqual(com.int_log(150.01, 10), 2)
        self.assertEqual(com.int_log(783651481.7329, 11.1), 9)
        self.assertEqual(com.int_log(0.28, 0.7), 4)

    def test_int_pow(self):
        self.assertEqual(com.int_pow(0, 1), 0)
        self.assertEqual(com.int_pow(1, 0), 1)
        self.assertEqual(com.int_pow(2, 0), 1)
        self.assertEqual(com.int_pow(2, 1), 2)
        self.assertEqual(com.int_pow(5, 9), 1953125)
        self.assertEqual(com.int_pow(5.2, 3.8), 526)
        self.assertEqual(com.int_pow(7.36, 4.42), 6786)
        self.assertEqual(com.int_pow(4.84, 2.226), 33)
        self.assertEqual(com.int_pow(0.21, 0.35), 1)

    def test_int_sqrt(self):
        self.assertEqual(com.int_sqrt(0), 0)
        self.assertEqual(com.int_sqrt(1), 1)
        self.assertEqual(com.int_sqrt(2), 1)
        self.assertEqual(com.int_sqrt(2.27), 2)
        self.assertEqual(com.int_sqrt(4.1), 2)
        self.assertEqual(com.int_sqrt(50.35), 7)
        self.assertEqual(com.int_sqrt(80166.213), 283)
        self.assertEqual(com.int_sqrt(0.148), 0)
        self.assertEqual(com.int_sqrt(0.541), 1)

    def test_int_to_base(self):
        self.assertEqual(com.int_to_base(1, 2), '1')
        self.assertEqual(com.int_to_base(1, 10), '1')
        self.assertEqual(com.int_to_base(2, 2), '10')
        self.assertEqual(com.int_to_base(2, 10), '2')
        self.assertEqual(com.int_to_base(25, 2), '11001')
        self.assertEqual(com.int_to_base(25, 3), '221')
        self.assertEqual(com.int_to_base(25, 5), '100')
        self.assertEqual(com.int_to_base(25, 8), '31')
        self.assertEqual(com.int_to_base(25, 10), '25')
        self.assertEqual(com.int_to_base(25, 16), '19')
        self.assertEqual(com.int_to_base(595129651, 36), '9uboz7')
        self.assertEqual(com.int_to_base(42, 3, '?!#'), '!!#?')

    def test_inverse_index_map(self):
        self.assertEqual(com.inverse_index_map([]), {})
        self.assertEqual(com.inverse_index_map('', False), {})
        self.assertEqual(com.inverse_index_map([2]), {2: 0})
        self.assertEqual(com.inverse_index_map([1], False), {1: [0]})
        self.assertEqual(com.inverse_index_map([3, 3], False), {3: [0, 1]})
        self.assertEqual(com.inverse_index_map('a'), {'a': 0})
        self.assertEqual(com.inverse_index_map((3, 2, 1)), {3: 0, 2: 1, 1: 2})
        self.assertEqual(
            com.inverse_index_map('XYZ'),
            {'X': 0, 'Y': 1, 'Z': 2})
        self.assertEqual(
            com.inverse_index_map((1, 6, 1, 8, 0, 3, 3, 9, 8, 8), False),
            {0: [4], 1: [0, 2], 3: [5, 6], 6: [1], 8: [3, 8, 9], 9: [7]})
        self.assertEqual(
            com.inverse_index_map('randomize'),
            {
                'r': 0,
                'a': 1,
                'n': 2,
                'd': 3,
                'o': 4,
                'm': 5,
                'i': 6,
                'z': 7,
                'e': 8,
            })

    def test_is_bouncy(self):
        self.assertFalse(com.is_bouncy(1))
        self.assertFalse(com.is_bouncy(9))
        self.assertFalse(com.is_bouncy(11))
        self.assertFalse(com.is_bouncy(12))
        self.assertFalse(com.is_bouncy(21))
        self.assertFalse(com.is_bouncy(111))
        self.assertFalse(com.is_bouncy(119))
        self.assertFalse(com.is_bouncy(199))
        self.assertFalse(com.is_bouncy(100))
        self.assertFalse(com.is_bouncy(110))
        self.assertFalse(com.is_bouncy(66420))
        self.assertFalse(com.is_bouncy(134468))
        self.assertFalse(com.is_bouncy(99964332))
        self.assertTrue(com.is_bouncy(120))
        self.assertTrue(com.is_bouncy(412))
        self.assertTrue(com.is_bouncy(525))
        self.assertTrue(com.is_bouncy(738))
        self.assertTrue(com.is_bouncy(12951))
        self.assertTrue(com.is_bouncy(21780))
        self.assertTrue(com.is_bouncy(155349))
        self.assertTrue(com.is_bouncy(277032))
        self.assertTrue(com.is_bouncy(47894411))

    def test_is_coprime_pair(self):
        self.assertTrue(com.is_coprime_pair(2, 1))
        self.assertTrue(com.is_coprime_pair(3, 1))
        self.assertFalse(com.is_coprime_pair(2, 2))
        self.assertTrue(com.is_coprime_pair(2, 3))
        self.assertFalse(com.is_coprime_pair(2, 4))
        self.assertFalse(com.is_coprime_pair(45, 21))
        self.assertFalse(com.is_coprime_pair(32, 58))
        self.assertTrue(com.is_coprime_pair(70, 27))
        self.assertTrue(com.is_coprime_pair(36, 77))
        self.assertTrue(com.is_coprime_pair(41327, 75600))
        self.assertTrue(com.is_coprime_pair(94753, 22416))
        self.assertFalse(com.is_coprime_pair(94755, 22416))

    def test_is_hexagonal(self):
        hex_nums = {1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325}
        for n in range(1, 350):
            self.assertEqual(com.is_hexagonal(n), n in hex_nums)
        self.assertFalse(com.is_hexagonal(971530876952))
        self.assertTrue(com.is_hexagonal(971530876953))
        self.assertFalse(com.is_hexagonal(971530876954))

    def test_is_leap_year(self):
        self.assertFalse(com.is_leap_year(1))
        self.assertTrue(com.is_leap_year(4))
        self.assertTrue(com.is_leap_year(40))
        self.assertFalse(com.is_leap_year(100))
        self.assertTrue(com.is_leap_year(104))
        self.assertTrue(com.is_leap_year(400))
        self.assertTrue(com.is_leap_year(1248))
        self.assertFalse(com.is_leap_year(1337))
        self.assertFalse(com.is_leap_year(1800))
        self.assertTrue(com.is_leap_year(1804))
        self.assertTrue(com.is_leap_year(1804))
        self.assertTrue(com.is_leap_year(2016))
        self.assertFalse(com.is_leap_year(2017))
        self.assertFalse(com.is_leap_year(2300))
        self.assertTrue(com.is_leap_year(2400))
        self.assertTrue(com.is_leap_year(4936))
        self.assertFalse(com.is_leap_year(4937))
        self.assertFalse(com.is_leap_year(4938))

    def test_is_palindrome(self):
        self.assertTrue(com.is_palindrome(1))
        self.assertTrue(com.is_palindrome(11))
        self.assertTrue(com.is_palindrome(22))
        self.assertFalse(com.is_palindrome(10))
        self.assertTrue(com.is_palindrome(101))
        self.assertFalse(com.is_palindrome(1212))
        self.assertTrue(com.is_palindrome(2332))
        self.assertTrue(com.is_palindrome(72427))
        self.assertTrue(com.is_palindrome(724427))
        self.assertTrue(com.is_palindrome(722444227))
        self.assertFalse(com.is_palindrome(513513))
        self.assertFalse(com.is_palindrome(551133))
        self.assertFalse(com.is_palindrome(5133150))

    def test_is_permutation(self):
        for cmp_cnts in (False, True):
            self.assertTrue(com.is_permutation([], set(), cmp_cnts))
            self.assertTrue(com.is_permutation('', iter([]), cmp_cnts))
            self.assertTrue(com.is_permutation(iter(()), range(0), cmp_cnts))
            self.assertFalse(com.is_permutation([1], (), cmp_cnts))
            self.assertFalse(com.is_permutation([], (2, 3), cmp_cnts))
            self.assertFalse(com.is_permutation([2], (2, 3), cmp_cnts))
            self.assertTrue(com.is_permutation({1}, [1], cmp_cnts))
            self.assertFalse(com.is_permutation([1], [2], cmp_cnts))
            self.assertTrue(com.is_permutation('12', '21', cmp_cnts))
            self.assertTrue(com.is_permutation('12', ['2', '1'], cmp_cnts))
            self.assertFalse(com.is_permutation('12', [1, 2], cmp_cnts))
            self.assertTrue(com.is_permutation((1, 4, 7), {7, 1, 4}, cmp_cnts))
            self.assertTrue(com.is_permutation('silent', 'listen', cmp_cnts))
            self.assertFalse(com.is_permutation('listen', 'tiles', cmp_cnts))
            self.assertTrue(
                com.is_permutation(
                    [37, 86, 19, 0, 4, 19, 655, 101, 4, 19],
                    [4, 37, 101, 4, 19, 86, 19, 655, 19, 0],
                    cmp_cnts))
            self.assertFalse(
                com.is_permutation(
                    [37, 86, 19, 0, 4, 655, 101, 4],
                    [4, 37, 101, 19, 86, 19, 655, 19, 0],
                    cmp_cnts))
            self.assertTrue(
                com.is_permutation(
                    iter([37, 86, 19, 0, 4, 19, 655, 101, 4, 19]),
                    iter([4, 37, 101, 4, 19, 86, 19, 655, 19, 0]),
                    cmp_cnts))
            self.assertFalse(
                com.is_permutation(
                    iter((37, 86, 19, 0, 4, 655, 101, 4)),
                    iter((4, 37, 101, 19, 86, 19, 655, 19, 0)),
                    cmp_cnts))

    def test_is_pentagonal(self):
        pent_nums = {1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247}
        for n in range(1, 250):
            self.assertEqual(com.is_pentagonal(n), n in pent_nums)
        self.assertFalse(com.is_pentagonal(728648331956))
        self.assertTrue(com.is_pentagonal(728648331957))
        self.assertFalse(com.is_pentagonal(728648331958))

    def test_is_power(self):
        self.assertTrue(com.is_power(1, 305))
        self.assertTrue(com.is_power(2, 1))
        self.assertTrue(com.is_power(3, 1))
        self.assertTrue(com.is_power(9024, 1))

        squares = set([n**2 for n in range(1, 23)])
        for n in range(1, 500):
            self.assertEqual(com.is_power(n, 2), n in squares)

        cubes = {1, 8, 27, 64, 125, 216, 343}
        for n in range(1, 350):
            self.assertEqual(com.is_power(n, 3), n in cubes)

        quarts = {1, 16, 81, 256}
        for n in range(1, 300):
            self.assertEqual(com.is_power(n, 4), n in quarts)

        self.assertFalse(com.is_power(48566960, 2))
        self.assertTrue(com.is_power(48566961, 2))
        self.assertFalse(com.is_power(48566962, 2))
        self.assertFalse(com.is_power(48566961, 3))
        self.assertFalse(com.is_power(48566961, 4))
        self.assertFalse(com.is_power(338463151208, 3))
        self.assertTrue(com.is_power(338463151209, 3))
        self.assertFalse(com.is_power(338463151210, 3))
        self.assertFalse(com.is_power(338463151209, 2))
        self.assertFalse(com.is_power(338463151209, 4))
        self.assertFalse(com.is_power(30821664720, 4))
        self.assertTrue(com.is_power(30821664721, 4))
        self.assertFalse(com.is_power(30821664722, 4))
        self.assertTrue(com.is_power(30821664721, 2))
        self.assertFalse(com.is_power(30821664721, 3))
        self.assertFalse(com.is_power(96889010406, 13))
        self.assertTrue(com.is_power(96889010407, 13))
        self.assertFalse(com.is_power(96889010408, 13))
        self.assertFalse(com.is_power(96889010407, 7))

    def test_is_prime(self):
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53}
        for n in range(2, 59):
            self.assertEqual(com.is_prime(n), n in primes)
        self.assertFalse(com.is_prime(993))
        self.assertFalse(com.is_prime(995))
        self.assertTrue(com.is_prime(997))
        self.assertFalse(com.is_prime(999))
        self.assertFalse(com.is_prime(10006719))
        self.assertTrue(com.is_prime(10006721))
        self.assertFalse(com.is_prime(10006723))
        self.assertFalse(com.is_prime(2097151))
        self.assertTrue(com.is_prime(2147483647))
        self.assertFalse(com.is_prime(4294967295))

    def test_is_square(self):
        squares = set([n**2 for n in range(1, 32)])
        for n in range(1, 1000):
            self.assertEqual(com.is_power(n, 2), n in squares)
        self.assertFalse(com.is_square(1769800759))
        self.assertFalse(com.is_square(1769800760))
        self.assertTrue(com.is_square(1769800761))
        self.assertFalse(com.is_square(1769800762))
        self.assertFalse(com.is_square(1769800763))

    def test_is_triangular(self):
        tri_nums = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120}
        for n in range(1, 125):
            self.assertEqual(com.is_triangular(n), n in tri_nums)
        self.assertFalse(com.is_triangular(884921413))
        self.assertFalse(com.is_triangular(884921414))
        self.assertTrue(com.is_triangular(884921415))
        self.assertFalse(com.is_triangular(884921416))
        self.assertFalse(com.is_triangular(884921417))

    def test_lcm(self):
        self.assertEqual(com.lcm(1, 1), 1)
        self.assertEqual(com.lcm(1, 2), 2)
        self.assertEqual(com.lcm(2, 1), 2)
        self.assertEqual(com.lcm(2, 3), 6)
        self.assertEqual(com.lcm(3, 2), 6)
        self.assertEqual(com.lcm(2, 4), 4)
        self.assertEqual(com.lcm(3, 4), 12)
        self.assertEqual(com.lcm(6, 4), 12)
        self.assertEqual(com.lcm(6, 21), 42)
        self.assertEqual(com.lcm(18, 12), 36)
        self.assertEqual(com.lcm(15, 35), 105)
        self.assertEqual(com.lcm(55250154, 21071889), 20608307442)

    def test_lcm_all(self):
        self.assertEqual(com.lcm_all([1]), 1)
        self.assertEqual(com.lcm_all((1, 1)), 1)
        self.assertEqual(com.lcm_all([1, 1, 1]), 1)
        self.assertEqual(com.lcm_all({1, 2}), 2)
        self.assertEqual(com.lcm_all([3, 4]), 12)
        self.assertEqual(com.lcm_all((35, 15)), 105)
        self.assertEqual(com.lcm_all([55250154, 21071889]), 20608307442)
        self.assertEqual(com.lcm_all([2, 1, 1]), 2)
        self.assertEqual(com.lcm_all(range(1, 4)), 6)
        self.assertEqual(com.lcm_all({2, 64, 8}), 64)
        self.assertEqual(com.lcm_all((8, 9, 7)), 504)
        self.assertEqual(com.lcm_all([4, 7, 2, 5, 3]), 420)
        self.assertEqual(
            com.lcm_all([540330, 424130, 465962, 357896]),
            4871660667720)

    def test_make_palindrome(self):
        self.assertEqual(com.make_palindrome(1), 11)
        self.assertEqual(com.make_palindrome(1, base=2), 0b11)
        self.assertEqual(com.make_palindrome(1, odd_length=True), 1)
        self.assertEqual(com.make_palindrome(1, base=2, odd_length=True), 1)
        self.assertEqual(com.make_palindrome(25), 2552)
        self.assertEqual(com.make_palindrome(0o31, base=8), 0o3113)
        self.assertEqual(com.make_palindrome(25, odd_length=True), 252)
        self.assertEqual(
            com.make_palindrome(0o31, base=8, odd_length=True),
            0o313)
        self.assertEqual(com.make_palindrome(1347), 13477431)
        self.assertEqual(com.make_palindrome(0x543, base=16), 0x543345)
        self.assertEqual(com.make_palindrome(1347, odd_length=True), 1347431)
        self.assertEqual(
            com.make_palindrome(0x543, base=16, odd_length=True),
            0x54345)

    def test_make_spiral(self):
        self.assertEqual(com.make_spiral(1), [[1]])
        self.assertEqual(
            com.make_spiral(2),
            [
                [7, 8, 9],
                [6, 1, 2],
                [5, 4, 3],
            ])
        self.assertEqual(
            com.make_spiral(3),
            [
                [21, 22, 23, 24, 25],
                [20,  7,  8,  9, 10],
                [19,  6,  1,  2, 11],
                [18,  5,  4,  3, 12],
                [17, 16, 15, 14, 13],
            ])
        self.assertEqual(
            com.make_spiral(4),
            [
                [43, 44, 45, 46, 47, 48, 49],
                [42, 21, 22, 23, 24, 25, 26],
                [41, 20,  7,  8,  9, 10, 27],
                [40, 19,  6,  1,  2, 11, 28],
                [39, 18,  5,  4,  3, 12, 29],
                [38, 17, 16, 15, 14, 13, 30],
                [37, 36, 35, 34, 33, 32, 31],
            ])
        self.assertEqual(
            com.make_spiral(5),
            [
                [73, 74, 75, 76, 77, 78, 79, 80, 81],
                [72, 43, 44, 45, 46, 47, 48, 49, 50],
                [71, 42, 21, 22, 23, 24, 25, 26, 51],
                [70, 41, 20,  7,  8,  9, 10, 27, 52],
                [69, 40, 19,  6,  1,  2, 11, 28, 53],
                [68, 39, 18,  5,  4,  3, 12, 29, 54],
                [67, 38, 17, 16, 15, 14, 13, 30, 55],
                [66, 37, 36, 35, 34, 33, 32, 31, 56],
                [65, 64, 63, 62, 61, 60, 59, 58, 57]
            ])

    def test_max_bipartite_matching(self):
        self.assertEqual(len(com.max_bipartite_matching([[False]])), 0)
        self.assertCountEqual(com.max_bipartite_matching([[True]]), [(0, 0)])
        self.assertCountEqual(
            com.max_bipartite_matching([
                [True, False],
                [False, True]]),
            [(0, 0), (1, 1)])
        self.assertEqual(
            len(com.max_bipartite_matching([
                [False, False],
                [True,  True]])),
            1)
        self.assertEqual(
            len(com.max_bipartite_matching([
                [False, True],
                [False, True]])),
            1)
        self.assertCountEqual(
            com.max_bipartite_matching([
                [False, True],
                [True,  True]]),
            [(0, 1), (1, 0)])
        self.assertCountEqual(
            com.max_bipartite_matching([
                [True,  False, False],
                [False, False, True],
                [False, True,  False]]),
            [(0, 0), (1, 2), (2, 1)])
        self.assertEqual(
            len(com.max_bipartite_matching([
                [True,  False, True, False, False],
                [False, False, True, False, False],
                [False, True,  True, True,  False],
                [False, False, True, False, False],
                [False, True,  True, False, True]])),
            4)
        self.assertCountEqual(
            com.max_bipartite_matching([
                [True,  False, False, False, False],
                [True,  False, True,  False, False],
                [False, True,  False, True,  False],
                [False, False, True,  False, True],
                [False, True,  False, False, True]]),
            [(0, 0), (1, 2), (2, 3), (3, 4), (4, 1)])
        self.assertEqual(
            len(com.max_bipartite_matching([
                [False, True,  True,  False, False, False],
                [True,  False, False, True,  False, False],
                [False, False, True,  False, False, False],
                [False, False, True,  True,  False, False],
                [False, False, False, False, False, False],
                [False, False, False, False, False, True]])),
            5)

    def test_max_triangle_path(self):
        self.assertEqual(com.max_triangle_path([[0]]), 0)
        self.assertEqual(com.max_triangle_path([[1]]), 1)
        self.assertEqual(com.max_triangle_path([[2]]), 2)
        self.assertEqual(com.max_triangle_path([[-5]]), -5)
        self.assertEqual(com.max_triangle_path([[1], [2, 3]]), 4)
        self.assertEqual(com.max_triangle_path([[1], [2, -3]]), 3)
        self.assertEqual(com.max_triangle_path([[1], [3, 2]]), 4)
        self.assertEqual(com.max_triangle_path([[1], [0, 2]]), 3)
        self.assertEqual(
            com.max_triangle_path([
                [3],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3]]),
            23)
        self.assertEqual(
            com.max_triangle_path([
                [-5],
                [-8, 69],
                [44, 46, -83],
                [7, 0, -47, 97],
                [-81, -64, -43, 13, -25],
                [21, 31, -30, 7, -28, 56]]),
            109)
        self.assertEqual(
            com.max_triangle_path([
                [72],
                [16, -188],
                [-348, -886, 702],
                [784, -522, 80, -453],
                [26, -850, 232, 444, 664],
                [-344, 80, -634, 0, -354, -736],
                [750, 0, -213, 343, 233, -955, -141],
                [349, -427, -492, -534, -450, -28, 498, -716],
                [589, -75, -428, 826, -180, 210, -36, -807, -874],
                [158, 509, 828, 45, -699, -33, 55, -242, -730, 634]]),
            2403)

    def test_minimum_line_cover(self):
        self.assertEqual(len(com.minimum_line_cover([[1]])), 0)
        self.assertEqual(len(com.minimum_line_cover([[0]])), 1)
        self.assertEqual(len(com.minimum_line_cover([[-1, 0]])), 1)
        self.assertCountEqual(com.minimum_line_cover([[0, 0]]), [(False, 0)])
        self.assertCountEqual(com.minimum_line_cover([[0], [0]]), [(True, 0)])
        self.assertCountEqual(
            com.minimum_line_cover([[0, 0, 0]]),
            [(False, 0)])
        self.assertCountEqual(
            com.minimum_line_cover([[0], [0], [0]]),
            [(True, 0)])
        self.assertEqual(len(com.minimum_line_cover([[0, 1], [2, 3]])), 1)
        self.assertEqual(len(com.minimum_line_cover([[5, 7], [4, 0]])), 1)
        self.assertCountEqual(
            com.minimum_line_cover([[0, 0], [-2, 6]]),
            [(False, 0)])
        self.assertCountEqual(
            com.minimum_line_cover([[-3, 0], [12, 0]]),
            [(True, 1)])
        self.assertEqual(len(com.minimum_line_cover([[8, 0], [0, 0]])), 2)
        self.assertCountEqual(
            com.minimum_line_cover([
                [1, 2, 0],
                [3, 4, 0],
                [0, 0, 0]]),
            [(False, 2), (True, 2)])
        self.assertEqual(
            len(com.minimum_line_cover([
                [0, 0, 0],
                [9, 2, 0],
                [4, 0, 6],
                [0, 3, 1]])),
            3)
        self.assertEqual(
            len(com.minimum_line_cover([
                [0, 4, 2, 2],
                [7, 6, 4, 0],
                [0, 5, 3, 5],
                [4, 3, 0, 0],
                [0, 0, 0, 0]])),
            4)
        self.assertEqual(
            len(com.minimum_line_cover([
                [0, 4, 2, 2, 3],
                [7, 6, 4, 0, 1],
                [0, 5, 3, 5, 7],
                [4, 3, 0, 0, 2],
                [0, 0, 0, 0, 0]])),
            4)
        self.assertEqual(
            len(com.minimum_line_cover([
                [0, 4, 2, 2, 3, 9],
                [7, 6, 4, 0, 1, -1],
                [0, 5, 3, 5, 7, 8],
                [4, 3, 0, 0, 2, 11],
                [0, 0, 0, 0, 0, 0]])),
            4)
        self.assertEqual(
            len(com.minimum_line_cover([
                [0, 3, 0, 2, 2],
                [7, 5, 4, 0, 0],
                [0, 4, 3, 5, 6],
                [4, 2, 0, 0, 1],
                [1, 0, 1, 1, 0]])),
            5)
        self.assertEqual(
            len(com.minimum_line_cover([
                [0, 1, 0, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 1, 0]])),
            4)
        self.assertCountEqual(
            com.minimum_line_cover([
                [0, 1, 0, 1, 1],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 0]]),
            [(True, 0), (True, 2), (True, 4)])
        self.assertEqual(
            len(com.minimum_line_cover([
                [5, 1, 2, 6, 7, 4, 3, 6, 4, 7],
                [2, 2, 0, 0, 1, 0, 3, 0, 4, 3],
                [6, 4, 2, 1, 1, 2, 0, 6, 6, 1],
                [4, 0, 2, 4, 4, 4, 4, 0, 2, 0],
                [2, 2, 4, 6, 2, 7, 1, 2, 5, 4],
                [3, 1, 4, 3, 2, 0, 6, 5, 5, 1],
                [2, 3, 6, 4, 0, 1, 6, 2, 2, 2],
                [1, 3, 1, 0, 0, 0, 1, 5, 1, 2]])),
            6)

    def test_mod_mutliply(self):
        self.assertEqual(com.mod_multiply(1, 1, 1), 0)
        self.assertEqual(com.mod_multiply(1, 2, 1), 0)
        self.assertEqual(com.mod_multiply(1, 2, 2), 0)
        self.assertEqual(com.mod_multiply(1, 2, 3), 2)
        self.assertEqual(com.mod_multiply(2, 1, 3), 2)
        self.assertEqual(com.mod_multiply(2, 3, 4), 2)
        self.assertEqual(com.mod_multiply(3, 3, 4), 1)
        self.assertEqual(com.mod_multiply(63, 52, 47), 33)
        self.assertEqual(com.mod_multiply(5052, 8658, 3010), 1906)
        self.assertEqual(com.mod_multiply(86**95, 64**28, 38**8), 261051428608)
        self.assertEqual(
            com.mod_multiply(8177**4018, 9470**1990, 27**29),
            24247430663168320345760575144348378592065)

    def test_next_multiple(self):
        self.assertEqual(com.next_multiple(1, 0), 0)
        self.assertEqual(com.next_multiple(1, 1), 1)
        self.assertEqual(com.next_multiple(1, 2), 2)
        self.assertEqual(com.next_multiple(2, 1), 2)
        self.assertEqual(com.next_multiple(2, 2), 2)
        self.assertEqual(com.next_multiple(2, 3), 4)
        self.assertEqual(com.next_multiple(3, 2), 3)
        self.assertEqual(com.next_multiple(7, 365), 371)
        self.assertEqual(com.next_multiple(365, 42), 365)
        self.assertEqual(com.next_multiple(73, 820), 876)
        self.assertEqual(com.next_multiple(264, 5133), 5280)
        self.assertEqual(com.next_multiple(6376, 913259), 918144)
        self.assertEqual(com.next_multiple(9448487, 589545477), 595254681)

    def test_optimal_assignment(self):
        self.assertCountEqual(com.optimal_assignment([[0]]), [(0, 0)])
        self.assertCountEqual(com.optimal_assignment([[1]]), [(0, 0)])
        self.assertCountEqual(com.optimal_assignment([[-2]]), [(0, 0)])
        self.assertCountEqual(
            com.optimal_assignment([[1, 2], [3, 5]]),
            [(0, 1), (1, 0)])
        self.assertCountEqual(
            com.optimal_assignment([[-1, -2], [-3, -5]]),
            [(0, 0), (1, 1)])
        self.assertCountEqual(
            com.optimal_assignment([[-1, 2], [-3, 4]]),
            [(0, 1), (1, 0)])
        self.assertCountEqual(
            com.optimal_assignment([
                [1, 6, 4],
                [8, 7, 9],
                [9, 0, 5]]),
            [(0, 0), (1, 2), (2, 1)])
        self.assertCountEqual(
            com.optimal_assignment([
                [52, 78, 91, 63, 14],
                [78, 45, 67, 43, 12],
                [85, 84, 43, 45, 36],
                [37, 60, 52, 54, 67],
                [48, 86, 23, 58, 99]]),
            [(0, 4), (1, 1), (2, 3), (3, 0), (4, 2)])
        self.assertCountEqual(
            com.optimal_assignment([
                [990, 621, 440, 679, 366, 961,  62, 609, 325, 188],
                [408, 172,  52,   0, 901, 168, 525, 705,  68,  25],
                [761, 187, 835, 508, 310, 216, 218, 351, 166, 263],
                [712,  78, 879, 530, 451, 564,   2,  49, 423, 394],
                [725, 558, 862, 243, 325, 509, 542, 448, 800, 760],
                [893, 341, 126, 547, 184, 199, 479, 282, 419, 508],
                [619, 297, 193, 182, 706, 558, 621, 393, 883, 922],
                [594, 192, 770, 523,  87, 295, 367, 744, 146, 700],
                [491, 386, 719,  14, 360, 673, 579, 413, 546, 427],
                [730, 392, 968, 587, 177, 291, 743,  63, 329, 717]]),
            [(0, 6), (1, 9), (2, 8), (3, 1), (4, 3), (5, 5), (6, 2), (7, 4),
             (8, 0), (9, 7)])

    def test_pandigital_string(self):
        self.assertEqual(com.pandigital_string(), '0123456789')
        self.assertEqual(com.pandigital_string(first=0), '0123456789')
        self.assertEqual(com.pandigital_string(first=3), '3456789')
        self.assertEqual(com.pandigital_string(first=9), '9')
        self.assertEqual(com.pandigital_string(last=0), '0')
        self.assertEqual(com.pandigital_string(last=4), '01234')
        self.assertEqual(com.pandigital_string(last=9), '0123456789')
        self.assertEqual(com.pandigital_string(first=0, last=9), '0123456789')
        self.assertEqual(com.pandigital_string(first=5, last=9), '56789')
        self.assertEqual(com.pandigital_string(first=0, last=8), '012345678')
        self.assertEqual(com.pandigital_string(first=2, last=6), '23456')

    def test_pentagonal(self):
        pent_nums = [0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247]
        for i, n in enumerate(pent_nums):
            self.assertEqual(com.pentagonal(i), n)
        self.assertEqual(com.pentagonal(53), 4187)
        self.assertEqual(com.pentagonal(8952), 120202980)

    def test_permute(self):
        self.assertEqual(com.permute(0, 0), 1)
        self.assertEqual(com.permute(0, 1), 0)
        self.assertEqual(com.permute(1, 0), 1)
        self.assertEqual(com.permute(1, 1), 1)
        self.assertEqual(com.permute(2, 0), 1)
        self.assertEqual(com.permute(2, 1), 2)
        self.assertEqual(com.permute(2, 2), 2)
        self.assertEqual(com.permute(2, 3), 0)
        self.assertEqual(com.permute(3, 0), 1)
        self.assertEqual(com.permute(3, 1), 3)
        self.assertEqual(com.permute(3, 2), 6)
        self.assertEqual(com.permute(3, 3), 6)
        self.assertEqual(com.permute(3, 4), 0)
        self.assertEqual(com.permute(4, 0), 1)
        self.assertEqual(com.permute(4, 1), 4)
        self.assertEqual(com.permute(4, 2), 12)
        self.assertEqual(com.permute(4, 3), 24)
        self.assertEqual(com.permute(4, 4), 24)
        self.assertEqual(com.permute(4, 5), 0)
        self.assertEqual(com.permute(12, 8), 19958400)
        self.assertEqual(com.permute(39, 11), 66902793897139200)
        self.assertEqual(
            com.permute(54, 37),
            649007187504351968469560171550257336096944816128000000000)

    def test_prime_factorization(self):
        self.assertEqual(com.prime_factorization(2), [[2, 1]])
        self.assertEqual(com.prime_factorization(3), [[3, 1]])
        self.assertEqual(com.prime_factorization(4), [[2, 2]])
        self.assertEqual(com.prime_factorization(5), [[5, 1]])
        self.assertEqual(com.prime_factorization(6), [[2, 1], [3, 1]])
        self.assertEqual(com.prime_factorization(12), [[2, 2], [3, 1]])
        self.assertEqual(com.prime_factorization(2903), [[2903, 1]])
        self.assertEqual(
            com.prime_factorization(61740),
            [[2, 2], [3, 2], [5, 1], [7, 3]])
        self.assertEqual(
            com.prime_factorization(4928693),
            [[7, 1], [11, 3], [23, 2]])
        self.assertEqual(
            com.prime_factorization(169165232),
            [[2, 4], [17, 1], [313, 1], [1987, 1]])
        self.assertEqual(
            com.prime_factorization(74435892358158),
            [[2, 1], [3, 3], [29, 1], [3049, 2], [5113, 1]])

    def test_prime(self):
        p_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
        for i, n in enumerate(p_nums):
            self.assertEqual(com.prime(i + 1), n)
        self.assertEqual(com.prime(74), 373)
        self.assertEqual(com.prime(225), 1427)
        self.assertEqual(com.prime(538), 3881)

    def test_primes(self):
        p_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
        for i in range(1, len(p_nums) + 1):
            self.assertCountEqual(com.primes(i), p_nums[:i])
        self.assertEqual(com.primes(168)[-1], 997)

    def test_primes_up_to(self):
        p_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97]
        for n in range(2, 100):
            self.assertCountEqual(
                com.primes_up_to(n),
                filter(lambda x: x <= n, p_nums))
        self.assertEqual(len(com.primes_up_to(1000)), 168)

    def test_quadratic_roots(self):
        roots = sorted(com.quadratic_roots(1, 0, -1))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -1)
        self.assertAlmostEqual(roots[1], 1)

        roots = sorted(com.quadratic_roots(1, -1, -1))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -0.61803399)
        self.assertAlmostEqual(roots[1], 1.61803399)

        roots = sorted(com.quadratic_roots(1, 3, -4))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -4)
        self.assertAlmostEqual(roots[1], 1)

        roots = sorted(com.quadratic_roots(2, 4, -4))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -2.7320508)
        self.assertAlmostEqual(roots[1], 0.7320508)

        roots = sorted(com.quadratic_roots(2, -4, -3))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -0.58113883)
        self.assertAlmostEqual(roots[1], 2.58113883)

        roots = sorted(com.quadratic_roots(-27, 643, -11))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 0.01711962)
        self.assertAlmostEqual(roots[1], 23.7976952)

        roots = sorted(com.quadratic_roots(1, 0, 1), key=(lambda x: x.imag))
        self.assertEqual(len(roots), 2)
        self.assertTrue(isinstance(roots[0], complex))
        self.assertTrue(isinstance(roots[1], complex))
        self.assertAlmostEqual(roots[0].real, 0)
        self.assertAlmostEqual(roots[0].imag, -1)
        self.assertAlmostEqual(roots[1].real, 0)
        self.assertAlmostEqual(roots[1].imag, 1)

        roots = sorted(com.quadratic_roots(24, 41, 35), key=(lambda x: x.imag))
        self.assertEqual(len(roots), 2)
        self.assertTrue(isinstance(roots[0], complex))
        self.assertTrue(isinstance(roots[1], complex))
        self.assertAlmostEqual(roots[0].real, -0.85416667)
        self.assertAlmostEqual(roots[0].imag, -0.85365839)
        self.assertAlmostEqual(roots[1].real, -0.85416667)
        self.assertAlmostEqual(roots[1].imag, 0.85365839)

    def test_radical(self):
        rads = [1, 2, 3, 2, 5, 6, 7, 2, 3, 10, 11, 6, 13, 14, 15, 2, 17, 6, 19]
        for i, n in enumerate(rads):
            self.assertEqual(com.radical(i + 1), n)
        self.assertEqual(com.radical(1391500), 2530)
        self.assertEqual(com.radical(21902926704), 73996374)

    def test_sqrt_decimal_expansion(self):
        self.assertEqual(com.sqrt_decimal_expansion(1, 0), '1.')
        self.assertEqual(com.sqrt_decimal_expansion(1, 1), '1.0')
        self.assertEqual(com.sqrt_decimal_expansion(1, 14), '1.00000000000000')
        self.assertEqual(com.sqrt_decimal_expansion(2, 0), '1.')
        self.assertEqual(com.sqrt_decimal_expansion(2, 1), '1.4')
        self.assertEqual(com.sqrt_decimal_expansion(2, 3), '1.414')
        self.assertEqual(com.sqrt_decimal_expansion(2, 14), '1.41421356237309')
        self.assertEqual(com.sqrt_decimal_expansion(64, 5), '8.00000')
        self.assertEqual(com.sqrt_decimal_expansion(152, 4), '12.3288')
        self.assertEqual(com.sqrt_decimal_expansion(2039, 6), '45.155287')
        self.assertEqual(
            com.sqrt_decimal_expansion(9734956, 53),
            '3120.08910129182048011564795491798243946307377557996188108')

    def test_sqrt_fraction_expansion(self):
        self.assertEqual(com.sqrt_fraction_expansion(2), (1, [2]))
        self.assertEqual(com.sqrt_fraction_expansion(3), (1, [1, 2]))
        self.assertEqual(com.sqrt_fraction_expansion(5), (2, [4]))
        self.assertEqual(com.sqrt_fraction_expansion(6), (2, [2, 4]))
        self.assertEqual(com.sqrt_fraction_expansion(7), (2, [1, 1, 1, 4]))
        self.assertEqual(com.sqrt_fraction_expansion(8), (2, [1, 4]))
        self.assertEqual(com.sqrt_fraction_expansion(10), (3, [6]))
        self.assertEqual(com.sqrt_fraction_expansion(11), (3, [3, 6]))
        self.assertEqual(com.sqrt_fraction_expansion(12), (3, [2, 6]))
        self.assertEqual(com.sqrt_fraction_expansion(13), (3, [1, 1, 1, 1, 6]))
        self.assertEqual(com.sqrt_fraction_expansion(23), (4, [1, 3, 1, 8]))
        self.assertEqual(
            com.sqrt_fraction_expansion(688),
            (26, [4, 2, 1, 5, 7, 3, 7, 5, 1, 2, 4, 52]))

    def test_sum_digits(self):
        self.assertEqual(com.sum_digits(1), 1)
        self.assertEqual(com.sum_digits(2), 2)
        self.assertEqual(com.sum_digits(10), 1)
        self.assertEqual(com.sum_digits(13), 4)
        self.assertEqual(com.sum_digits(209), 11)
        self.assertEqual(com.sum_digits(1337), 14)
        self.assertEqual(com.sum_digits(609278806205509), 67)
        self.assertEqual(
            com.sum_digits(9987223242228759440094102307791387034898),
            182)

    def test_sum_keep_digits(self):
        self.assertEqual(com.sum_keep_digits(1, 2), 3)
        self.assertEqual(com.sum_keep_digits(1, 2, d=1), 3)
        self.assertEqual(com.sum_keep_digits(1, 2, d=2), 3)
        self.assertEqual(com.sum_keep_digits(1, 2, d=100), 3)
        self.assertEqual(com.sum_keep_digits(7, 3), 10)
        self.assertEqual(com.sum_keep_digits(7, 3, d=1), 0)
        self.assertEqual(com.sum_keep_digits(7, 3, d=2), 10)
        self.assertEqual(com.sum_keep_digits(7, 3, d=3), 10)
        self.assertEqual(com.sum_keep_digits(80, 175), 255)
        self.assertEqual(com.sum_keep_digits(80, 175, d=1), 5)
        self.assertEqual(com.sum_keep_digits(80, 175, d=2), 55)
        self.assertEqual(com.sum_keep_digits(80, 175, d=3), 255)
        self.assertEqual(com.sum_keep_digits(80, 175, d=4), 255)
        self.assertEqual(com.sum_keep_digits(9008577767, 2942448238, d=1), 5)
        self.assertEqual(com.sum_keep_digits(9008577767, 2942448238, d=3), 5)
        self.assertEqual(
            com.sum_keep_digits(9008577767, 2942448238, d=6),
            26005)
        self.assertEqual(
            com.sum_keep_digits(9008577767, 2942448238, d=7),
            1026005)
        self.assertEqual(
            com.sum_keep_digits(9008577767, 2942448238, d=10),
            1951026005)
        self.assertEqual(
            com.sum_keep_digits(9008577767, 2942448238, d=11),
            11951026005)
        self.assertEqual(
            com.sum_keep_digits(9008577767, 2942448238, d=552),
            11951026005)
        self.assertEqual(
            com.sum_keep_digits(9008577767, 2942448238),
            11951026005)

    def test_sum_divisors(self):
        div_sums = [1, 3, 4, 7, 6, 12, 8, 15, 13, 18, 12, 28, 14, 24, 24, 31]
        for i, n in enumerate(div_sums):
            self.assertEqual(com.sum_divisors(i + 1), n)
        self.assertEqual(com.sum_divisors(892), 1568)
        self.assertEqual(com.sum_divisors(81468), 215488)
        self.assertEqual(com.sum_divisors(1485436710), 3774758112)

    def test_sum_of_squares(self):
        self.assertEqual(com.sum_of_squares(1), 1)
        self.assertEqual(com.sum_of_squares(2), 5)
        self.assertEqual(com.sum_of_squares(3), 14)
        self.assertEqual(com.sum_of_squares(4), 30)
        self.assertEqual(com.sum_of_squares(5), 55)
        self.assertEqual(com.sum_of_squares(6), 91)
        self.assertEqual(com.sum_of_squares(7), 140)
        self.assertEqual(com.sum_of_squares(401), 21574201)
        self.assertEqual(com.sum_of_squares(34594), 13800661997045)

    def test_sum_proper_divisors(self):
        div_sums = [0, 1, 1, 3, 1, 6, 1, 7, 4, 8, 1, 16, 1, 10, 9, 15, 1, 21]
        for i, n in enumerate(div_sums):
            self.assertEqual(com.sum_proper_divisors(i + 1), n)
        self.assertEqual(com.sum_proper_divisors(900), 1921)
        self.assertEqual(com.sum_proper_divisors(36582), 54810)
        self.assertEqual(com.sum_proper_divisors(9145116791), 203174473)

    def test_totient(self):
        tots = [1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8]
        for i, n in enumerate(tots):
            self.assertEqual(com.totient(i + 2), n)
        self.assertEqual(com.totient(2, prime_factors=[2]), 1)
        self.assertEqual(com.totient(3, prime_factors=[3]), 2)
        self.assertEqual(com.totient(4, prime_factors=[2]), 2)
        self.assertEqual(com.totient(5, prime_factors=[5]), 4)
        self.assertEqual(com.totient(6, prime_factors=[2, 3]), 2)
        self.assertEqual(com.totient(7, prime_factors=[7]), 6)
        self.assertEqual(com.totient(68), 32)
        self.assertEqual(com.totient(68, [2, 17]), 32)
        self.assertEqual(com.totient(876, prime_factors=[2, 3, 73]), 288)
        self.assertEqual(com.totient(876), 288)
        self.assertEqual(com.totient(58758), 16776)
        self.assertEqual(
            com.totient(58758, prime_factors=[2, 3, 7, 1399]),
            16776)
        self.assertEqual(
            com.totient(19614162799, prime_factors=[7, 11, 31, 24097]),
            14790124800)
        self.assertEqual(com.totient(19614162799), 14790124800)

    def test_totients_up_to(self):
        self.assertEqual(com.totients_up_to(2), [1])
        self.assertEqual(com.totients_up_to(3), [1, 2])
        self.assertEqual(com.totients_up_to(4), [1, 2, 2])
        self.assertEqual(com.totients_up_to(5), [1, 2, 2, 4])
        self.assertEqual(com.totients_up_to(6), [1, 2, 2, 4, 2])
        self.assertEqual(com.totients_up_to(7), [1, 2, 2, 4, 2, 6])
        self.assertEqual(
            com.totients_up_to(38),
            [1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12,
             10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18])

    def test_triangular(self):
        tri_nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        for i, n in enumerate(tri_nums):
            self.assertEqual(com.triangular(i + 1), n)
        self.assertEqual(com.triangular(292), 42778)
        self.assertEqual(com.triangular(38483), 740489886)
        self.assertEqual(com.triangular(4946666), 12234754731111)


# MAIN ########################################################################


if __name__ == '__main__':
    unittest.main()
