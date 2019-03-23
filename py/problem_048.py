#!/usr/bin/env python3

"""problem_048.py

Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last DIGIT_COUNT digits of the series, 1^1 + 2^2 + 3^3 + ... + MAX^MAX.
"""

__author__ = 'Curtis Belmonte'

import common.digits as digs


# PARAMETERS ##################################################################


DIGIT_COUNT = 10  # default: 10

MAX = 1000  # default: 1000


# SOLUTION ####################################################################


def solve() -> int:
    total = 0
    for n in range(1, MAX + 1):
        total = digs.sum_keep_digits(total, n**n, DIGIT_COUNT)
    return total


if __name__ == '__main__':
    print(solve())
