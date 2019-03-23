#!/usr/bin/env python3

"""problem_013.py

Problem 13: Large sum

Work out the first D digits of the sum of the numbers contained in the file
FILE_NAME (all of which have the same number of digits).
"""

__author__ = 'Curtis Belmonte'


# PARAMETERS ##################################################################


D = 10  # default: 10

FILE_NAME = '../input/013.txt'  # default: '../input/013.txt'


# SOLUTION ####################################################################


def solve() -> int:
    total = 0
    with open(FILE_NAME) as input_file:
        for line in input_file:
            total += int(line.rstrip())
    return int(str(total)[:D])


if __name__ == '__main__':
    print(solve())
