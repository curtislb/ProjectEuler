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

import math
from typing import Sequence

import common.arrays as arrs
import common.divisors as divs
import common.primes as prime
import common.sequences as seqs


# PARAMETERS ##################################################################


MIN_SOLUTIONS = 1000 # default: 1000


# SOLUTION ####################################################################


def find_min_denom(min_solutions: int) -> int:
    """Finds the least n such that 1/x + 1/y = 1/n exceeds a solution count.

    Specifically, returns the minimum natural number n for which there are more
    than min_solutions integer pairs x <= y that satisfy the above equation.
    """

    # count max distinct prime factors to exceed min_solutions
    prime_count = int(math.ceil(math.log(2 * min_solutions - 1, 3)))

    # check products of primorials up to prime count
    prime_list = prime.primes(prime_count)
    primorials = arrs.cumulative_products(prime_list) # type: Sequence[int]
    for n in seqs.generate_products(primorials):
        # find solution count in terms of divisors of n^2
        if (divs.count_power_divisors(n, 2) + 1) // 2 > min_solutions:
            return n


def solve() -> int:
    return find_min_denom(MIN_SOLUTIONS)


if __name__ == '__main__':
    print(solve())
