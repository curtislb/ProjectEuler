#!/usr/bin/env python3

"""problem_075.py

Problem 75: Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ MAX_LENGTH
can exactly one integer sided right angle triangle be formed?

Author: Curtis Belmonte
"""

import common as com

import collections
import math

# PARAMETERS ##################################################################

MAX_LENGTH = 1500000 # default: 1500000

# SOLUTION ####################################################################

def triple_length(m, n):
    """Returns the length of the triangle formed by the Pythagorean triple
    (m^2 - n^2, 2mn, m^2 + n^2)."""
    return 2 * m * (m + n)


def solve():
    # count lengths for all valid Pythagorean triples
    length_counts = collections.Counter()
    max_m = int(math.sqrt(MAX_LENGTH / 2))
    for n in range(1, max_m):
        for m in range(n + 1, max_m + 1):
            # check if Pythagorean triple is primitive
            if (m - n) % 2 == 1 and com.is_coprime_pair(m, n):
                # count length of primitive triple and all multiples
                length = triple_length(m, n)
                for k_length in range(length, MAX_LENGTH + 1, length):
                    length_counts[k_length] += 1

    # count all lengths with only one triple
    count = 0
    for num_triples in length_counts.values():
        if num_triples == 1:
            count += 1

    return count


if __name__ == '__main__':
    print(solve())
