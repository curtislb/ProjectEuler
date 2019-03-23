#!/usr/bin/env python3

"""problem_116.py

Problem 116: Red, green or blue tiles

A row of five black square tiles is to have a number of its tiles replaced with
coloured oblong tiles chosen from red (length two), green (length three), or
blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

    R R K K K
    K R R K K
    K K R R K
    K K K R R
    R R R R K
    R R K R R
    K R R R R

If green tiles are chosen there are three ways.

    G G G K K
    K G G G K
    K K G G G

And if blue tiles are chosen there are two ways.

    B B B B K
    K B B B B

Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring ROW_LENGTH units
in length be replaced if colours cannot be mixed and at least one coloured tile
must be used?

NOTE: This is related to Problem 117.
"""

__author__ = 'Curtis Belmonte'

import common.combinatorics as comb
import common.sequences as seqs


# PARAMETERS ##################################################################


ROW_LENGTH = 50  # default: 50


# SOLUTION ####################################################################


def solve() -> int:
    count = 0

    # count combinations over all possible tile lengths
    for tile in range(2, 5):
        for num_tiles in range(1, (ROW_LENGTH // tile) + 1):
            prod = seqs.arithmetic_product(
                ROW_LENGTH - (tile - 1) * num_tiles, num_tiles, -1)
            count += prod // comb.factorial(num_tiles)

    return count


if __name__ == '__main__':
    print(solve())
