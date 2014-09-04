"""problem_027.py

Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

    n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible
by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula n² − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79
and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < MAX_A and |b| < MAX_B

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = START_N.

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

MAX_A = 1000 # default: 1000
MAX_B = 1000 # default: 1000
START_N = 0 # default: 0

# SOLUTION ####################################################################

@common.memoized
def is_prime(n):
    """Memoized wrapper for the common.is_prime function."""
    return common.is_prime(n)


if __name__ == '__main__':
    # search for best a and b from -MAX + 1 to MAX - 1
    best_product = None
    best_streak = -1
    for a in range(-MAX_A + 1, MAX_A):
        for b in range(-MAX_B + 1, MAX_B):
            # count number of primes generated for subsequent n
            n = START_N
            result = (n * n) + (a * n) + b
            while is_prime(result):
                # advance result to that generated by next value of n
                result += (2 * n) + 1 + a
                n += 1
            
            # update best product and consecutive prime count if necessary
            streak = n - START_N + 1
            if streak > best_streak:
                best_product = a * b
                best_streak = streak
    
    print(best_product)