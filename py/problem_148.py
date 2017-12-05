#!/usr/bin/env python3

"""problem_148.py

Problem 148: Exploring Pascal's triangle

We can easily verify that none of the entries in the first seven rows of
Pascal's triangle are divisible by 7:

                             1
                         1       1
                     1       2       1
                 1       3       3       1
             1       4       6       4       1
         1       5      10      10       5       1
    1        6      15      20      15       6       1

However, if we check the first one hundred rows, we will find that only 2361 of
the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by PRIME in the first
ROW_COUNT rows of Pascal's triangle.
"""

__author__ = 'Curtis Belmonte'

import math

import common.sequences as seqs


# PARAMETERS ##################################################################


PRIME = 7 # default: 7

ROW_COUNT = 10**9 # default: 10**9


# SOLUTION ####################################################################


def solve() -> int:
    # count number of entries up to nearest power of PRIME
    log_p = int(math.log(ROW_COUNT, PRIME))
    tri_p = seqs.triangular(PRIME)
    power = PRIME**log_p
    nonzero = tri_p**log_p

    # count remaining entries not divisible by PRIME
    count = 0
    remaining = ROW_COUNT
    while remaining > 0:
        msd, remaining = divmod(remaining, power)
        count += nonzero * seqs.triangular(msd)
        power //= PRIME
        nonzero = nonzero * (msd + 1) // tri_p
    
    return count


if __name__ == '__main__':
    print(solve())
