#!/usr/bin/env python3

"""problem_124.py

Problem 124: Ordered radicals

The radical of n, rad(n), is the product of the distinct prime factors of n.
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on
n if the radical values are equal, we get:



Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and
E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ MAX_N, find E(INDEX).

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

MAX_N = 100000 # default: 10**5

INDEX = 10000 # default: 10**4

# SOLUTION ####################################################################

def solve():
    radicals = [(1, 1)]
    for n in range(2, MAX_N + 1):
        radicals.append((com.radical(n), n))
    return sorted(radicals)[INDEX - 1][1]


if __name__ == '__main__':
    print(solve())
