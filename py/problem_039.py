#!/usr/bin/env python3

"""problem_039.py

Problem 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ MAX_PERIMETER, is the number of solutions maximised?

Author: Curtis Belmonte
"""

from collections import Counter

import common as com
from common import memoized

# PARAMETERS ##################################################################


MAX_PERIMETER = 1000 # default: 1000


# SOLUTION ####################################################################


@memoized
def int_sqrt(num):
    """Memoized wrapper for the common.int_sqrt function."""
    return com.int_sqrt(num)


def solve():
    # precompute perfect squares up to half the max perimeter squared
    squares = set()
    n = 0
    n_square = n * n
    max_square = (MAX_PERIMETER // 2)**2
    while n_square <= max_square:
        squares.add(n_square)
        n += 1
        n_square = n * n
    
    # search for triplets of perfect squares that satisfy a^2 + b^2 = c^2
    counts = Counter()
    for a_square in squares:
        for b_square in squares:
            c_square = a_square + b_square
            if c_square in squares:
                # compute the perimeter a + b + c
                a = int_sqrt(a_square)
                b = int_sqrt(b_square)
                c = int_sqrt(c_square)
                perimeter = a + b + c
                
                # if perimeter does not exceed max perimeter, increment count
                if perimeter <= MAX_PERIMETER:
                    counts.update([perimeter])
    
    # return the perimeter with the greatest count
    return counts.most_common(1)[0][0]


if __name__ == '__main__':
    print(solve())
