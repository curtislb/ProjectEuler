#!/usr/bin/env python3

"""problem_493.py

Problem 493: Under The Rainbow

NUM_BALLS colored balls are placed in an urn, NUM_BALLS/NUM_COLORS for each of
NUM_COLORS different colors.

What is the expected number of distinct colors in NUM_DRAWS randomly picked
balls?

Give your answer with PRECISION digits after the decimal point.

Author: Curtis Belmonte
"""

import common as com

from fractions import Fraction

# PARAMETERS ##################################################################

NUM_BALLS = 70 # default: 70

NUM_COLORS = 7 # default: 7

NUM_DRAWS = 20 # default: 20

# SOLUTION ####################################################################

def solve():
    a = com.choose(NUM_BALLS - (NUM_BALLS // NUM_COLORS), NUM_DRAWS)
    b = com.choose(NUM_BALLS, NUM_DRAWS)
    expected_value = NUM_COLORS * (1 - Fraction(a, b))
    return int('{:.9f}'.format(float(expected_value)).replace('.', ''))


if __name__ == '__main__':
    solution_string = str(solve())
    print('{}.{}'.format(solution_string[0], solution_string[1:]))