#!/usr/bin/env python3

"""problem_027.py

Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

    n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79
and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < A_LIMIT and |b| < B_LIMIT

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = START_N.
"""

__author__ = 'Curtis Belmonte'

import common.primes as prime
from common.utility import memoized


# PARAMETERS ##################################################################


A_LIMIT = 1000  # default: 1000

B_LIMIT = 1000  # default: 1000

START_N = 0  # default: 0


# SOLUTION ####################################################################


@memoized
def is_prime(n: int) -> bool:
    """Memoized wrapper for the is_prime function."""
    return prime.is_prime(n)


def solve() -> int:
    # search for best a and b from -MAX + 1 to MAX - 1
    best_product = None
    best_streak = -1
    for a in range(-A_LIMIT + 1, A_LIMIT):
        for b in range(-B_LIMIT + 1, B_LIMIT):
            # count number of primes generated for subsequent n
            n = START_N
            result = (n * n) + (a * n) + b
            while is_prime(result):
                # advance result to that generated by next value of n
                result += (2 * n) + 1 + a
                n += 1
            
            # update best product and consecutive prime count if necessary
            streak = n - START_N + 1
            if streak > best_streak:
                best_product = a * b
                best_streak = streak
    
    return best_product


if __name__ == '__main__':
    print(solve())
