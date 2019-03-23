#!/usr/bin/env python3

"""problem_084.py

Problem 84: Monopoly odds

In the game, Monopoly, the standard board is set up in the following way:

    GO  A1  CC1 A2  T1  R1  B1  CH1 B2  B3  JAIL
    H2                                      C1
    T2                                      U1
    H1                                      C2
    CH3                                     C3
    R4                                      R2
    G3                                      D1
    CC3                                     CC2
    G2                                      D2
    G1                                      D3
    G2J F3  U2  F2  F1  R3  E3  E2  CH2 E1  FP

A player starts on the GO square and adds the scores on two 6-sided dice to
determine the number of squares they advance in a clockwise direction. Without
any further rules we would expect to visit each square with equal probability:
2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH
(chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player
to go directly to jail, if a player rolls three consecutive doubles, they do
not advance the result of their 3rd roll. Instead they proceed directly to
jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player
lands on CC or CH they take a card from the top of the respective pile and,
after following the instructions, it is returned to the bottom of the pile.
There are sixteen cards in each pile, but for the purpose of this problem we
are only concerned with cards that order a movement; any instruction not
concerned with movement will be ignored and the player will remain on the
CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL

Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.

The heart of this problem concerns the likelihood of visiting a particular
square. That is, the probability of finishing at that square after a roll. For
this reason it should be clear that, with the exception of G2J for which the
probability of finishing on it is zero, the CH squares will have the lowest
probabilities, as 5/8 request a movement to another square, and it is the final
square that the player finishes at on each roll that we are interested in. We
shall make no distinction between "Just Visiting" and being sent to JAIL, and
we shall also ignore the rule about requiring a double to "get out of jail",
assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can
concatenate these two-digit numbers to produce strings that correspond with
sets of squares.

Statistically it can be shown that the three most popular squares, in order,
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square
00. So these three most popular squares can be listed with the six-digit modal
string: 102400.

If, instead of using two 6-sided dice, NUM_DICE NUM_SIDES-sided dice are used,
find the six-digit modal string.
"""

__author__ = 'Curtis Belmonte'

from collections import Counter
from fractions import Fraction
from typing import Counter as CounterT, List

import common.probability as prob
from common.games import GameBoard
from common.utility import Real

# PARAMETERS ##################################################################


NUM_DICE = 2  # default: 2

NUM_SIDES = 4  # default: 4


# SOLUTION ####################################################################


# A mapping from each space type to board positions of this type
space_type_map: GameBoard.SpaceTypeMap = {
    'GO': [0],
    'A': [1, 3],
    'CC': [2, 17, 33],
    'T': [4, 38],
    'R': [5, 15, 25, 35],
    'B': [6, 8, 9],
    'CH': [7, 22, 36],
    'JAIL': [10],
    'C': [11, 13, 14],
    'U': [12, 28],
    'D': [16, 18, 19],
    'FP': [20],
    'E': [21, 23, 24],
    'F': [26, 27, 29],
    'G2J': [30],
    'G': [31, 32, 34],
    'H': [37, 39],
}

# All special move rules for different space types
move_rules: GameBoard.MoveRules = {
    'G2J': {
        ('JAIL', 1): 1,
    },
    'CC': {
        ('GO', 1): Fraction(1, 16),
        ('JAIL', 1): Fraction(1, 16),
    },
    'CH': {
        ('GO', 1): Fraction(1, 16),
        ('JAIL', 1): Fraction(1, 16),
        ('C', 1): Fraction(1, 16),
        ('E', 3): Fraction(1, 16),
        ('H', 2): Fraction(1, 16),
        ('R', 1): Fraction(1, 16),
        'R': Fraction(1, 8),
        'U': Fraction(1, 16),
        -3: Fraction(1, 16),
    },
}


def solve() -> int:
    # set up the game board
    board = GameBoard(space_type_map, move_rules)

    # precompute possible roll values and their probabilities
    roll_values: List[int] = []
    roll_probs: List[Real] = []
    for roll in range(NUM_DICE, NUM_DICE * NUM_SIDES + 1):
        roll_values.append(roll)
        roll_probs.append(prob.dice_probability(roll, NUM_DICE, NUM_SIDES))
    
    # simulate many moves, keeping track of most popular spaces
    counts: CounterT[int] = Counter()
    position = 0
    for _ in range(2 * 10**5):
        roll = prob.choose_weighted_random(roll_values, roll_probs)
        position = board.move(position, roll)
        counts[position] += 1

    # return modal string as a decimal integer
    return int(
        ''.join('{0:02d}'.format(key) for key, _ in counts.most_common(3)),
        10)


if __name__ == '__main__':
    print('{0:06d}'.format(solve()))
