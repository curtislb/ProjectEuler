#!/usr/bin/env python3

"""problem_014.py

Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under LIMIT, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above LIMIT.

Author: Curtis Belmonte
"""

import common as com


# PARAMETERS ##################################################################


LIMIT = 1000000 # default: 1000000


# SOLUTION ####################################################################


collatz_lengths = {}


def collatz_length(n):
    """Returns the length of the Collatz sequence, starting from n."""
    m = n
    length = 0
    while m != 1:
        # break out early if solution already exists
        if m in collatz_lengths:
            length += collatz_lengths[m]
            break

        # compute next step in sequence
        else:
            length += 1
            m = com.collatz_step(m)

    # memoize answer and return
    collatz_lengths[n] = length
    return length


def solve():
    best_num = 0
    best_length = 0
    for n in range(2, LIMIT):
        length = collatz_length(n)
        if length > best_length:
            best_num = n
            best_length = length
    return best_num


if __name__ == '__main__':
    print(solve())
