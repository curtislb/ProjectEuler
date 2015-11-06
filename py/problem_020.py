"""problem_020.py

Problem 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the
digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number N!

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

N = 100 # default: 100

# SOLUTION ####################################################################

def solve():
    return com.sum_digits(com.factorial(N))


if __name__ == '__main__':
    print(solve())
