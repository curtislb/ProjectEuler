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
FILE_NAME.

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method!
"""

__author__ = 'Curtis Belmonte'

from typing import List

import common.fileio as fio


# PARAMETERS ##################################################################


FILE_NAME = '../input/018.txt'  # default: '../input/018.txt'


# SOLUTION ####################################################################


def max_triangle_path(triangle: List[List[int]]) -> int:
    """Alters triangle and returns the maximum path sum from top to bottom.

    A path is valid iff it consists of a number from each row of the triangle
    such that each number is adjacent to those in the rows above and below it.
    """

    num_rows = len(triangle)

    # add maximum adjacent values from row above to each row
    for i in range(1, num_rows):
        for j in range(i + 1):
            if j != 0 and j != i:
                # two adjacent elements above; add maximal
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            elif j == 0:
                # no adjacent element to left above; add right
                triangle[i][j] += triangle[i - 1][j]
            else:
                # no adjacent element to right above; add left
                triangle[i][j] += triangle[i - 1][j - 1]

    # return maximal sum accumulated in last row of triangle
    return max(triangle[-1])


def solve() -> int:
    return max_triangle_path(list(fio.ints_from_file(FILE_NAME)))


if __name__ == '__main__':
    print(solve())
