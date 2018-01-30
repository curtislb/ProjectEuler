#!/usr/bin/env python3

"""problem_500.py

Problem 500: Problem 500!!!

The number of divisors of 120 is 16. In fact 120 is the smallest number having
16 divisors.

Find the smallest number with 2^POWER divisors. Give your answer modulo MOD.
"""

__author__ = 'Curtis Belmonte'

import heapq
import math

import common.arithmetic as arith
import common.primes as prime


# PARAMETERS ##################################################################


POWER = 500500 # default: 500500

MOD = 500500507 # default: 500500507


# SOLUTION ####################################################################


def solve() -> int:
    # find all potential prime factors, and keep track of max
    factors = prime.primes(POWER)
    max_factor = factors[-1]
    sqrt_max_factor = math.sqrt(max_factor)

    mod_product = 1
    squares_exceed_max = False
    for _ in range(POWER):
        # multiply minimum factor into modular product
        factor = heapq.heappop(factors)
        mod_product = arith.mod_multiply(mod_product, factor, MOD)

        # add squares until they exceed the max factor
        if not squares_exceed_max:
            if factor > sqrt_max_factor:
                squares_exceed_max = True
            else:
                heapq.heappush(factors, factor**2)

    return mod_product


if __name__ == '__main__':
    print(solve())
