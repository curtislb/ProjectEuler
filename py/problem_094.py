#!/usr/bin/env python3

"""problem_094.py

Problem 94: Almost equilateral triangles

It is easily proved that no equilateral triangle exists with integral length
sides and integral area. However, the almost equilateral triangle 5-5-6 has an
area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two
sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral
side lengths and area and whose perimeters do not exceed MAX_PERIMETER.
"""

__author__ = 'Curtis Belmonte'


# PARAMETERS ##################################################################


MAX_PERIMETER = 10**9 # default: 10**9


# SOLUTION ####################################################################

def solve() -> int:
    total = 0

    # generate Pythagorean triples corresponding to valid triangles
    i = 0
    triple = (3, 4, 5)
    max_side = MAX_PERIMETER // 3
    while triple[2] < max_side:
        # add perimeter of triangle formed by current triple
        total += 2 * (triple[2] + min(triple))

        # generate next triple, alternating transformations
        a, b, c = triple
        a2 = 2 * a
        b2 = 2 * b
        c2 = 2 * c
        c3 = 3 * c
        if i % 2 == 0:
            triple = (-a + b2 + c2, -a2 + b + c2, -a2 + b2 + c3)
        else:
            triple = (a - b2 + c2, a2 - b + c2, a2 - b2 + c3)

        i += 1

    return total


if __name__ == '__main__':
    print(solve())
