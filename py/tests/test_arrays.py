#!/usr/bin/env python3

"""test_arrays.py

Unit test for the 'arrays' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.arrays as arrs


class TestArrays(unittest.TestCase):
    def test_argmax(self):
        self.assertEqual(arrs.argmax([[]]), 0)
        self.assertEqual(arrs.argmax('LOOOL'), 1)
        self.assertEqual(arrs.argmax(range(5)), 4)
        self.assertEqual(arrs.argmax([12, 34, 39, 5, 30]), 2)
        self.assertEqual(arrs.argmax([-1, 6, -8, 6, -8]), 1)

    def test_argmin(self):
        self.assertEqual(arrs.argmin([[]]), 0)
        self.assertEqual(arrs.argmin('LOOOL'), 0)
        self.assertEqual(arrs.argmin(range(5)), 0)
        self.assertEqual(arrs.argmin([12, 34, 39, 5, 30]), 3)
        self.assertEqual(arrs.argmin([-1, 6, -8, 6, -8]), 2)
        
    def test_binary_search(self):
        self.assertIsNone(arrs.binary_search([], 0))
        self.assertIsNone(arrs.binary_search([], 'x'))
        self.assertIsNone(arrs.binary_search([], None))

        self.assertIsNone(arrs.binary_search(['xy'], 'x'))
        self.assertEqual(arrs.binary_search(['xy'], 'xy'), 0)
        self.assertEqual(arrs.binary_search('xy', 'x'), 0)
        self.assertEqual(arrs.binary_search('xy', 'y'), 1)
        self.assertIsNone(arrs.binary_search('xy', 'z'))

        seq = [[0],  [0, 1], [1, 0], [1, 1, 0]]
        self.assertEqual(arrs.binary_search(seq, [1, 0]), 2)
        self.assertIsNone(arrs.binary_search(seq, [0, 0]))
        self.assertIsNone(arrs.binary_search(seq, []))

        seq = [0, 5, 5, 13, 19, 22, 41, 55, 68, 68, 72, 81, 98]
        self.assertEqual(arrs.binary_search(seq, 55), 7)
        self.assertIn(arrs.binary_search(seq, 5), [1, 2])
        self.assertEqual(arrs.binary_search(seq, 0), 0)
        self.assertEqual(arrs.binary_search(seq, 98), 12)
        self.assertIsNone(arrs.binary_search(seq, 23))
        
    def test_cumulative_partial_sum(self):
        self.assertEqual(arrs.cumulative_partial_sum([1]), [1])
        self.assertEqual(arrs.cumulative_partial_sum([1, 2, 3]), [1, 3, 6])
        self.assertEqual(arrs.cumulative_partial_sum([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(arrs.cumulative_partial_sum([1, 2, 3], 2), [1, 3, 5])
        self.assertEqual(arrs.cumulative_partial_sum([-1, 2, -3]), [-1, 1, -2])
        self.assertEqual(
            arrs.cumulative_partial_sum(
                [9, -7, -1, 18, 25, -6, 14, -20, 0, 4, -18, 12, -3, 11, 6, -5],
                8),
            [9, 2, 1, 19, 44, 38, 52, 32, 23, 34, 17, 11, -17, 0, -8, 7])
        
    def test_inverse_index_map(self):
        self.assertEqual(arrs.inverse_index_map([]), {})
        self.assertEqual(arrs.inverse_index_map([2]), {2: 0})
        self.assertEqual(arrs.inverse_index_map('a'), {'a': 0})
        self.assertEqual(arrs.inverse_index_map((3, 2, 1)), {3: 0, 2: 1, 1: 2})
        self.assertEqual(
            arrs.inverse_index_map('XYZ'), {'X': 0, 'Y': 1, 'Z': 2})
        self.assertEqual(
            arrs.inverse_index_map('randomz'),
            {'r': 0, 'a': 1, 'n': 2, 'd': 3, 'o': 4, 'm': 5, 'z': 6})

    def test_inverse_index_map_nd(self):
        self.assertEqual(arrs.inverse_index_map_nd(''), {})
        self.assertEqual(arrs.inverse_index_map_nd('z'), {'z': [0]})
        self.assertEqual(arrs.inverse_index_map_nd([1]), {1: [0]})
        self.assertEqual(arrs.inverse_index_map_nd([3, 3]), {3: [0, 1]})
        self.assertEqual(
            arrs.inverse_index_map_nd('ABBA'), {'A': [0, 3], 'B': [1, 2]})
        self.assertEqual(
            arrs.inverse_index_map_nd((1, 6, 1, 8, 0, 3, 3, 9, 8, 8)),
            {0: [4], 1: [0, 2], 3: [5, 6], 6: [1], 8: [3, 8, 9], 9: [7]})
        
    def test_is_permutation(self):
        for cmp in (False, True):
            self.assertTrue(arrs.is_permutation([], set(), cmp))
            self.assertTrue(arrs.is_permutation('', iter([]), cmp))
            self.assertTrue(arrs.is_permutation(iter(()), range(0), cmp))
            self.assertFalse(arrs.is_permutation([1], (), cmp))
            self.assertFalse(arrs.is_permutation([], (2, 3), cmp))
            self.assertFalse(arrs.is_permutation([2], (2, 3), cmp))
            self.assertTrue(arrs.is_permutation({1}, [1], cmp))
            self.assertFalse(arrs.is_permutation([1], [2], cmp))
            self.assertTrue(arrs.is_permutation('12', '21', cmp))
            self.assertTrue(arrs.is_permutation('12', ['2', '1'], cmp))
            self.assertFalse(arrs.is_permutation('12', [1, 2], cmp))
            self.assertTrue(arrs.is_permutation((1, 4, 7), {7, 1, 4}, cmp))
            self.assertTrue(arrs.is_permutation('silent', 'listen', cmp))
            self.assertFalse(arrs.is_permutation('listen', 'tiles', cmp))
            self.assertTrue(
                arrs.is_permutation(
                    [37, 86, 19, 0, 4, 19, 655, 101, 4, 19],
                    [4, 37, 101, 4, 19, 86, 19, 655, 19, 0],
                    cmp))
            self.assertFalse(
                arrs.is_permutation(
                    [37, 86, 19, 0, 4, 655, 101, 4],
                    [4, 37, 101, 19, 86, 19, 655, 19, 0],
                    cmp))
            self.assertTrue(
                arrs.is_permutation(
                    iter([37, 86, 19, 0, 4, 19, 655, 101, 4, 19]),
                    iter([4, 37, 101, 4, 19, 86, 19, 655, 19, 0]),
                    cmp))
            self.assertFalse(
                arrs.is_permutation(
                    iter((37, 86, 19, 0, 4, 655, 101, 4)),
                    iter((4, 37, 101, 19, 86, 19, 655, 19, 0)),
                    cmp))


if __name__ == '__main__':
    unittest.main()
