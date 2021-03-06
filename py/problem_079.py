#!/usr/bin/env python3

"""problem_079.py

Problem 79: Passcode derivation

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file FILE_NAME contains a set of successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.
"""

__author__ = 'Curtis Belmonte'

from typing import Dict, List, Set, Tuple

import common.digits as digs
import common.fileio as fio


# PARAMETERS ##################################################################


FILE_NAME = '../input/079.txt'  # default: '../input/079.txt'


# SOLUTION ####################################################################


def solve() -> int:
    # keep track of all digits preceding other digits
    pre_digits: Dict[int, Set[int]] = {}
    attempts = fio.ints_from_file(FILE_NAME)
    for attempt in attempts:
        digits = digs.get_digits(attempt[0])
        for i, digit in enumerate(digits):
            # add digit to dict if we haven't seen it before
            if digit not in pre_digits:
                pre_digits[digit] = set()

            # add all of the preceding digits
            for j in range(i):
                pre_digits[digit].add(digits[j])

    # sort digits by how many other digits precede them
    ordering: List[Tuple[int, Set[int]]] = list(pre_digits.items())
    ordering.sort(key=(lambda x: len(x[1])))
    digits = [order[0] for order in ordering]

    return digs.join_digits(digits)


if __name__ == '__main__':
    print(solve())
