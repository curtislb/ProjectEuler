#!/usr/bin/env python3

"""problem_016.py

Problem 16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number BASE^EXPONENT?

Author: Curtis Belmonte
"""

import common.digits as digs


# PARAMETERS ##################################################################


BASE = 2 # default: 2

EXPONENT = 1000 # default: 1000


# SOLUTION ####################################################################


def solve():
    return digs.sum_digits(BASE**EXPONENT)


if __name__ == '__main__':
    print(solve())
