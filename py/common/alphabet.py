#!/usr/bin/env python3

"""Common library for working with the English alphabet.

This module provides constants and functions related to the English alphabet.
Examples include counting the occurrences of letters in a word and converting
between letters and their alphabetic indices.
"""

from typing import Mapping, Sequence


#: Mapping from positive integers to their English word equivalents.
NUMBER_WORDS: Mapping[int, str] = {
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


def letter_char_lower(index: int) -> str:
    """Gives the lowercase letter of the alphabet corresponding to ``index``.

    Args:
        index: An alphabetic index, from 1 to 26.

    Returns:
        A lowercase letter, from 'a' to 'z'.
    """
    return chr(index + ord('a') - 1)


def letter_counts_upper(word: str) -> Sequence[int]:
    """Counts the occurrence of each uppercase letter in ``word``.

    Args:
        word: A string consisting of uppercase letters from 'A' to 'Z'.

    Returns:
        An integer sequence of length 26, whose entries represent the count of
        each letter (from 'A' to 'Z', in order) in ``word``.
    """
    letter_counts = [0] * 26
    for letter in word:
        letter_counts[letter_index_upper(letter) - 1] += 1
    return letter_counts


def letter_index_upper(letter: str) -> int:
    """Gives the alphabetic index corresponding to an uppercase letter.

    Args:
        letter: An uppercase letter, from 'A' to 'Z'.

    Returns:
        An alphabetic index, from 1 to 26.
    """
    return ord(letter) - ord('A') + 1
