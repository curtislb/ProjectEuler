#!/usr/bin/env python3

"""problem_078.py

Problem 78: Coin partitions

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles in
exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by DIVISOR.

Author: Curtis Belmonte
"""

import common.sequences as seqs


# PARAMETERS ##################################################################


DIVISOR = 10**6 # Default: 10**6


# SOLUTION ####################################################################


def solve():
    partitions = [1, 1]
    n = 2

    while True:
        # compute the recurrence p(n) = p(n - 1) + p(n - 2) - p(n - 5) - ...
        p = 0
        k = 1
        penta = seqs.pentagonal(k)
        while penta <= n:
            sign = int((-1)**(k - 1))
            p += sign * partitions[n - penta]
            k = -k if k > 0 else -k + 1
            penta = seqs.pentagonal(k)

        if p % DIVISOR == 0:
            return n

        partitions.append(p)
        n += 1


if __name__ == '__main__':
    print(solve())
