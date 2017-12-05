#!/usr/bin/env python3

"""problem_026.py

Problem 26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10   =     0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < LIMIT for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""

__author__ = 'Curtis Belmonte'

from typing import *


# PARAMETERS ##################################################################


LIMIT = 1000 # default: 1000


# SOLUTION ####################################################################


def reciprocal_cycle_length(n: int) -> int:
    """Returns the length of the recurring cycle in the decimal fraction part
    of 1/n for some natural number n.
    """
    
    # perform long division for 1/n
    remainders = {} # type: Dict[int, int]
    dividend = 1
    digit_count = 0
    while dividend != 0:
        # compute next remainder
        dividend = (dividend * 10) % n
        
        if dividend in remainders:
            # remainder has been seen before; found cycle
            return digit_count - remainders[dividend]
        else:
            # store remainder for later cycle detection
            remainders[dividend] = digit_count
        
        digit_count += 1
        
    # division occurred without remainder; no digit cycle
    return 0


def solve() -> int:
    # search for d with longest reciprocal cycle 
    max_d = 0
    max_length = -1
    for d in range(2, LIMIT):
        length = reciprocal_cycle_length(d)
        if length > max_length:
            max_d = d
            max_length = length
    
    return max_d


if __name__ == '__main__':
    print(solve())
