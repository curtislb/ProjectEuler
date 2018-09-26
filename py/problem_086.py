#!/usr/bin/env python3

"""problem_086.py

Problem 86: Cuboid route

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
fly, F, sits in the opposite corner. By travelling on the surfaces of the room
the shortest "straight line" distance from S to F is 10.

However, there are up to three "shortest" path candidates for any given cuboid
and the shortest route doesn't always have integer length.

It can be shown that there are exactly 2060 distinct cuboids, ignoring
rotations, with integer dimensions, up to a maximum size of M by M by M, for
which the shortest route has integer length when M = 100. This is the least
value of M for which the number of solutions first exceeds two thousand; the
number of solutions when M = 99 is 1975.

Find the least value of M such that the number of solutions first exceeds
MIN_SOLUTIONS.
"""

__author__ = 'Curtis Belmonte'

import common.sequences as seqs
from common.utility import memoized


# PARAMETERS ##################################################################


MIN_SOLUTIONS = 10**6 # default: 10**6


# SOLUTION ####################################################################


@memoized
def is_square(n: int) -> bool:
    """Memoized wrapper for the is_square function."""
    return seqs.is_square(n)


def solve() -> int:
    m = 0
    count = 0
    while count <= MIN_SOLUTIONS:
        # count new solutions after incrementing m
        m += 1

        # look for Pythagorean triples (m, n, d) where m = x, n = (y + z)
        for n in range(2, 2 * m + 1):
            if is_square(m**2 + n**2):
                # count choices for z <= y <= m where y + z = n
                if n > m + 1:
                    # only count pairs y, z where z <= y <= m
                    count += (2*m + 2 - n) // 2
                else:
                    # all pairs y, z already satisfy z <= y <= m
                    count += n // 2
    return m


if __name__ == '__main__':
    print(solve())
