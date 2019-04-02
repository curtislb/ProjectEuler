#!/usr/bin/env python3

"""problem_081.py

Problem 81: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated by parentheses
and is equal to 2427.

    (131)  673   234   103    18
    (201)  (96) (342)  965   150
     630   803  (746) (422)  111
     537   699   497  (121)  956
     805   732   524   (37) (331)

Find the minimal path sum in FILE_NAME, a text file containing a square
matrix, from the left column to the right column.
"""

__author__ = 'Curtis Belmonte'

from typing import List, Optional

import common.fileio as fio
import common.utility as util


# PARAMETERS ##################################################################


FILE_NAME = '../input/081.txt'  # default: '../input/081.txt'


# SOLUTION ####################################################################

def get_min_cost(matrix: List[List[int]], i: int, j: int) -> int:
    down_cost = matrix[i + 1][j] if i < -1 else None
    right_cost = matrix[i][j + 1] if j < -1 else None
    min_cost = util.min_present(down_cost, right_cost)
    return 0 if min_cost is None else min_cost


def solve() -> Optional[int]:
    matrix: List[List[int]] = list(fio.ints_from_file(FILE_NAME, sep=','))
    n = len(matrix[0])
    
    # dynamically update costs along diagonals from bottom-right to middle
    for diag in range(2, n + 1):
        i, j = -1, -diag
        while j < 0:
            matrix[i][j] += get_min_cost(matrix, i, j)
            i, j = i - 1, j + 1

    # dynamically update costs along diagonals from middle to top-left
    for diag in range(2, n + 1):
        i, j = -diag, -n
        while i >= -n:
            matrix[i][j] += get_min_cost(matrix, i, j)
            i, j = i - 1, j + 1

    return matrix[0][0]


if __name__ == '__main__':
    print(solve())
