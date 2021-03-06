#!/usr/bin/env python3

"""problem_007.py

Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the Nth prime number?
"""

__author__ = 'Curtis Belmonte'

import common.primes as prime


# PARAMETERS ##################################################################


N = 10001  # default: 10001


# SOLUTION ####################################################################


def solve() -> int:
    return prime.prime(N)


if __name__ == '__main__':
    print(solve())
