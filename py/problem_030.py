"""problem_030.py

Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of EXPONENTth
powers of their digits.

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

EXPONENT = 5 # default: 5

# SOLUTION ####################################################################

if __name__ == '__main__':
    # search for max value that could be written as powers of its digits
    MAX_DIGIT_POWER = 9**EXPONENT
    max_value = 99
    max_sum = MAX_DIGIT_POWER * 2
    while max_value <= max_sum:
        max_value = max_value * 10 + 9
        max_sum += MAX_DIGIT_POWER
    
    # check all numbers below max value with at least two digits
    total = 0
    for n in range(10, max_value):
        if common.digit_function_sum(n, lambda x: x**EXPONENT) == n:
            total += n
    
    print(total)
