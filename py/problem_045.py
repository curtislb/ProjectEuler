#!/usr/bin/env python3

"""problem_045.py

Problem 45: Triangular, pentagonal, and hexagonal

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

    Triangle      T(n) = n(n+1)/2     1, 3, 6, 10, 15, ...
    Pentagonal    P(n) = n(3n−1)/2    1, 5, 12, 22, 35, ...
    Hexagonal     H(n) = n(2n−1)      1, 6, 15, 28, 45, ...

It can be verified that T(285) = P(165) = H(143) = 40755.

Find the smallest triangle number greater than LOWER_LIMIT that is also
pentagonal and hexagonal.
"""

__author__ = 'Curtis Belmonte'

import common.sequences as seqs


# PARAMETERS ##################################################################


LOWER_LIMIT = 40755 # default: 40755


# SOLUTION ####################################################################


def solve() -> int:
    # generate the first triangle number above LOWER_LIMIT
    tri_num = 0
    n = 1
    while tri_num <= LOWER_LIMIT:
        tri_num += n
        n += 1
    
    # check if each subsequent triangle number is hexagonal and pentagonal
    while (not seqs.is_hexagonal(tri_num) or
           not seqs.is_pentagonal(tri_num)):
        tri_num += n
        n += 1
    
    return tri_num


if __name__ == '__main__':
    print(solve())
