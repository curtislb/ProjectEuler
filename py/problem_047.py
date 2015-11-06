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

import common as com

# PARAMETERS ##################################################################

CONSEC = 4 # default: 4
FACTORS = 4 # default: 4

# SOLUTION ####################################################################

# increment for max integer when generating primes
prime_step = 1000


def main():
    # precompute fixed range of prime numbers
    max_prime = prime_step
    primes = com.primes_up_to(max_prime)
    
    n = 2
    consec_count = 0
    while consec_count != CONSEC:
        # generate more prime numbers as needed
        if n > max_prime:
            max_prime += prime_step
            primes = com.primes_up_to(max_prime)
        
        # increment consecutive count if n has correct number of prime factors
        if com.count_prime_factors(n, primes) == FACTORS:
            consec_count += 1
        else:
            consec_count = 0
        
        n += 1
    
    return n - CONSEC


if __name__ == '__main__':
    print(main())
