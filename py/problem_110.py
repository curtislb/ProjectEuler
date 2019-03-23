#!/usr/bin/env python3

"""problem_110.py

Problem 110: Diophantine reciprocals II

In the following equation x, y, and n are positive integers.

    1/x + 1/y = 1/n

It can be verified that when n = 1260 there are 113 distinct solutions and this
is the least value of n for which the total number of distinct solutions
exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds
MIN_SOLUTIONS?

NOTE: This problem is a much more difficult version of Problem 108 and as it is
well beyond the limitations of a brute force approach it requires a clever
implementation.
"""

__author__ = 'Curtis Belmonte'

import problem_108 as p108


# PARAMETERS ##################################################################


MIN_SOLUTIONS = 4000000  # default: 4000000


# SOLUTION ####################################################################


def solve() -> int:
    return p108.find_min_denom(MIN_SOLUTIONS)


if __name__ == '__main__':
    print(solve())
