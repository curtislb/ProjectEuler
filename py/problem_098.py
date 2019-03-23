#!/usr/bin/env python3

"""problem_098.py

Problem 98: Anagramic squares

By replacing each of the letters in the word CARE with 1, 2, 9, and 6
respectively, we form a square number: 1296 = 36^2. What is remarkable is that,
by using the same digital substitutions, the anagram, RACE, also forms a square
number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair
and specify further that leading zeroes are not permitted, neither may a
different letter have the same digital value as another letter.

Using FILE_NAME, a text file containing nearly two-thousand common English
words, find all the square anagram word pairs (a palindromic word is NOT
considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""

__author__ = 'Curtis Belmonte'

import math
from collections import defaultdict
from typing import Dict, List, Mapping, Optional, Sequence

import common.alphabet as alpha
import common.digits as digs
import common.fileio as fio
import common.sequences as seqs


# PARAMETERS ##################################################################


FILE_NAME = '../input/098.txt'  # default: '../input/098.txt'


# SOLUTION ####################################################################


def first_len(words: List[str]) -> int:
    """Returns the length of the first word in words."""
    return len(words[0])


def try_map_digits(digits: Sequence[int], word: str)\
        -> Optional[Mapping[str, int]]:

    """Tries to find a valid mapping between digits and the letters in word.

    Specifically, tries to return a dict mapping each unique letter in word to
    the digit that should replace it in order to form the decimal number
    represented by digits. A valid mapping must also not map any two distinct
    letters to the same digit.

    If no such mapping exists for digits and words, instead returns None.
    """

    mapping: Dict[str, int] = {}
    is_used = [False] * 10
    for i, letter in enumerate(word):
        if letter not in mapping:
            if is_used[digits[i]]:
                # invalid mapping: two letters mapped to same digit
                return None
            else:
                # map current letter to corresponding digit
                is_used[digits[i]] = True
                mapping[letter] = digits[i]
        elif mapping[letter] != digits[i]:
            # invalid mapping: letter mapped to two distinct digits
            return None
    return mapping


def is_square_mapping(digit_map: Mapping[str, int], word: str) -> bool:
    """Checks if digit_map maps the letters in word into a perfect square."""
    mapped_digits = [digit_map[letter] for letter in word]
    return (mapped_digits[0] != 0 and
            seqs.is_square(digs.concat_digits(mapped_digits)))


def max_anagramic_square(word1: str, word2: str) -> int:
    """Returns the maximum anagramic square formed by the pair word1, word2.

    Specifically, searches for all pairs of square numbers that can be formed
    by mapping the letters in anagrams word1 and word2 to the same digits and
    returns the maximum square number across all such pairs.

    If no such pair of squares exists for word1 and word2, instead returns 0.
    """

    # check all possible squares in decreasing order
    word_len = len(word1)
    upper_root = int(math.sqrt(10**word_len - 1))
    lower_root = int(math.ceil(math.sqrt(10**(word_len - 1))))
    for root in range(upper_root, lower_root - 1, -1):
        square = root**2
        square_digits = digs.digits(square)

        # try mapping square digits directly to word1
        digit_mapping = try_map_digits(square_digits, word1)
        if digit_mapping is not None:
            if is_square_mapping(digit_mapping, word2):
                return square

        # try mapping square digits directly to word2
        digit_mapping = try_map_digits(square_digits, word2)
        if digit_mapping is not None:
            if is_square_mapping(digit_mapping, word1):
                return square

    # no anagramic square pairs found
    return 0


def solve() -> int:
    # parse words from input file into anagramic groups
    counts_to_words: Dict[Sequence[int], List[str]] = defaultdict(list)
    for word in fio.strings_from_file(FILE_NAME):
        letter_counts = tuple(alpha.letter_counts_upper(word))
        counts_to_words[letter_counts].append(word)

    # sort anagramic word groups in decreasing order of word length
    word_lists = sorted(counts_to_words.values(), key=first_len, reverse=True)

    # check all anagram pairs for anagramic square numbers
    max_square = 0
    max_digits = 0
    for words in word_lists:
        word_count = len(words)
        # ignore words with no anagram and ones too short to yield max square
        if word_count > 1 and first_len(words) >= max_digits:
            for i in range(word_count - 1):
                for j in range(i + 1, word_count):
                    # find max anagramic square for given word pair
                    square = max_anagramic_square(words[i], words[j])
                    if square > max_square:
                        max_square = square
                        max_digits = digs.count_digits(square)

    return max_square


if __name__ == '__main__':
    print(solve())
