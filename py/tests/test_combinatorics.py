#!/usr/bin/env python3

"""test_combinatorics.py

Unit test for the 'combinatorics' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.combinatorics as comb


class TestCombinatorics(unittest.TestCase):
    def test_choose(self) -> None:
        self.assertEqual(comb.choose(0, 0), 1)
        self.assertEqual(comb.choose(1, 0), 1)
        self.assertEqual(comb.choose(1, 1), 1)
        self.assertEqual(comb.choose(2, 0), 1)
        self.assertEqual(comb.choose(2, 1), 2)
        self.assertEqual(comb.choose(2, 2), 1)
        self.assertEqual(comb.choose(3, 0), 1)
        self.assertEqual(comb.choose(3, 1), 3)
        self.assertEqual(comb.choose(3, 2), 3)
        self.assertEqual(comb.choose(3, 3), 1)
        self.assertEqual(comb.choose(4, 0), 1)
        self.assertEqual(comb.choose(4, 1), 4)
        self.assertEqual(comb.choose(4, 2), 6)
        self.assertEqual(comb.choose(4, 3), 4)
        self.assertEqual(comb.choose(4, 4), 1)
        self.assertEqual(comb.choose(12, 5), 792)
        self.assertEqual(comb.choose(84, 26), 3496176570135581124912)
        self.assertEqual(
            comb.choose(309, 254),
            41885714195904323564014555767112516232542200976007970465503616)
    
    def test_combination_sums(self) -> None:
        with self.assertRaises(ValueError):
            comb.combination_sums(1, [1, 0, 2])
        with self.assertRaises(ValueError):
            comb.combination_sums(2, [1, 2, -1])
        with self.assertRaises(ValueError):
            comb.combination_sums(0, [1])
        with self.assertRaises(ValueError):
            comb.combination_sums(-1, [1])
        with self.assertRaises(ValueError):
            comb.combination_sums(-1, [-1])

        self.assertEqual(comb.combination_sums(1, []), 0)
        self.assertEqual(comb.combination_sums(1, [1]), 1)
        self.assertEqual(comb.combination_sums(1, [1, 2]), 1)
        self.assertEqual(comb.combination_sums(1, [2, 1]), 1)
        self.assertEqual(comb.combination_sums(2, [1, 2]), 2)
        self.assertEqual(comb.combination_sums(2, [1, 1]), 3)
        self.assertEqual(comb.combination_sums(3, [1, 2]), 2)
        self.assertEqual(comb.combination_sums(3, [3, 1, 2]), 3)
        self.assertEqual(comb.combination_sums(100, [1, 5, 10, 25, 50]), 292)
        self.assertEqual(comb.combination_sums(100, (25, 50, 10, 1, 5)), 292)
        self.assertEqual(
            comb.combination_sums(500, [1, 5, 10, 25, 50, 100, 200, 500]),
            111023)
        
    def test_factorial(self) -> None:
        self.assertEqual(comb.factorial(0), 1)
        self.assertEqual(comb.factorial(1), 1)
        self.assertEqual(comb.factorial(2), 2)
        self.assertEqual(comb.factorial(3), 6)
        self.assertEqual(comb.factorial(4), 24)
        self.assertEqual(comb.factorial(13), 6227020800)
        self.assertEqual(
            comb.factorial(45),
            119622220865480194561963161495657715064383733760000000000)
        
    def test_permute(self) -> None:
        self.assertEqual(comb.permute(0, 0), 1)
        self.assertEqual(comb.permute(0, 1), 0)
        self.assertEqual(comb.permute(1, 0), 1)
        self.assertEqual(comb.permute(1, 1), 1)
        self.assertEqual(comb.permute(2, 0), 1)
        self.assertEqual(comb.permute(2, 1), 2)
        self.assertEqual(comb.permute(2, 2), 2)
        self.assertEqual(comb.permute(2, 3), 0)
        self.assertEqual(comb.permute(3, 0), 1)
        self.assertEqual(comb.permute(3, 1), 3)
        self.assertEqual(comb.permute(3, 2), 6)
        self.assertEqual(comb.permute(3, 3), 6)
        self.assertEqual(comb.permute(3, 4), 0)
        self.assertEqual(comb.permute(4, 0), 1)
        self.assertEqual(comb.permute(4, 1), 4)
        self.assertEqual(comb.permute(4, 2), 12)
        self.assertEqual(comb.permute(4, 3), 24)
        self.assertEqual(comb.permute(4, 4), 24)
        self.assertEqual(comb.permute(4, 5), 0)
        self.assertEqual(comb.permute(12, 8), 19958400)
        self.assertEqual(comb.permute(39, 11), 66902793897139200)
        self.assertEqual(
            comb.permute(54, 37),
            649007187504351968469560171550257336096944816128000000000)


if __name__ == '__main__':
    unittest.main()
