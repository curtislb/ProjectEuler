#!/usr/bin/env python3

"""problem_102.py

Problem 102: Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which
-1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

    A(-340,495), B(-153,-910), C(835,-947)

    X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using FILE_NAME, a text file containing the co-ordinates of one thousand
"random" triangles, find the number of triangles for which the interior
contains the point QUERY_POINT.
"""

__author__ = 'Curtis Belmonte'

from typing import Sequence

import common.matrices as mat


# PARAMETERS ##################################################################


FILE_NAME = '../input/102.txt'  # default: '../input/102.txt'

QUERY_POINT = (0, 0)  # default: (0, 0)


# SOLUTION ####################################################################


def vector_sub(u: Sequence[int], v: Sequence[int]) -> Sequence[int]:
    """Returns the difference (u - v) of equal-length vectors u and v."""
    return [u[i] - v[i] for i in range(len(u))]


def on_same_side(
        p1: Sequence[int],
        p2: Sequence[int],
        a: Sequence[int],
        b: Sequence[int]) -> bool:

    """Determines if points p1 and p2 are on the same side of segment AB."""

    segment_ab = vector_sub(b, a)
    cross1 = mat.cross_product_3d(segment_ab, vector_sub(p1, a))
    cross2 = mat.cross_product_3d(segment_ab, vector_sub(p2, a))
    return mat.dot_product(cross1, cross2) >= 0


def solve() -> int:
    count = 0
    point = QUERY_POINT + (0,)

    with open(FILE_NAME) as input_file:
        for line in input_file:
            # parse triangle vertex coordinates from line
            tokens = map(int, line.strip().split(','))
            a = (next(tokens), next(tokens), 0)
            b = (next(tokens), next(tokens), 0)
            c = (next(tokens), next(tokens), 0)

            # check if query point on correct side of all segments
            if (on_same_side(point, a, b, c)
                    and on_same_side(point, b, c, a)
                    and on_same_side(point, c, a, b)):
                count += 1

    return count


if __name__ == '__main__':
    print(solve())
