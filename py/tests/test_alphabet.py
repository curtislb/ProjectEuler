#!/usr/bin/env python3

"""test_alphabet.py

Unit test for the 'alphabet' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.alphabet as alpha


class TestAlphabet(unittest.TestCase):
    def test_letter_char_lower(self) -> None:
        self.assertEqual(alpha.letter_char_lower(1), 'a')
        self.assertEqual(alpha.letter_char_lower(9), 'i')
        self.assertEqual(alpha.letter_char_lower(26), 'z')

    def test_letter_counts_upper(self) -> None:
        self.assertEqual(
            alpha.letter_counts_upper('A'), [1] + ([0] * 25))
        self.assertEqual(
            alpha.letter_counts_upper('YXXZ'), ([0] * 23) + [2, 1, 1])
        self.assertEqual(
            alpha.letter_counts_upper('GOOGOLPLEX'),
            [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0,
             0, 1, 0, 0])
        self.assertEqual(
            alpha.letter_counts_upper('AQUICKBROWNFOXJUMPSOVERTHELAZYDOG'),
            [2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 2, 1, 1, 2, 1,
             1, 1, 1, 1])

    def test_letter_index_upper(self) -> None:
        self.assertEqual(alpha.letter_index_upper('Z'), 26)
        self.assertEqual(alpha.letter_index_upper('A'), 1)
        self.assertEqual(alpha.letter_index_upper('Q'), 17)


if __name__ == '__main__':
    unittest.main()
