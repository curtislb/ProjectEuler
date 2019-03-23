#!/usr/bin/env python3

"""problem_117.py

Problem 117: Red, green, and blue tiles

Using a combination of black square tiles and oblong tiles chosen from: red
tiles measuring two units, green tiles measuring three units, and blue tiles
measuring four units, it is possible to tile a row measuring five units in
length in exactly fifteen different ways.

    K K K K K   R R K K K   K R R K K   K K R R K
    K K K R R   R R R R K   R R K R R   K R R R R
    G G G K K   K G G G K   K K G G G   R R G G G
    G G G R R   B B B B K   K B B B B

How many ways can a row measuring ROW_LENGTH units in length be tiled?

NOTE: This is related to Problem 116."""

__author__ = 'Curtis Belmonte'

from common.utility import memoized


# PARAMETERS ##################################################################


ROW_LENGTH = 50  # default: 50


# SOLUTION ####################################################################


@memoized
def count_tilings(n: int) -> int:
    """Returns the number of unique ways to tile a row of length n >= 1."""
    if n < 5:
        # handle recursive base case
        return 2**(n - 1)
    else:
        # place each tile at end of row and recurse on remainder
        return (count_tilings(n - 1) +
                count_tilings(n - 2) +
                count_tilings(n - 3) +
                count_tilings(n - 4))


def solve() -> int:
    return count_tilings(ROW_LENGTH)


if __name__ == '__main__':
    print(solve())
