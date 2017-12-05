#!/usr/bin/env python3

"""problem_124.py

Problem 124: Ordered radicals

The radical of n, rad(n), is the product of the distinct prime factors of n.
For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on
n if the radical values are equal, we get:

    Unsorted       Sorted
    n    rad(n)    n    rad(n)  k
    1    1         1    1       1
    2    2         2    2       2
    3    3         4    2       3
    4    2         8    2       4
    5    5         3    3       5
    6    6         9    3       6
    7    7         5    5       7
    8    2         6    6       8
    9    3         7    7       9
    10   10        10   10      10

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and
E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ MAX_N, find E(INDEX).
"""

__author__ = 'Curtis Belmonte'

import common.divisors as divs


# PARAMETERS ##################################################################


MAX_N = 10**5 # default: 10**5

INDEX = 10**4 # default: 10**4


# SOLUTION ####################################################################


def solve() -> int:
    radicals = [(1, 1)]
    for n in range(2, MAX_N + 1):
        radicals.append((divs.radical(n), n))
    return sorted(radicals)[INDEX - 1][1]


if __name__ == '__main__':
    print(solve())
