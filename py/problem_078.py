"""problem_078.py

Problem 78: Coin partitions

Let p(n) represent the number of different ways in which n coins can be
separated into piles. For example, five coins can be separated into piles in
exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by DIVISOR.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

DIVISOR = 1000000 # Default: 1000000

# SOLUTION ####################################################################

def solve():
    n = 2800
    p = com.combination_sums(n, list(range(1, n + 1)))
    while p % DIVISOR != 0:
        n += 1
        p = com.combination_sums(n, list(range(1, n + 1)))
    return n


if __name__ == '__main__':
    print(solve())
