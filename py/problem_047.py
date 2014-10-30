"""problem_047.py

Problem 47: Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first CONSEC consecutive integers to have FACTORS distinct prime
factors. What is the first of these numbers?

@author: Curtis Belmonte
"""

import collections

import common

# PARAMETERS ##################################################################

CONSEC = 4 # default: 4
FACTORS = 4 # default: 4

# SOLUTION ####################################################################

if __name__ == '__main__':
    n = 2
    
    # create buffer of whether property holds for first CONSEC numbers from n
    buffer = collections.deque()
    for i in range(n, n + CONSEC):
        prime_factors = common.prime_factorization(n)
        buffer.append(len(prime_factors) == FACTORS)
    
    # append new element and pop previous, until property holds for all CONSEC
    while sum(buffer) != CONSEC:
        n += 1
        prime_factors = common.prime_factorization(n + (CONSEC - 1))
        buffer.popleft()
        buffer.append(len(prime_factors) == FACTORS)
    
    print(n)

