#!/usr/bin/env python3

"""problem_100.py

Problem 100: Arranged probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and
six red discs, and two discs were taken at random, it can be seen that the
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two
blue discs at random, is a box containing eighty-five blue discs and
thirty-five red discs.

By finding the first arrangement to contain over MIN_DISCS discs in total,
determine the number of blue discs that the box would contain.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

MIN_DISCS = 10**12 # default: 10**12

# SOLUTION ####################################################################

@com.memoized
def b(n):
    """Returns the nth natural number solution for b in the Diophantine
    equation 2b*(b-1) = a*(a-1)."""

    if n < 3:
        return 3 if n == 2 else 1 # if n == 1

    return 6*b(n - 1) - b(n - 2) - 2


def total_discs(blue_discs):
    """Returns the number of discs in total for an arrangement with the given
    number of blue discs."""
    return com.quadratic_roots(1, -1, -2*blue_discs*(blue_discs - 1))[1]


def solve():
    # search for first b in 2b*(b-1) = t*(t-1), such that t > MIN_DISCS
    n = 1
    blue = b(n)
    total = total_discs(blue)
    while total <= MIN_DISCS:
        n += 1
        blue = b(n)
        total = total_discs(blue)

    return blue


if __name__ == '__main__':
    print(solve())
