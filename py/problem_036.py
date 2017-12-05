#!/usr/bin/env python3

"""problem_036.py

Problem 36: Double-base palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than LIMIT, which are palindromic in base
BASE_A and base BASE_B.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

__author__ = 'Curtis Belmonte'

import common.digits as digs


# PARAMETERS ##################################################################


LIMIT = 1000000 # default: 1000000

BASE_A = 10 # default: 10

BASE_B = 2 # default: 2


# SOLUTION ####################################################################


def solve() -> int:
    total = 0
    
    # generate all even-length palindromes in BASE_A below LIMIT
    n = 1
    palindrome = digs.make_palindrome(n, BASE_A)
    while palindrome < LIMIT:
        # check if palindrome is also a palindrome in BASE_B
        if digs.is_palindrome(palindrome, BASE_B):
            total += palindrome
        
        # generate next even-length palindrome in BASE_A
        n += 1
        palindrome = digs.make_palindrome(n, BASE_A)
    
    # generate all odd-length palindromes in BASE_A below LIMIT
    n = 1
    palindrome = digs.make_palindrome(n, BASE_A, odd_length=True)
    while palindrome < LIMIT:
        # check if palindrome is also a palindrome in BASE_B
        if digs.is_palindrome(palindrome, BASE_B):
            total += palindrome
        
        # generate next odd-length palindrome in BASE_A
        n += 1
        palindrome = digs.make_palindrome(n, BASE_A, odd_length=True)
    
    return total


if __name__ == '__main__':
    print(solve())
