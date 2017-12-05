#!/usr/bin/env python3

"""problem_057.py

Problem 57: Square root convergents

It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first NUM_EXPANSIONS expansions, how many fractions contain a numerator
with more digits than denominator?
"""

__author__ = 'Curtis Belmonte'

from fractions import Fraction

import common.digits as digs


# PARAMETERS ##################################################################


NUM_EXPANSIONS = 1000 # default: 1000


# SOLUTION ####################################################################


def solve() -> int:
    frac = Fraction(1)
    count = 0
    for _ in range(NUM_EXPANSIONS):
        frac = 1 + Fraction(1, 1 + frac)
        numer = frac.numerator
        denom = frac.denominator
        if digs.count_digits(numer) > digs.count_digits(denom):
            count += 1
    return count


if __name__ == '__main__':
    print(solve())
