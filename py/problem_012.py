"""problem_012.py

Problem 12: Highly divisible triangular number

The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten
terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over D divisors?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

D = 500 # default: 500

# SOLUTION ####################################################################

@common.memoized
def count_divisors(n):
    """Memoized wrapper for the common.count_divisors function."""
    return common.count_divisors(n)


def count_triangle_divisors(n):
    """Returns the number of divisors of the triangle number n*(n + 1)/2."""
    
    # because n and n + 1 are necessarily co-prime, sum their divisor counts
    if n % 2 == 0:
        # n component of triangle number is evenly divisible by 2
        return count_divisors(n // 2) * count_divisors(n + 1)
    else:
        # n + 1 component of triangle number is evenly divisible by 2
        return count_divisors(n) * count_divisors((n + 1) // 2);
    

if __name__ == '__main__':
    n = 1
    while count_triangle_divisors(n) < D:
        n += 1
    
    print(common.triangle(n))
