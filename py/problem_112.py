#!/usr/bin/env python3

"""problem_112.py

Problem 112: Bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over
half of the numbers below one-thousand (525) are bouncy. In fact, the least
number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we
reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly
BOUNCY_PERCENTAGE%.
"""

__author__ = 'Curtis Belmonte'

import common.digits as digs


# PARAMETERS ##################################################################


BOUNCY_PERCENTAGE = 99  # default: 99


# SOLUTION ####################################################################


def solve() -> int:
    n = 1
    adjusted_count = 0  # 100 * (bouncy numbers)
    adjusted_total = BOUNCY_PERCENTAGE  # BOUNCY_PERCENTAGE * (total numbers)

    # find first number for which ratio is exactly BOUNCY_PERCENTAGE%
    while adjusted_count != adjusted_total:
        n += 1
        if digs.is_bouncy(n):
            adjusted_count += 100
        adjusted_total += BOUNCY_PERCENTAGE

    return n


if __name__ == '__main__':
    print(solve())
