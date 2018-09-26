#!/usr/bin/env python3

"""problem_123.py

Problem 123: Prime square remainders

Let p_n be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when
(p_n − 1)^n + (p_n + 1)^n is divided by p_n^2.

For example, when n = 3, p_3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10^9 is 7037.

Find the least value of n for which the remainder first exceeds 10^POWER.
"""

__author__ = 'Curtis Belmonte'

import math

import common.arithmetic as arith
import common.primes as prime


# PARAMETERS ##################################################################


POWER = 10 # default: 10


# SOLUTION ####################################################################


def solve() -> int:
    # prepare initial list of primes
    max_prime = int(math.ceil(10**(POWER / 2 + 1)))
    prime_list = prime.primes_up_to(max_prime)

    # search for n that satisfies problem statement
    min_remainder = 10 ** POWER
    n = 1
    while True:
        while n <= len(prime_list):
            # check if modular sum of terms exceeds min_remainder
            p = prime_list[n - 1]
            p_sqr = p**2
            term_1 = arith.mod_power(p - 1, n, p_sqr)
            term_2 = arith.mod_power(p + 1, n, p_sqr)
            if (term_1 + term_2) % p_sqr > min_remainder:
                return n

            # advance to next prime number
            n += 1

        # answer not found; generate more primes until it is
        max_prime *= 10
        prime_list = prime.primes_up_to(max_prime)


if __name__ == '__main__':
    print(solve())
