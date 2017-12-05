#!/usr/bin/env python3

"""problem_018.py

Problem 18: Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle contained in the file
INPUT_FILE.

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method!
"""

__author__ = 'Curtis Belmonte'

import common.fileio as fio
import common.matrices as mat


# PARAMETERS ##################################################################


INPUT_FILE = '../input/018.txt' # default: '../input/018.txt'


# SOLUTION ####################################################################


def solve() -> int:
    triangle = list(fio.ints_from_file(INPUT_FILE))
    return mat.max_triangle_path(triangle)


if __name__ == '__main__':
    print(solve())
