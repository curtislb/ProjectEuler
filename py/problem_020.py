"""problem_020.py

Problem 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the
digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number N!

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

N = 100 # default: 100

# SOLUTION ####################################################################

if __name__ == '__main__':
    print(common.sum_digits(common.factorial(N)))
