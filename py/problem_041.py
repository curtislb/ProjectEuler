#!/usr/bin/env python3

"""problem_041.py

Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

Author: Curtis Belmonte
"""

import common.arrays as arrs
import common.digits as digs
import common.primes as prime


# PARAMETERS ##################################################################


# N/A


# SOLUTION ####################################################################


# Array of 1 to n pandigital numbers for n from 2 to 7
pandigit_strings = [digs.pandigital_string(1, n) for n in range(2, 8)]


def solve():
    # compute primes up to maximum possible pandigital number
    # note: 1 to 8 or 9 pandigital numbers cannot be prime (divisible by 3)
    prime_nums = prime.primes_up_to(7654321)
    
    # check if each prime is 1 to n pandigital in decreasing order
    i = -1
    p = prime_nums[i]
    digit_count = digs.count_digits(p)
    while not arrs.is_permutation(str(p), pandigit_strings[digit_count-2]):
        # advance to next largest prime number
        i -= 1
        p = prime_nums[i]
        digit_count = digs.count_digits(p)
    
    # print largest prime that satisfies the conditions
    return prime_nums[i]


if __name__ == '__main__':
    print(solve())
