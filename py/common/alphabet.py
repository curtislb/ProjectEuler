#!/usr/bin/env python3

"""words.py



Author: Curtis Belmonte
"""


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


def alpha_char_lower(index):
    """Returns the letter of the alphabet corresponding to index."""
    return chr(index + ord('a') - 1)


def alpha_index_upper(letter):
    """Returns the alphabetic index of the uppercase character letter."""
    return ord(letter) - ord('A') + 1
