"""problem_001.py

Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of M or N below LIMIT.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

M = 3 # default: 3
N = 5 # default: 5
LIMIT = 1000 # default: 1000

# SOLUTION ####################################################################

def sum_divisible_by(n):
    """Returns the sum of natural numbers below LIMIT divisible by n."""
    return com.arithmetic_series(n, (LIMIT - 1) // n, n)


def solve():
    LCM = com.lcm(M, N)
    return sum_divisible_by(M) + sum_divisible_by(N) - sum_divisible_by(LCM)


if __name__ == '__main__':
    print(solve())
