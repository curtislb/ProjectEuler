"""problem_068.py

Problem 68: Magic 5-gon ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
each line adding to nine.

      4
       \
        3
       / \
      1 — 2 — 6
     /
    5

Working clockwise, and starting from the group of three with the numerically
lowest external node (4,3,2 in this example), each solution can be described
uniquely. For example, the above solution can be described by the set: 4,3,2;
6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and
12. There are eight solutions in total.

    Total   Solution Set
    9       4,2,3; 5,3,1; 6,1,2
    9       4,3,2; 6,2,1; 5,1,3
    10      2,3,5; 4,5,1; 6,1,3
    10      2,5,3; 6,3,1; 4,1,5
    11      1,4,6; 3,6,2; 5,2,4
    11      1,6,4; 5,4,2; 3,2,6
    12      1,5,6; 2,6,4; 3,4,5
    12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum
string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to
form 16- and 17-digit strings. What is the maximum 16-digit string for a
"magic" 5-gon ring?

Author: Curtis Belmonte
"""

import common as com

import itertools

# PARAMETERS ##################################################################

# N/A

# SOLUTION ####################################################################

def solve():
    best_int = -com.INFINITY

    # check permutations with 6-10 on outer ring and 1-5 in inner ring
    for outer_ring in itertools.permutations(list(range(7, 11))):
        for inner_ring in itertools.permutations(list(range(1, 6))):
                A = 6
                B, C, D, E = outer_ring
                v, w, x, y, z = inner_ring

                # check if permutation forms magic 5-gon
                if (
                    A + v + w ==
                    B + w + x ==
                    C + x + y ==
                    D + y + z ==
                    E + z + v
                ):
                    # construct 5-gon string from ints
                    ngon_string = ('{}' * 15).format(
                        A, v, w,
                        B, w, x,
                        C, x, y,
                        D, y, z,
                        E, z, v
                    )

                    # update largest 5-gon int as necessary
                    ngon_int = int(ngon_string)
                    if ngon_int > best_int:
                        best_int = ngon_int

    return best_int

if __name__ == '__main__':
    print(solve())
