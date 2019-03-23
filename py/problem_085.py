#!/usr/bin/env python3

"""problem_085.py

Problem 85: Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2
contains eighteen rectangles.

Although there exists no rectangular grid that contains exactly RECT_TARGET
rectangles, find the area of the grid with the nearest solution.
"""

__author__ = 'Curtis Belmonte'

from typing import Optional

import common.arithmetic as arith


# PARAMETERS ##################################################################


RECT_TARGET = 2 * 10**6  # default: 2 * 10**6


# SOLUTION ####################################################################


def count_rectangles(m: int, n: int) -> int:
    """Returns the number of rectangles in an m by n rectangular grid."""
    return m * (m + 1) * n * (n + 1) // 4


def solve() -> Optional[int]:
    best_diff = float('inf')
    best_area = None
    upper_bound = arith.int_sqrt(RECT_TARGET * 4)
    for m in range(1, upper_bound + 1):
        for n in range(1, upper_bound + 1):
            if m * n > upper_bound:
                break

            diff = abs(RECT_TARGET - count_rectangles(m, n))
            if diff < best_diff:
                best_diff = diff
                best_area = m * n

    return best_area


if __name__ == '__main__':
    print(solve())
