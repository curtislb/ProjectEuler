#!/usr/bin/env python3

"""problem_040.py

Problem 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive
integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the
following expression.

    d(1) × d(10) × d(100) × ... × d(MAX_POWER_10)

Author: Curtis Belmonte
"""

import common as com


# PARAMETERS ##################################################################


MAX_POWER_10 = 1000000 # default: 1000000


# SOLUTION ####################################################################


def solve():
    # search for and multiply all necessary digits
    product = 1
    power_10 = 1
    position = 1
    number = 1
    while power_10 <= MAX_POWER_10:
        # step forward to number that contains next necessary digit
        digit_count = com.count_digits(number)
        while position < power_10 - digit_count + 1:
            digit_count = com.count_digits(number)
            position += digit_count
            number += 1
        
        # get necessary digit from current number
        product *= com.get_digit(number, power_10 - position + 1)
        
        # advance count to next necessary digit index
        power_10 *= 10
    
    return product


if __name__ == '__main__':
    print(solve())
