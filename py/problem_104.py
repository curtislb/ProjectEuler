#!/usr/bin/env python3

"""problem_104.py

Problem 104: Pandigital Fibonacci ends

The Fibonacci sequence is defined by the recurrence relation:

    F(n) = F(n - 1) + F(n - 2), where F(1) = 1 and F(2) = 1

It turns out that F(541), which contains 113 digits, is the first Fibonacci
number for which the last nine digits are 1-9 pandigital (contain all the
digits 1 to 9, but not necessarily in order). And F(2749), which contains 575
digits, is the first Fibonacci number for which the first nine digits are 1-9
pandigital.

Given that F(k) is the first Fibonacci number for which the first D digits AND
the last D digits are 1 to D pandigital, find k.

Author: Curtis Belmonte
"""

import common as com


# PARAMETERS ##################################################################


D = 9 # default: 9


# SOLUTION ####################################################################


digit_mod = 10**D

pandigit_string = com.pandigital_string(1, D)


def is_end_pandigital(n):
    """Determines if the first and last D digits of n are 1 to D pandigital."""
    if com.is_permutation(str(n % digit_mod), pandigit_string):
        return com.is_permutation(str(n)[:9], pandigit_string)


def solve():
    k = 2750 # TODO: less arbitrary lower bound?
    fib_num = com.fibonacci(k)
    while not is_end_pandigital(fib_num):
        k += 1
        fib_num = com.fibonacci(k)

    return k + 1


if __name__ == '__main__':
    print(solve())
