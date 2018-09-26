#!/usr/bin/env python3

"""problem_347.py

Problem 347: Largest integer divisible by two primes

The largest integer ≤ 100 that is only divisible by both the primes 2 and 3 is
96, as 96 = 32 * 3 = 2^5 * 3. For two distinct primes p and q let M(p, q, n) be
the largest positive integer ≤ n only divisible by both p and q and
M(p, q, n) = 0 if such a positive integer does not exist.

    E.g. M(2, 3, 100) = 96.

M(3, 5, 100) = 75 and not 90 because 90 is divisible by 2, 3 and 5. Also
M(2, 73, 100) = 0 because there does not exist a positive integer ≤ 100 that is
divisible by both 2 and 73.

Let S(n) be the sum of all distinct M(p, q, n). S(100) = 2262. Find S(N).
"""

__author__ = 'Curtis Belmonte'

import math

import common.primes as prime


# PARAMETERS ##################################################################


N = 10**7 # default: 10**7


# SOLUTION ####################################################################


def max_exclusive_product(p: int, q: int, n: int) -> int:
    """Finds the maximum exclusive product of primes p < q not exceeding n.

    The result is a natural number whose only prime factors are p and q and is
    the largest such number <= n, if any such number exists. If no such number
    exists, the result is instead 0.
    """

    max_num = 0

    # generate products of powers of p and q up to n
    max_p_power = n // q
    p_power = p
    while p_power <= max_p_power:
        prod = p_power * q
        while prod <= n:
            # keep track of max product generated
            if prod > max_num:
                max_num = prod
            prod *= q
        p_power *= p

    return max_num


def solve() -> int:
    # generate all possible prime factors
    prime_list = prime.primes_up_to(N // 2)
    prime_count = len(prime_list)

    # add maximum products <= N for all valid prime pairs p < q
    total = 0
    max_p = int(math.sqrt(N))
    for i in range(prime_count - 1):
        # only consider p <= sqrt(N)
        p = prime_list[i]
        if p > max_p:
            break

        max_q = N // p
        for j in range(i + 1, prime_count):
            # only consider q <= N / p
            q = prime_list[j]
            if q > max_q:
                break

            # add maximum exclusive product <= N for p, q
            total += max_exclusive_product(p, q, N)

    return total


if __name__ == '__main__':
    print(solve())
