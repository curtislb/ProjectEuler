"""problem_021.py

Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under LIMIT.

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 10000 # default: 10000

# SOLUTION ####################################################################

def solve():
    total = 0
    
    # search for amicable pairs (m, n) below LIMIT
    for m in range(2, LIMIT):
        n = com.sum_proper_divisors(m)
        
        # do m and n meet conditions of amicable pair with m < n < LIMIT
        if m < n and n < LIMIT and com.sum_proper_divisors(n) == m:
            total += m + n
    
    return total


if __name__ == '__main__':
    print(solve())
