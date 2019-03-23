#!/usr/bin/env python3

"""problem_070.py

Problem 70: Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to
determine the number of positive numbers less than or equal to n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < MAX_N, for which φ(n) is a permutation of n and
the ratio n/φ(n) produces a minimum.
"""

__author__ = 'Curtis Belmonte'

from typing import Optional

import common.arrays as arrs
import common.primes as prime


# PARAMETERS ##################################################################


MAX_N = 10**7  # default: 10**7


# SOLUTION ####################################################################


def two_prime_phi(p1: int, p2: int) -> int:
    """Returns the totient of the product of two primes p1 and p2."""
    return (p1 - 1) * (p2 - 1)


def solve() -> Optional[int]:
    best_n = None
    best_ratio = float('inf')
    primes = prime.primes_up_to(MAX_N)

    for i, p1 in enumerate(primes):
        # cut off if all remaining products exceed MAX_N
        if p1**2 > MAX_N:
            break

        for j in range(i, len(primes)):
            p2 = primes[j]

            # compute n as the product of two primes
            n = p1 * p2
            if n > MAX_N:
                break

            # check if totient is a permutation and compare ratio
            phi = two_prime_phi(p1, p2)
            if arrs.is_permutation(str(n), str(phi)):
                ratio = n / phi
                if ratio < best_ratio:
                    best_n = n
                    best_ratio = ratio

    return best_n


if __name__ == '__main__':
    print(solve())
