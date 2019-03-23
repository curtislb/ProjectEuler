#!/usr/bin/env python3

"""problem_205.py

Problem 205: Dice Game

Peter has P_NUM_DICE dice, each with faces numbered 1, 2, 3, ..., P_NUM_SIDES.
Colin has C_NUM_DICE dice, each with faces numbered 1, 2, 3, ..., C_NUM_SIDES.

Peter and Colin roll their dice and compare totals: the highest total wins. The
result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer
rounded to PRECISION decimal places.
"""

__author__ = 'Curtis Belmonte'

import common.digits as digs
import common.probability as prob


# PARAMETERS ##################################################################


P_NUM_DICE = 9  # default: 9

P_NUM_SIDES = 4  # default: 4

C_NUM_DICE = 6  # default: 6

C_NUM_SIDES = 6  # default: 6

PRECISION = 7  # default: 7


# SOLUTION ####################################################################


def solve() -> int:
    # calculate total outcomes and min/max roll for each player
    p_outcomes = P_NUM_SIDES**P_NUM_DICE
    c_outcomes = C_NUM_SIDES**C_NUM_DICE
    min_roll = min(P_NUM_DICE, C_NUM_DICE)
    max_roll = max(P_NUM_SIDES * P_NUM_DICE, C_NUM_SIDES * C_NUM_DICE)

    # count ways each player can roll values in [min_roll, max_roll]
    p_rolls = []
    c_rolls = []
    for roll in range(min_roll, max_roll + 1):
        p = prob.dice_probability(roll, P_NUM_DICE, P_NUM_SIDES) * p_outcomes
        c = prob.dice_probability(roll, C_NUM_DICE, C_NUM_SIDES) * c_outcomes
        p_rolls.append(int(p))
        c_rolls.append(int(c))

    # calculate combinations of outcomes where P > C
    win_count = 0
    roll_count = max_roll + 1 - min_roll
    for i in range(roll_count - 1):
        for j in range(i + 1, roll_count):
            win_count += c_rolls[i] * p_rolls[j]

    # format and return probability that P > C
    win_prob = win_count / (p_outcomes * c_outcomes)
    return digs.decimal_digits(win_prob, PRECISION)


if __name__ == '__main__':
    print('0.{0:d}'.format(solve()))
