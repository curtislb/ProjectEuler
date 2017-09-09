#!/usr/bin/env python3

"""problem_031.py

Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can AMOUNT be made using any number of coins in COINS?

Author: Curtis Belmonte
"""

import common.combinatorics as comb


# PARAMETERS ##################################################################


AMOUNT = 200 # default: 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
# default: [1, 2, 5, 10, 20, 50, 100, 200]


# SOLUTION ####################################################################


def solve():
    return comb.combination_sums(AMOUNT, COINS)


if __name__ == '__main__':
    print(solve())
