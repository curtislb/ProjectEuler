#!/usr/bin/env python3

"""problem_076.py

Problem 76: Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can N be written as a sum of at least two positive
integers?
"""

__author__ = 'Curtis Belmonte'

import common.combinatorics as comb


# PARAMETERS ##################################################################


N = 100  # default: 100


# SOLUTION ####################################################################


def solve() -> int:
    return comb.combination_sums(N, list(range(1, N)))


if __name__ == '__main__':
    print(solve())
