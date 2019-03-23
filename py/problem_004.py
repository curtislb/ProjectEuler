#!/usr/bin/env python3

"""problem_004.py

Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two D-digit numbers.
"""

__author__ = 'Curtis Belmonte'

import common.digits as digs


# PARAMETERS ##################################################################


D = 3  # default: 3


# SOLUTION ####################################################################


def solve() -> int:
    # calculate max and min D-digit numbers
    max_factor = 10**D - 1
    min_factor = 10**(D - 1)

    # multiply D-digit products to find largest palindrome
    max_product = -1
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            # any products larger than current max_product for this i?
            product = i * j
            if product <= max_product:
                break

            # check if i * j is a palindrome
            if digs.is_palindrome(product):
                max_product = product
                break

    return max_product


if __name__ == '__main__':
    print(solve())
