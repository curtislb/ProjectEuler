#!/usr/bin/env python3

"""test_probability.py

Unit test for the 'probability' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest
from fractions import Fraction

import common.probability as prob


class MyTestCase(unittest.TestCase):
    def test_dice_probability(self) -> None:
        self.assertEqual(prob.dice_probability(1, 1, 1), 1)
        self.assertEqual(prob.dice_probability(0, 1, 1), 0)
        self.assertEqual(prob.dice_probability(2, 1, 1), 0)
        self.assertEqual(prob.dice_probability(1, 1, 6), Fraction(1, 6))
        self.assertEqual(prob.dice_probability(6, 1, 6), Fraction(1, 6))
        self.assertEqual(prob.dice_probability(7, 1, 6), 0)
        self.assertEqual(prob.dice_probability(2, 2, 6), Fraction(1, 36))
        self.assertEqual(prob.dice_probability(7, 2, 6), Fraction(1, 6))
        self.assertEqual(prob.dice_probability(18, 5, 7), Fraction(190, 2401))


if __name__ == '__main__':
    unittest.main()
