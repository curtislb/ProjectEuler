"""problem_099.py

Problem 99: Largest exponential

Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using INPUT_FILE, a text file containing lines with a base/exponent pair on
each line, determine which line number has the greatest numerical value.

Author: Curtis Belmonte
"""

import common as com

import math

# PARAMETERS ##################################################################

INPUT_FILE = '../input/099.txt' # default: '../input/099.txt'

# SOLUTION ####################################################################

def solve():
    max_line = None
    max_value = -com.INFINITY
    base_exp_pairs = com.numbers_from_file(INPUT_FILE, sep=',')

    # compare exponent * log(base) for all pairs
    for i, pair in enumerate(base_exp_pairs):
        base, exponent = pair
        value = exponent * math.log(base)
        if value > max_value:
            max_line = i
            max_value = value

    return max_line + 1


if __name__ == '__main__':
    print(solve())
