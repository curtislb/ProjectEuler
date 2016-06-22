"""problem_102.py

Problem 102: Triangle containment

Three distinct points are plotted at random on a Cartesian plane, for which
-1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

    A(-340,495), B(-153,-910), C(835,-947)

    X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ
does not.

Using INPUT_FILE, a text file containing the co-ordinates of one thousand
"random" triangles, find the number of triangles for which the interior
contains the point QUERY_POINT.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

INPUT_FILE = '../input/102.txt' # default: '../input/102.txt'

QUERY_POINT = (0, 0) # default: (0, 0)

# SOLUTION ####################################################################

def vector_sub(u, v):
    return com.vector_pair_op(u, v, lambda x,y: x - y)


def same_side(p1, p2, A, B):
    """Determines if points p1 and p2 are on the same side of segment AB."""
    segment_AB = vector_sub(B, A)
    cross1 = com.cross_product_3d(segment_AB, vector_sub(p1, A))
    cross2 = com.cross_product_3d(segment_AB, vector_sub(p2, A))
    return com.dot_product(cross1, cross2) >= 0


def solve():
    count = 0
    point = QUERY_POINT + (0,)

    with open(INPUT_FILE) as f:
        for line in f:
            # parse triangle vertex coordinates from line
            tokens = [int(t) for t in line.strip().split(',')]
            A = (tokens[0], tokens[1], 0)
            B = (tokens[2], tokens[3], 0)
            C = (tokens[4], tokens[5], 0)

            # check if query point on correct side of all segments
            if (
                same_side(point, A, B, C) and
                same_side(point, B, C, A) and
                same_side(point, C, A, B)
            ):
                count += 1

    return count


if __name__ == '__main__':
    print(solve())
