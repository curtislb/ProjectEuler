#!/usr/bin/env python3

"""test_expansion.py

Unit test for the 'expansion' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.expansion as expan


class TestExpansion(unittest.TestCase):
    def test_sqrt_decimal_expansion(self) -> None:
        self.assertEqual(expan.sqrt_decimal_expansion(1, 0), '1.')
        self.assertEqual(expan.sqrt_decimal_expansion(1, 1), '1.0')
        self.assertEqual(expan.sqrt_decimal_expansion(1, 12), '1.000000000000')
        self.assertEqual(expan.sqrt_decimal_expansion(2, 0), '1.')
        self.assertEqual(expan.sqrt_decimal_expansion(2, 1), '1.4')
        self.assertEqual(expan.sqrt_decimal_expansion(2, 3), '1.414')
        self.assertEqual(expan.sqrt_decimal_expansion(2, 12), '1.414213562373')
        self.assertEqual(expan.sqrt_decimal_expansion(64, 5), '8.00000')
        self.assertEqual(expan.sqrt_decimal_expansion(152, 4), '12.3288')
        self.assertEqual(expan.sqrt_decimal_expansion(2039, 6), '45.155287')
        self.assertEqual(
            expan.sqrt_decimal_expansion(9734956, 53),
            '3120.08910129182048011564795491798243946307377557996188108')

    def test_sqrt_fraction_expansion(self) -> None:
        self.assertEqual(expan.sqrt_fraction_expansion(2), (1, [2]))
        self.assertEqual(expan.sqrt_fraction_expansion(3), (1, [1, 2]))
        self.assertEqual(expan.sqrt_fraction_expansion(5), (2, [4]))
        self.assertEqual(expan.sqrt_fraction_expansion(6), (2, [2, 4]))
        self.assertEqual(expan.sqrt_fraction_expansion(7), (2, [1, 1, 1, 4]))
        self.assertEqual(expan.sqrt_fraction_expansion(8), (2, [1, 4]))
        self.assertEqual(expan.sqrt_fraction_expansion(10), (3, [6]))
        self.assertEqual(expan.sqrt_fraction_expansion(11), (3, [3, 6]))
        self.assertEqual(expan.sqrt_fraction_expansion(12), (3, [2, 6]))
        self.assertEqual(
            expan.sqrt_fraction_expansion(13), (3, [1, 1, 1, 1, 6]))
        self.assertEqual(
            expan.sqrt_fraction_expansion(23), (4, [1, 3, 1, 8]))
        self.assertEqual(
            expan.sqrt_fraction_expansion(688),
            (26, [4, 2, 1, 5, 7, 3, 7, 5, 1, 2, 4, 52]))


if __name__ == '__main__':
    unittest.main()
