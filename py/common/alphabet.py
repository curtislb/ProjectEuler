#!/usr/bin/env python3

"""alphabet.py

Constants and functions relating to the English alphabet.
"""

__author__ = 'Curtis Belmonte'

from typing import Sequence


# Mapping from natural numbers to their English word equivalents
NUMBER_WORDS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def alpha_char_lower(index: int) -> str:
    """Returns the letter of the alphabet corresponding to index."""
    return chr(index + ord('a') - 1)


def alpha_index_upper(letter: str) -> int:
    """Returns the alphabetic index of the uppercase character letter."""
    return ord(letter) - ord('A') + 1


def letter_counts_upper(word: str) -> Sequence[int]:
    """Returns a sequence with the count of each uppercase letter in word."""
    letter_counts = [0] * 26
    for letter in word:
        letter_counts[alpha_index_upper(letter) - 1] += 1
    return letter_counts
