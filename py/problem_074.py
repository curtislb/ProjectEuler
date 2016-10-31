#!/usr/bin/env python3

"""problem_074.py

Problem 74: Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of
its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of
numbers that link back to 169; it turns out that there are only three such
loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get
stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest
non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below MAX_START, contain exactly
TARGET_LEN non-repeating terms?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

MAX_START = 10**6 # default: 10**6
TARGET_LEN = 60 # default: 60

# SOLUTION ####################################################################

chain_lengths = {
    # factorions: n (-> n)
    1: 1,
    2: 1,
    145: 1,
    40585: 1,

    # 169 -> 363601 -> 1454 (-> 169)
    169: 3,
    363601: 3,
    1454: 3,

    # 871 -> 45361 (-> 871)
    871: 2,
    45361: 2,

    # 872 -> 45362 (-> 872)
    872: 2,
    45362: 2,
}


def get_chain_length(n):
    """Returns the length of the digit factorial chain starting with n."""

    if n in chain_lengths:
        return chain_lengths[n]

    length = 1 + get_chain_length(com.digit_function_sum(n, com.factorial))
    chain_lengths[n] = length
    return length


def solve():
    # compute all chain lengths
    for n in range(3, MAX_START + 1):
        if n not in chain_lengths:
            chain_lengths[n] = get_chain_length(n)

    # count number of chains of the correct length
    total = 0
    for length in chain_lengths.values():
        if length == TARGET_LEN:
            total += 1

    return total


if __name__ == '__main__':
    print(solve())
