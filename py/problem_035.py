"""problem_035.py

Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below LIMIT?

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 1000000 # default: 1000000

# SOLUTION ####################################################################

def main():
    # search for circular primes from 2 to LIMIT - 1
    count = 0
    tested_rotations = set()
    for n in range(2, LIMIT):
        # check if the digit rotations of n have already been seen
        if n not in tested_rotations:
            # mark all digit rotations of n as seen
            rotations = set(com.digit_rotations(n))
            for rotation in rotations:
                tested_rotations.add(rotation)
            
            # check if all digit rotations of n are prime
            all_rotations_prime = True
            for rotation in rotations:
                if not com.is_prime(rotation):
                    all_rotations_prime = False
                    break
            
            # if all rotations of n are prime, count each as a circular prime
            if all_rotations_prime:
                count += len(rotations)
    
    return count


if __name__ == '__main__':
    print(main())
    