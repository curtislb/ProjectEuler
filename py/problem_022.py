#!/usr/bin/env python3

"""problem_022.py

Problem 22: Names scores

Using INPUT_FILE, a large text file containing many first names, begin by
sorting it into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the list to
obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

Author: Curtis Belmonte
"""

import heapq

import common.alphabet as alpha
import common.fileio as fio


# PARAMETERS ##################################################################


INPUT_FILE = '../input/022.txt' # default: '../input/022.txt'


# SOLUTION ####################################################################


def name_score(name, position):
    """Returns the score for name in position when sorted alphabetically."""
    score = sum(map(alpha.alpha_index_upper, name))
    return position * score


def solve():
    # heap sort names from input file
    names = fio.strings_from_file(INPUT_FILE)
    heapq.heapify(names)
    
    # sum up the name scores for all names in alphabetical order
    total = 0
    for i in range(1, len(names) + 1):
        total += name_score(heapq.heappop(names), i)
    
    return total


if __name__ == '__main__':
    print(solve())
