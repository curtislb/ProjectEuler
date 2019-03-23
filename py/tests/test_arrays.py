#!/usr/bin/env python3

"""test_arrays.py

Unit test for the 'arrays' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest
from typing import Iterator, List, Sequence

import common.arrays as arrs


class TestArrays(unittest.TestCase):
    def test_argmax(self) -> None:
        self.assertEqual(arrs.argmax([[]]), 0)
        self.assertEqual(arrs.argmax('LOOOL'), 1)
        self.assertEqual(arrs.argmax(range(5)), 4)
        self.assertEqual(arrs.argmax([12, 34, 39, 5, 30]), 2)
        self.assertEqual(arrs.argmax([-1, 6, -8, 6, -8]), 1)

    def test_argmin(self) -> None:
        self.assertEqual(arrs.argmin([[]]), 0)
        self.assertEqual(arrs.argmin('LOOOL'), 0)
        self.assertEqual(arrs.argmin(range(5)), 0)
        self.assertEqual(arrs.argmin([12, 34, 39, 5, 30]), 3)
        self.assertEqual(arrs.argmin([-1, 6, -8, 6, -8]), 2)
        
    def test_binary_search(self) -> None:
        self.assertIsNone(arrs.binary_search([], 0))
        self.assertIsNone(arrs.binary_search([], 'x'))
        self.assertIsNone(arrs.binary_search([], None))

        self.assertIsNone(arrs.binary_search(['xy'], 'x'))
        self.assertEqual(arrs.binary_search(['xy'], 'xy'), 0)
        self.assertEqual(arrs.binary_search('xy', 'x'), 0)
        self.assertEqual(arrs.binary_search('xy', 'y'), 1)
        self.assertIsNone(arrs.binary_search('xy', 'z'))

        seq1 = [[0],  [0, 1], [1, 0], [1, 1, 0]]
        self.assertEqual(arrs.binary_search(seq1, [1, 0]), 2)
        self.assertIsNone(arrs.binary_search(seq1, [0, 0]))
        self.assertIsNone(arrs.binary_search(seq1, []))

        seq2 = [0, 5, 5, 13, 19, 22, 41, 55, 68, 68, 72, 81, 98]
        self.assertEqual(arrs.binary_search(seq2, 55), 7)
        self.assertIn(arrs.binary_search(seq2, 5), [1, 2])
        self.assertEqual(arrs.binary_search(seq2, 0), 0)
        self.assertEqual(arrs.binary_search(seq2, 98), 12)
        self.assertIsNone(arrs.binary_search(seq2, 23))
        
    def test_cumulative_partial_sums(self) -> None:
        self.assertEqual(arrs.cumulative_partial_sums([1], 1), [1])
        self.assertEqual(arrs.cumulative_partial_sums([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(arrs.cumulative_partial_sums([1, 2, 3], 2), [1, 3, 5])
        self.assertEqual(arrs.cumulative_partial_sums([1, 2, 3], 3), [1, 3, 6])
        self.assertEqual(
            arrs.cumulative_partial_sums([-1, 2, -3], 3), [-1, 1, -2])
        self.assertEqual(
            arrs.cumulative_partial_sums(
                [9, -7, -1, 18, 25, -6, 14, -20, 0, 4, -18, 12, -3, 11, 6, -5],
                8),
            [9, 2, 1, 19, 44, 38, 52, 32, 23, 34, 17, 11, -17, 0, -8, 7])

    def test_cumulative_products(self) -> None:
        self.assertEqual(arrs.cumulative_products([1]), [1])
        self.assertEqual(arrs.cumulative_products([1, 1]), [1, 1])
        self.assertEqual(arrs.cumulative_products([1, 2]), [1, 2])
        self.assertEqual(arrs.cumulative_products([2, 1]), [2, 2])
        self.assertEqual(arrs.cumulative_products([1, 2, 3]), [1, 2, 6])
        self.assertEqual(arrs.cumulative_products([3, 2, 1]), [3, 6, 6])
        self.assertEqual(arrs.cumulative_products([-1, 2, -3]), [-1, -2, 6])
        self.assertEqual(
            arrs.cumulative_products([2, 3, 5, 7, 11, 13, 17]),
            [2, 6, 30, 210, 2310, 30030, 510510])
        self.assertEqual(
            arrs.cumulative_products(
                [9, -7, -1, 18, 25, -6, 14, -20, 1, 4, -18, 12, -3, 11]),
            [9, -63, 63, 1134, 28350, -170100, -2381400, 47628000, 47628000,
             190512000, -3429216000, -41150592000, 123451776000, 1357969536000])
        
    def test_inverse_index_map(self) -> None:
        self.assertEqual(arrs.inverse_index_map([]), {})
        self.assertEqual(arrs.inverse_index_map([2]), {2: 0})
        self.assertEqual(arrs.inverse_index_map('a'), {'a': 0})
        self.assertEqual(arrs.inverse_index_map((3, 2, 1)), {3: 0, 2: 1, 1: 2})
        self.assertEqual(
            arrs.inverse_index_map('XYZ'), {'X': 0, 'Y': 1, 'Z': 2})
        self.assertEqual(
            arrs.inverse_index_map('randomz'),
            {'r': 0, 'a': 1, 'n': 2, 'd': 3, 'o': 4, 'm': 5, 'z': 6})

    def test_inverse_index_map_all(self) -> None:
        self.assertEqual(arrs.inverse_index_map_all(''), {})
        self.assertEqual(arrs.inverse_index_map_all('z'), {'z': [0]})
        self.assertEqual(arrs.inverse_index_map_all([1]), {1: [0]})
        self.assertEqual(arrs.inverse_index_map_all([3, 3]), {3: [0, 1]})
        self.assertEqual(
            arrs.inverse_index_map_all('ABBA'), {'A': [0, 3], 'B': [1, 2]})
        self.assertEqual(
            arrs.inverse_index_map_all((1, 6, 1, 8, 0, 3, 3, 9, 8, 8)),
            {0: [4], 1: [0, 2], 3: [5, 6], 6: [1], 8: [3, 8, 9], 9: [7]})
        
    def test_is_permutation(self) -> None:
        for cmp in (False, True):
            empty_str_iter: Iterator[str] = iter([])
            empty_int_iter: Iterator[int] = iter(())
            empty_int_list: List[int] = []
            empty_int_tupl: Sequence[int] = ()
            self.assertTrue(arrs.is_permutation([], set(), cmp))
            self.assertTrue(arrs.is_permutation('', empty_str_iter, cmp))
            self.assertTrue(arrs.is_permutation(empty_int_iter, range(0), cmp))
            self.assertFalse(arrs.is_permutation([1], empty_int_tupl, cmp))
            self.assertFalse(arrs.is_permutation(empty_int_list, (2, 3), cmp))
            self.assertFalse(arrs.is_permutation([2], (2, 3), cmp))
            self.assertTrue(arrs.is_permutation({1}, [1], cmp))
            self.assertFalse(arrs.is_permutation([1], [2], cmp))
            self.assertTrue(arrs.is_permutation('12', '21', cmp))
            self.assertTrue(arrs.is_permutation('12', ['2', '1'], cmp))
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
