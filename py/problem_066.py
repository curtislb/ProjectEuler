#!/usr/bin/env python3

"""problem_066.py

Problem 66: Diophantine equation

Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is
square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
obtained when D=5.

Find the value of D ≤ MAX_D in minimal solutions of x for which the largest
value of x is obtained.

Author: Curtis Belmonte
"""

from typing import *

import common.expansion as expan
import common.sequences as seqs
from common.utility import memoized


# PARAMETERS ##################################################################


MAX_D = 1000 # default: 1000


# SOLUTION ####################################################################


@memoized
def partial_numerator(n: int, a0: int, block: Sequence[int]) -> int:
    """Computes the numerator of the partial quotient p_n/q_n for the continued
    fraction expansion sqrt(D) = [a0; (block)].

    Adapted from http://mathworld.wolfram.com/ContinuedFraction.html"""

    # handle base cases
    if n == 0:
        return a0
    if n == 1:
        return a0 * (block[0]) + 1

    # compute answer using recurrence relation
    period = len(block)
    return (block[(n - 1) % period] * partial_numerator(n - 1, a0, block)
            + partial_numerator(n - 2, a0, block))


def solve() -> int:
    best_d = None
    best_x = -float('inf')

    for d in range(2, MAX_D + 1):
        # skip perfect square values
        if seqs.is_square(d):
            continue

        # compute continued fraction expansion of sqrt(D)
        a0, block = expan.sqrt_fraction_expansion(d)
        block = tuple(block)
        r = len(block) - 1

        # compute minimal integer solution by computing partial quotient
        # (see http://mathworld.wolfram.com/PellEquation.html)
        if r % 2 == 1:
            x = partial_numerator(r, a0, block)
        else:
            x = partial_numerator(2 * r + 1, a0, block)

        # update best values of D and x as necessary
        if x > best_x:
            best_d = d
            best_x = x

    return best_d


if __name__ == '__main__':
    print(solve())
