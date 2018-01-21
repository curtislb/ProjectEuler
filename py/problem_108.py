#!/usr/bin/env python3

"""problem_108.py

Problem 108: Diophantine reciprocals I

In the following equation x, y, and n are positive integers.

    1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

    1/5 + 1/20 = 1/4
    1/6 + 1/12 = 1/4
    1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct solutions exceeds
MIN_SOLUTIONS?

NOTE: This problem is an easier version of Problem 110; it is strongly advised
that you solve this one first.
"""

__author__ = 'Curtis Belmonte'

import common.divisors as divs


# PARAMETERS ##################################################################


MIN_SOLUTIONS = 1000 # default: 1000


# SOLUTION ####################################################################


def solve() -> int:
    n = 1
    while (divs.count_power_divisors(n, 2) + 1) // 2 <= MIN_SOLUTIONS:
        n += 1
    return n


if __name__ == '__main__':
    print(solve())
