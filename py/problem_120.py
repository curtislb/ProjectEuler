#!/usr/bin/env python3

"""problem_120.py

Problem 120: Square remainders

Let r be the remainder when (a−1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 ≡ 42 mod 49. And
as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

For MIN_A ≤ a ≤ MAX_A, find ∑ r_max.
"""

__author__ = 'Curtis Belmonte'


# PARAMETERS ##################################################################


MIN_A = 3  # default: 3

MAX_A = 1000  # default: 1000


# SOLUTION ####################################################################


def solve() -> int:
    total = 0
    
    for a in range(MIN_A, MAX_A + 1):
        # for even a, r_max = a^2 - 2a
        if a % 2 == 0:
            total += a**2 - 2 * a
        
        # for odd a, r_max = a^2 - a
        else:
            total += a**2 - a

    return total


if __name__ == '__main__':
    print(solve())
