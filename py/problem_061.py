#!/usr/bin/env python3

"""problem_061.py

Problem 61: Cyclical figurate numbers

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:

Triangle      P(3, n) = n(n+1)/2       1, 3, 6, 10, 15, ...
Square        P(4, n) = n^2            1, 4, 9, 16, 25, ...
Pentagonal    P(5, n) = n(3n - 1)/2    1, 5, 12, 22, 35, ...
Hexagonal     P(6, n) = n(2n - 1)      1, 6, 15, 28, 45, ...
Heptagonal    P(7, n) = n(5n - 3)/2    1, 7, 18, 34, 55, ...
Octagonal     P(8, n) = n(3n - 2)      1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three
interesting properties:

1. The set is cyclic, in that the last two digits of each number is the first 
two digits of the next number (including the last number with the first).

2. Each polygonal type: triangle (P(3, 127) = 8128), square (P(4, 91) = 8281),
and pentagonal (P(5, 44) = 2882), is represented by a different number in the
set.

3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and
octagonal, is represented by a different number in the set.
"""

__author__ = 'Curtis Belmonte'

from typing import List, Optional, Sequence, Set

import common.sequences as seqs


# PARAMETERS ##################################################################


# N/A


# SOLUTION ####################################################################


# A dict defined so that P[m](n) = P(m, n)
P = {
    3: seqs.triangular,
    4: lambda n: n**2,
    5: seqs.pentagonal,
    6: seqs.hexagonal,
    7: lambda n: n * (5 * n - 3) // 2,
    8: lambda n: n * (3 * n - 2),
}


def is_cyclic_6(num_list: Sequence[str]) -> bool:
    """Determines if num_list is cyclic and contains 6 values."""
    return len(num_list) == 6 and num_list[-1][-2:] == num_list[0][:2]


def find_cycle(p_strs: List[List[str]], found: List[str], k_used: Set[int])\
        -> Optional[Sequence[str]]:

    if is_cyclic_6(found):
        return found
    
    for k in range(5):
        if k not in k_used:
            for pk_str in p_strs[k]:
                if pk_str[:2] == found[-1][-2:]:
                    new_k_used = set(k_used)
                    new_k_used.add(k)
                    cycle = find_cycle(p_strs, found + [pk_str], new_k_used)
                    if cycle is not None and is_cyclic_6(cycle):
                        return cycle

    # failed to find a valid cycle
    return None


def solve() -> Optional[int]:
    p_strs: List[List[str]] = [[] for _ in range(6)]

    for k in range(3, 9):
        n = 1
        pk_max = 1
        while pk_max < 1000:
            n += 1
            pk_max = P[k](n)
        while pk_max < 10000:
            p_strs[k - 3].append(str(pk_max))
            n += 1
            pk_max = P[k](n)

    n = 0
    ans_list: Optional[Sequence[str]] = None
    while ans_list is None and n < len(p_strs[5]):
        p_strs_copy = []
        for pk_strs in p_strs:
            p_strs_copy.append(pk_strs[:])
        ans_list = find_cycle(p_strs_copy[:5][:], [p_strs[5][n]], set())
        n += 1

    if ans_list is not None:
        return sum(map(int, ans_list))

    return None


if __name__ == '__main__':
    print(solve())
