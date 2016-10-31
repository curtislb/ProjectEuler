#!/usr/bin/env python3

"""problem_092.py

Problem 92: Square digit chains

A number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. What is most amazing is that EVERY starting number will eventually arrive
at 1 or 89.

How many starting numbers below LIMIT will arrive at 89?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 10**7 # default: 10**7

# SOLUTION ####################################################################

squares = [n*n for n in range(10)]

chains_to_89 = {
    1: False,
    89: True,
}


def has_chain_to_89(n):
    """Determines if the square digit chain from n will arrive at 89."""

    if n in chains_to_89:
        return chains_to_89[n]

    has_chain = has_chain_to_89(com.digit_function_sum(n, lambda x: squares[x]))
    chains_to_89[n] = has_chain
    return has_chain


def solve():
    total = 0
    for n in range(1, LIMIT):
        if has_chain_to_89(n):
            total += 1

    return total


if __name__ == '__main__':
    print(solve())
