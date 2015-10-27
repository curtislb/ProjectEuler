"""problem_046.py

Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and FACTOR times a square?

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

FACTOR = 2 # default: 2

# SOLUTION ####################################################################

def main():
    n = 7
    answer = -1
    
    # test all odd composite numbers for property
    while answer == -1:
        n += 2
        
        # skip number if it is not composite
        if com.is_prime(n):
            continue
        
        # check if the given number is a counterexample
        is_counterexample = True
        primes = com.primes_up_to(n)
        for prime in primes:
            # test property for each prime
            diff = n - prime
            if diff % FACTOR == 0 and com.is_perfect_square(diff // FACTOR):
                is_counterexample = False
                break
        
        # if property doesn't hold for this n, set it as answer
        if is_counterexample:
            answer = n
            
    return answer


if __name__ == '__main__':
    print(main())
