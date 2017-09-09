#!/usr/bin/env python3

"""problem_095.py

Problem 95: Amicable chains

The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the
sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the
proper divisors of 284 is 220, forming a chain of two numbers. For this reason,
220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we
form a chain of five numbers:

    12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element
exceeding MAX_ELEMENT.

Author: Curtis Belmonte
"""

import common.divisors as divs
import common.sequences as seqs


# PARAMETERS ##################################################################


MAX_ELEMENT = 10**6 # default: 10**6


# SOLUTION ####################################################################


def solve():
    # calculate all proper divisor sums in range
    divisor_sums = [0 if n < 2 else divs.sum_proper_divisors(n)
                    for n in range(MAX_ELEMENT + 1)]

    chain_lengths = {}
    values = range(2, MAX_ELEMENT + 1)

    def incr(n):
        return divisor_sums[n]

    def is_valid(n):
        return n <= MAX_ELEMENT

    # compute all chain lengths for terms in range
    seqs.compute_chain_lengths(chain_lengths, values, incr, is_valid)

    # find minimum member of max length chain
    max_length = max(chain_lengths.values())
    min_member = MAX_ELEMENT + 1
    for member, length in chain_lengths.items():
        if length == max_length and member < min_member:
            min_member = member

    return min_member


if __name__ == '__main__':
    print(solve())
