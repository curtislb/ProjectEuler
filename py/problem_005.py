#!/usr/bin/env python3

"""problem_005.py

Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to MAX?

Author: Curtis Belmonte
"""

import common as com


# PARAMETERS ##################################################################


MAX = 20 # default: 20


# SOLUTION ####################################################################


def solve():
    return com.lcm_all([num for num in range(2, MAX + 1)])


if __name__ == '__main__':
    print(solve())
