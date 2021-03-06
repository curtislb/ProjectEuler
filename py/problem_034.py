#!/usr/bin/env python3

"""problem_034.py

Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

__author__ = 'Curtis Belmonte'

import common.combinatorics as comb
import common.digits as digs


# PARAMETERS ##################################################################


# N/A


# SOLUTION ####################################################################


def solve() -> int:
    # search for max value that could be written as powers of its digits
    max_digit_factorial = comb.factorial(9)
    max_value = 99
    max_sum = max_digit_factorial * 2
    while max_value <= max_sum:
        max_value = max_value * 10 + 9
        max_sum += max_digit_factorial
    
    # check all numbers below max value with at least two digits
    total = 0
    for n in range(10, max_value):
        if digs.digit_function_sum(n, comb.factorial) == n:
            total += n
    
    return total


if __name__ == '__main__':
    print(solve())
