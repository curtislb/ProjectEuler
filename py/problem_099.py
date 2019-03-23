#!/usr/bin/env python3

"""problem_099.py

Problem 99: Largest exponential

Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using FILE_NAME, a text file containing lines with a base/exponent pair on
each line, determine which line number has the greatest numerical value.
"""

__author__ = 'Curtis Belmonte'

import math

import common.fileio as fio


# PARAMETERS ##################################################################


FILE_NAME = '../input/099.txt'  # default: '../input/099.txt'


# SOLUTION ####################################################################


def solve() -> int:
    max_line = None
    max_value = -float('inf')
    base_exp_pairs = fio.ints_from_file(FILE_NAME, sep=',')

    # compare exponent * log(base) for all pairs
    for i, pair in enumerate(base_exp_pairs):
        base, exponent = pair
        value = exponent * math.log(base)
        if value > max_value:
            max_line = i
            max_value = value

    return max_line + 1


if __name__ == '__main__':
    print(solve())
