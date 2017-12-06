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
"""

__author__ = 'Curtis Belmonte'

from typing import Optional

import common.arithmetic as arith
from common.utility import memoized


# PARAMETERS ##################################################################


MIN_DISCS = 10**12 # default: 10**12


# SOLUTION ####################################################################


@memoized
def b(n: int) -> int:
    """Returns the nth natural number solution for b in the Diophantine
    equation 2b*(b-1) = a*(a-1).
    """
    return (1 if n == 1 else
            3 if n == 2 else
            6 * b(n - 1) - b(n - 2) - 2)


def total_discs(blue_discs: int) -> Optional[float]:
    """Returns the number of discs in total for a valid arrangement with the
    given number of blue discs.
    """
    root = arith.quadratic_roots(1, -1, -2 * blue_discs * (blue_discs - 1))[1]
    if isinstance(root, float):
        return root
    else:
        return None


def solve() -> int:
    # search for first b in 2b*(b-1) = t*(t-1), such that t > MIN_DISCS
    n = 1
    blue = b(n)
    total = total_discs(blue)
    while total is not None and total <= MIN_DISCS:
        n += 1
        blue = b(n)
        total = total_discs(blue)

    return blue


if __name__ == '__main__':
    print(solve())
