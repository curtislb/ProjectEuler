#!/usr/bin/env python3

"""problem_001.py

Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of M or N below LIMIT.

Author: Curtis Belmonte
"""

import common.divisors as divs
import common.sequences as seqs


# PARAMETERS ##################################################################


M = 3 # default: 3

N = 5 # default: 5

LIMIT = 1000 # default: 1000


# SOLUTION ####################################################################


def sum_divisible_by(n):
    """Returns the sum of natural numbers below LIMIT divisible by n."""
    return seqs.arithmetic_series(n, (LIMIT - 1) // n, n)


def solve():
    m_sum = sum_divisible_by(M)
    n_sum = sum_divisible_by(N)
    lcm_sum = sum_divisible_by(divs.lcm(M, N))
    return m_sum + n_sum - lcm_sum


if __name__ == '__main__':
    print(solve())
