#!/usr/bin/env python3

"""problem_071.py

Problem 71: Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n < d and
HCF(n,d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
    5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ MAX_DENOM in ascending
order of size, find the numerator of the fraction immediately to the left of
TARGET_FRAC.
"""

__author__ = 'Curtis Belmonte'

from typing import Optional

from fractions import Fraction


# PARAMETERS ##################################################################


MAX_DENOM = 10**6  # default: 10**6

TARGET_FRAC = Fraction(3, 7)  # default: Fraction(3, 7)


# SOLUTION ####################################################################


def solve() -> Optional[int]:
    for d in range(MAX_DENOM, TARGET_FRAC.denominator - 1, -1):
        if d % TARGET_FRAC.denominator == 0:
            n = TARGET_FRAC.numerator * (d // TARGET_FRAC.denominator)
            return Fraction(n - 1, d).numerator

    # target fraction not found
    return None


if __name__ == '__main__':
    print(solve())
