"""problem_007.py

Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the Nth prime number?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

N = 10001 # default: 10001

# SOLUTION ####################################################################

if __name__ == '__main__':
    print(common.prime(N))
