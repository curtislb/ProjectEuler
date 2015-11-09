"""problem_010.py

Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below LIMIT.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 2000000 # default: 2000000

# SOLUTION ####################################################################

def solve():
    return sum(com.primes_up_to(LIMIT - 1))


if __name__ == '__main__':
    print(solve())
