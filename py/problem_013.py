#!/usr/bin/env python3

"""problem_013.py

Problem 13: Large sum

Work out the first D digits of the sum of the numbers contained in the file
INPUT_FILE (all of which have the same number of digits).

Author: Curtis Belmonte
"""

# import common as com

# PARAMETERS ##################################################################

D = 10 # default: 10
INPUT_FILE = '../input/013.txt' # default: '../input/013.txt'

# SOLUTION ####################################################################

def solve():
    total = 0
    with open(INPUT_FILE) as f:
        for line in f:
            total += int(line.rstrip())
    return int(str(total)[:D])


if __name__ == '__main__':
    print(solve())
