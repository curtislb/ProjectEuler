#!/usr/bin/env python3

"""problem_015.py

Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through an N × N grid?

Author: Curtis Belmonte
"""

import common.combinatorics as comb


# PARAMETERS ##################################################################


N = 20 # default: 20


# SOLUTION ####################################################################


def solve() -> int:
    # compute the value of (2*N)! / N! = (2*N) * (2*N - 1) * ... * (N + 1)
    product = 1
    for i in range(N + 1, 2 * N + 1):
        product *= i
    
    # divide the numerator by N! to account for all duplicate moves
    return product // comb.factorial(N)


if __name__ == '__main__':
    print(solve())
