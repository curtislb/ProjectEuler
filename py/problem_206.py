"""problem_206.py

Problem 206: Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Author: Curtis Belmonte
"""

import common as com

import math

# PARAMETERS ##################################################################

# N/A

# SOLUTION ####################################################################

# the concealed square form to match
square_form = '1_2_3_4_5_6_7_8_9_0'

# the list of digits in the concealed square, in reverse order
rev_form_digits = [None if c == '_' else int(c) for c in square_form[::-1]]


def is_match(n):
    """Determines if the integer n has the correct concealed square form."""

    for form_digit in rev_form_digits:
        # n is too small
        if n == 0:
            return False

        # next digit of n can be anything
        elif form_digit is None:
            n //= 10

        # compare digit of n to corresponding form digit
        else:
            n, digit = divmod(n, 10)
            if digit != form_digit:
                return False

    return True


def solve():
    # begin searching for numbers ending in 30 or 70 above the min square root
    n = int(math.sqrt(int(square_form.replace('_', '0'))))
    while n % 100 not in (30, 70):
        n += 1

    # search for number which produces the correct square form
    while True:
        if is_match(n * n):
            return n
        
        # only consider numbers ending in 30 or 70
        if n % 100 == 30:
            n += 40
        else:
            n += 60


if __name__ == '__main__':
    print(solve())
