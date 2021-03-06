#!/usr/bin/env python3

"""problem_024.py

Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the Nth lexicographic permutation of the digits DIGITS?
"""

__author__ = 'Curtis Belmonte'

import common.combinatorics as comb


# PARAMETERS ##################################################################


N = 1000000  # default: 1000000

DIGITS = list(range(10))  # default: list(range(10))


# SOLUTION ####################################################################


def solve() -> int:
    # adjust permutation number to be zero-indexed
    n = N - 1
    
    # sort the digits in lexicographic order
    digits = sorted(DIGITS)
    
    # determine each digit of the nth lexicographic permutation
    digit_count = len(DIGITS)
    permutation_digits = []
    for i in range(1, digit_count):
        digit, n = divmod(n, comb.factorial(digit_count - i))
        permutation_digits.append(digits[digit])
        del digits[digit]
    
    # append the remaining digit and print the result
    permutation_digits.append(digits[0])
    return int(''.join(map(str, permutation_digits)))


if __name__ == '__main__':
    print(solve())
