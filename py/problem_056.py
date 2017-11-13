#!/usr/bin/env python3

"""problem_056.py

Problem 56: Powerful digit sum

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < MAX_VALUE, what is
the maximum digital sum?

Author: Curtis Belmonte
"""

import common.digits as digs


# PARAMETERS ##################################################################


MAX_VALUE = 100 # default: 100


# SOLUTION ####################################################################


def solve() -> int:
    max_sum = 0
    for a in range(2, MAX_VALUE):
        for b in range(2, MAX_VALUE):
            digit_sum = digs.sum_digits(a**b)
            if digit_sum > max_sum:
                max_sum = digit_sum
    return max_sum


if __name__ == '__main__':
    print(solve())
