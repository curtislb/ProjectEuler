#!/usr/bin/env python3

"""problem_073.py

Problem 73: Counting fractions in a range

Consider the fraction, n/d, where n and d are positive integers. If n < d and
HCF(n,d) = 1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7,
3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between MIN_FRAC and MAX_FRAC in the sorted set of
reduced proper fractions for d ≤ MAX_D?

Author: Curtis Belmonte
"""

from fractions import Fraction

import common.divisors as divs


# PARAMETERS ##################################################################


MIN_FRAC = Fraction(1, 3) # default: Fraction(1, 3)

MAX_FRAC = Fraction(1, 2) # default: Fraction(1, 2)

MAX_D = 12000 # default: 12000


# SOLUTION ####################################################################


def solve():
    total = 0

    # skip denominators for which all fractions are out of range
    min_d = 2
    while Fraction(1, min_d) > MIN_FRAC:
        min_d += 1

    # search for coprime n, d pairs in range
    for d in range(min_d, MAX_D + 1):
        min_n = int(float(MIN_FRAC * d)) + 1
        max_n = int(float(MAX_FRAC * d))
        for n in range(min_n, max_n + 1):
            if divs.is_coprime_pair(n, d):
                total += 1

    return total


if __name__ == '__main__':
    print(solve())
