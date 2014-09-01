"""problem_016.py

Problem 16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number BASE^EXPONENT?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

BASE = 2 # default: 2
EXPONENT = 1000 # default: 1000

# SOLUTION ####################################################################

if __name__ == '__main__':
    print(common.sum_digits(BASE**EXPONENT))