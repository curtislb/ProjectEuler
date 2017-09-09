#!/usr/bin/env python3

"""problem_179.py

Problem 179: Consecutive positive divisors

Find the number of integers 1 < n < LIMIT, for which n and n + 1 have the same
number of positive divisors. For example, 14 has the positive divisors 1, 2, 7,
14 while 15 has 1, 3, 5, 15.

Author: Curtis Belmonte
"""

import common.divisors as divs


# PARAMETERS ##################################################################


LIMIT = 10**7 # default: 10**7


# SOLUTION ####################################################################


def solve():
    divisor_counts = divs.count_divisors_up_to(LIMIT)
    
    # check consecutive numbers for equal divisor counts
    count = 0
    for n in range(2, LIMIT):
        if divisor_counts[n] == divisor_counts[n + 1]:
            count += 1

    return count


if __name__ == '__main__':
    print(solve())
