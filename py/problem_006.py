#!/usr/bin/env python3

"""problem_006.py

Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    
The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first N natural
numbers and the square of the sum.

Author: Curtis Belmonte
"""

import common.sequences as seqs


# PARAMETERS ##################################################################


N = 100 # default: 100


# SOLUTION ####################################################################


def solve() -> int:
    return seqs.triangular(N)**2 - seqs.sum_of_squares(N)


if __name__ == '__main__':
    print(solve())
