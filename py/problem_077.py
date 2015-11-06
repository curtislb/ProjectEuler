"""problem_077.py

Problem 77: Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over N
different ways?

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

N = 5000 # default: 5000

# SOLUTION ####################################################################

def solve():
    primes = list(com.primes_up_to(2 * N))
    n = 2
    while com.combination_sums(n, primes) <= N:
        n += 1
    return n


if __name__ == '__main__':
    print(solve())
