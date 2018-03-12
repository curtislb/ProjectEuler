#!/usr/bin/env python3

"""problem_042.py

Problem 42: Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, t(n) = ½n(n+1);
so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value
is a triangle number then we shall call the word a triangle word.

Using FILE_NAME, a text file containing many common English words, how many
are triangle words?
"""

__author__ = 'Curtis Belmonte'

import common.alphabet as alpha
import common.fileio as fio
import common.sequences as seqs
from common.utility import memoized


# PARAMETERS ##################################################################


FILE_NAME = '../input/042.txt' # default: '../input/042.txt'


# SOLUTION ####################################################################


@memoized
def word_value(word: str) -> int:
    """Returns the sum of the alphabetical positions of each letter in word."""
    return (0 if word == '' else
            word_value(word[:-1]) + alpha.letter_index_upper(word[-1]))


def solve() -> int:
    # compute word values for all words in the input file
    word_values = [word_value(word) for word in
                   fio.strings_from_file(FILE_NAME)]
    max_word_value = max(word_values)
    
    # compute triangle numbers up to maximum word value
    triangle_nums = set()
    i = 0
    triangle_num = seqs.triangular(i)
    while triangle_num <= max_word_value:
        triangle_nums.add(triangle_num)
        i += 1
        triangle_num = seqs.triangular(i)
    
    # count the number of word values that are triangle numbers
    return sum((word_val in triangle_nums) for word_val in word_values)


if __name__ == '__main__':
    print(solve())
