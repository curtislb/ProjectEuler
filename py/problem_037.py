#!/usr/bin/env python3

"""problem_037.py

Problem 37: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the first MAX_COUNT of the only eleven primes that are both
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

MAX_COUNT = 11 # default: 11

# SOLUTION ####################################################################

@com.memoized
def is_prime(n):
    """Memoized wrapper for the com.is_prime function."""
    return com.is_prime(n)
    

def solve():
    total = 0
    
    # search for truncatable primes until MAX_COUNT are found
    count = 0
    m = 5
    while count < MAX_COUNT:
        # search for candidate prime numbers m < n around multiples of 6
        m += 6
        n = m + 2
        
        # check if m itself is prime before testing truncations
        if is_prime(m):
            # check if m is a right truncatable prime
            right_trunc_prime = True
            for truncation in com.digit_truncations_right(m):
                if truncation == m:
                    continue

                if not is_prime(truncation):
                    right_trunc_prime = False
                    break
            
            # if necessary, check if m is also a left truncatable prime
            if right_trunc_prime:
                left_trunc_prime = True
                for truncation in com.digit_truncations_left(m):
                    if truncation == m:
                        continue

                    if not is_prime(truncation):
                        left_trunc_prime = False
                        break
                
                # if m is both a left and right truncatable prime, add to total
                if left_trunc_prime:
                    count += 1
                    total += m
        
        # check if n itself is prime before testing truncations
        if is_prime(n):
            # check if n is a right truncatable prime
            right_trunc_prime = True
            for truncation in com.digit_truncations_right(n):
                if truncation == n:
                    continue

                if not is_prime(truncation):
                    right_trunc_prime = False
                    break
            
            # if necessary, check if n is also a left truncatable prime
            if right_trunc_prime:
                left_trunc_prime = True
                for truncation in com.digit_truncations_left(n):
                    if truncation == n:
                        continue

                    if not is_prime(truncation):
                        left_trunc_prime = False
                        break
                
                # if n is both a left and right truncatable prime, add to total
                if left_trunc_prime:
                    count += 1
                    total += n
    
    return total


if __name__ == '__main__':
    print(solve())
