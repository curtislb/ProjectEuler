#!/usr/bin/env python3

"""test_alphabet.py



Author: Curtis Belmonte
"""

import unittest

from .context import alphabet as alpha


class TestWords(unittest.TestCase):
    def test_alpha_char_lower(self):
        self.assertEqual(alpha.alpha_char_lower(1), 'a')
        self.assertEqual(alpha.alpha_char_lower(9), 'i')
        self.assertEqual(alpha.alpha_char_lower(26), 'z')

    def test_alpha_index_upper(self):
        self.assertEqual(alpha.alpha_index_upper('A'), 1)
        self.assertEqual(alpha.alpha_index_upper('Q'), 17)
        self.assertEqual(alpha.alpha_index_upper('Z'), 26)


if __name__ == '__main__':
    unittest.main()
