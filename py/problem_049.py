#!/usr/bin/env python3

"""problem_049.py

Problem 49: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

__author__ = 'Curtis Belmonte'

from typing import List, Optional

import common.arrays as arrs
import common.primes as prime


# PARAMETERS ##################################################################


# N/A


# SOLUTION ####################################################################


def solve() -> Optional[int]:
    # generate all four-digit primes
    primes = set(filter((lambda x: x > 999), prime.primes_up_to(9999)))
    
    # remove sequence from problem description
    primes.remove(1487)
    primes.remove(4817)
    primes.remove(8147)
    
    # test all permutation groups in primes
    while len(primes) > 2:
        first = None
        perms: List[int] = []
        
        # find all permutations of first prime in primes
        for p in primes:
            if first is None:
                first = str(p)
                perms.append(p)
            elif arrs.is_permutation(first, str(p)):
                perms.append(p)
        
        # check if any three prime permutations form arithmetic sequence
        if len(perms) > 2:
            perms.sort()
            for i in range(len(perms)):
                for j in range(i + 1, len(perms)):
                    for k in range(j + 1, len(perms)):
                        if perms[j] - perms[i] == perms[k] - perms[j]:
                            return int(''.join(
                                map(str, [perms[i], perms[j], perms[k]])))
        
        # remove permutation group from primes
        for n in perms:
            primes.remove(n)

    # failed to find solution
    return None


if __name__ == '__main__':
    print(solve())
