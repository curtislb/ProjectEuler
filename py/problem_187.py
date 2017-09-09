#!/usr/bin/env python3

"""problem_187.py

Problem 187: Semiprimes

A composite is a number containing at least two prime factors. For example,
15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3.

There are ten composites below thirty containing precisely two, not necessarily
distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

How many composite integers, n < LIMIT, have precisely two, not necessarily
distinct, prime factors?

Author: Curtis Belmonte
"""

import common.primes as prime


# PARAMETERS ##################################################################


LIMIT = 10**8 # default: 10**8


# SOLUTION ####################################################################


def solve():
    # compute all possible prime factors
    primes = prime.primes_up_to((LIMIT - 1) // 2)
    num_primes = len(primes)

    # count all pairs of factors whose product is less than LIMIT
    count = 0
    for i in range(num_primes):
        a = primes[i]
        max_b = (LIMIT - 1) // a
        for j in range(i, num_primes):
            b = primes[j]
            if b > max_b:
                break
            count += 1

    return count


if __name__ == '__main__':
    print(solve())
