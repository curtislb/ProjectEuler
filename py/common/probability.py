#!/usr/bin/env python3

"""probability.py

Functions for making random choices and computing probabilities.
"""

__author__ = 'Curtis Belmonte'

import random
from fractions import Fraction
from typing import Sequence

import common.combinatorics as comb
from common.typex import Real, T


def choose_weighted_random(values: Sequence[T], probs: Sequence[Real]) -> T:
    """Returns a value at random from values, weighted by probs.

    In order for a proper weighted selection to be made, the sum of the values
    in probs must be equal to 1.
    """

    # generate a random float in [0, 1)
    x = random.random()

    # search for corresponding index in values
    i = 0
    cum_prob = probs[0]
    while x > cum_prob:
        i += 1
        cum_prob += probs[i]

    return values[i]


def dice_probability(x: int, n: int, s: int) -> Fraction:
    """Returns the probability of rolling a value of x with n s-sided dice."""
    total = 0
    sign = 1
    for k in range((x - n) // s + 1):
        total += sign * comb.choose(n, k) * comb.choose(x - s * k - 1, n - 1)
        sign = -sign
    return Fraction(total, s**n)
