#!/usr/bin/env python3

"""problem_204.py

Problem 204: Generalised Hamming Numbers

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15. There
are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if it
has no prime factor larger than n. Hence the Hamming numbers are the
generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type TYPE are there which don't exceed
MAX_NUMBER?
"""

__author__ = 'Curtis Belmonte'

import common.primes as prime


# PARAMETERS ##################################################################


TYPE = 100  # default: 100

MAX_NUMBER = 10**9  # default: 10**9


# SOLUTION ####################################################################


def solve() -> int:
    # find all prime factors up to TYPE
    prime_list = prime.primes_up_to(TYPE)

    # generate all Hamming numbers <= MAX_NUMBER
    ham_nums = {1}
    for p in prime_list:
        # multiply each number by p until it exceeds MAX_NUMBER
        multiples = set()
        for n in ham_nums:
            while n <= MAX_NUMBER:
                multiples.add(n)
                n *= p

        # set distinct multiples as new Hamming number set
        ham_nums = multiples

    # count the distinct Hamming numbers
    return len(ham_nums)


if __name__ == '__main__':
    print(solve())
