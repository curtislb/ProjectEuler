#!/usr/bin/env python3

"""problem_091.py

Problem 91: Right triangles with integer coordinates

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and
are joined to the origin, O(0, 0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can be
formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.

Given that 0 ≤ x1, y1, x2, y2 ≤ MAX_COORD, how many right triangles can be
formed?

Author: Curtis Belmonte
"""


# PARAMETERS ##################################################################


MAX_COORD = 50 # default: 50


# SOLUTION ####################################################################


def solve() -> int:
    # prepare all valid points in range
    points = []
    for x in range(MAX_COORD + 1):
        for y in range(MAX_COORD + 1):
            if x == 0 and y == 0:
                continue
            points.append((x, y))

    # count all pairs of points that form right triangles with origin
    count = 0
    num_points = len(points)
    for i in range(num_points):
        for j in range(i + 1, num_points):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # compute and order side lengths of triangle
            a_sqr = x1**2 + y1**2
            b_sqr = x2**2 + y2**2
            c_sqr = (x2 - x1)**2 + (y2 - y1)**2
            a_sqr, b_sqr, c_sqr = sorted((a_sqr, b_sqr, c_sqr))

            # check if side lengths form Pythagorean triple
            if a_sqr + b_sqr == c_sqr:
                count += 1

    return count


if __name__ == '__main__':
    print(solve())
