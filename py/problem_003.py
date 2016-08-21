#!/usr/bin/env python3

"""problem_003.py

Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number N?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

N = 600851475143 # default: 600851475143

# SOLUTION ####################################################################

def solve():
    return com.prime_factorization(N)[-1][0]


if __name__ == '__main__':
    print(solve())
