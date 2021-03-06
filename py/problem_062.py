#!/usr/bin/env python3

"""problem_062.py

Problem 62: Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly NUM_PERMS permutations of its digits
are cube.
"""

__author__ = 'Curtis Belmonte'

from typing import Dict, List, Sequence

import common.digits as digs


# PARAMETERS ##################################################################


NUM_PERMS = 5  # default: 5


# SOLUTION ####################################################################


cube_digits: Dict[Sequence[int], List[int]] = {}


def solve() -> int:
    n = 1
    cube = n**3
    while True:
        digits = tuple(digs.digit_counts(cube))
        if digits not in cube_digits:
            cube_digits[digits] = [cube]
        else:
            cube_digits[digits].append(cube)
            if len(cube_digits[digits]) == NUM_PERMS:
                return cube_digits[digits][0]
        n += 1
        cube = n**3


if __name__ == '__main__':
    print(solve())
