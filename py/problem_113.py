#!/usr/bin/env python3

"""problem_113.py

Problem 113: [Title]

Working from left-to-right if no digit is exceeded by the digit to its left it
is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a
decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a
"bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that
there are only 12951 numbers below one-million that are not bouncy and only
277032 non-bouncy numbers below 10^10.

How many numbers below 10^MAX_DIGITS are not bouncy?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

MAX_DIGITS = 100 # default: 100

# SOLUTION ####################################################################

def next_digit_counts(counts, num_digits):
    """Returns the next iteration of the counts matrix with a digit prepended.

    counts      A 9x3 matrix with the number of increasing, decreasing, and
                bouncy numbers (in that order) that begin with each digit from
                1 to 9 and consist of num_digits digits.

    num_digits  The length of numbers represented by the counts matrix.
    """

    new_counts = [[0] * 3 for __ in range(9)]

    for x in range(9):
        # count cases where next digit is 0
        new_counts[x][1] += 1 # case x0+
        for i in range(num_digits - 1):
            # case x0+[1-9]0*
            new_counts[x][2] += 9 * 10**i

        # count cases where x > y
        for y in range(x):
            new_counts[x][1] += counts[y][1] + 1
            new_counts[x][2] += counts[y][0] + counts[y][2]

        # count cases where x == y
        new_counts[x][0] += counts[x][0]
        new_counts[x][1] += counts[x][1]
        new_counts[x][2] += counts[x][2]

        # count cases where x < y
        for y in range(x + 1, 9):
            new_counts[x][0] += counts[y][0] + 1
            new_counts[x][2] += counts[y][1] + counts[y][2]

    return new_counts


def solve():
    # iterate counts for each digit, keeping track of bouncy numbers
    counts = [[0] * 3 for __ in range(9)]
    bouncy_count = 0
    for i in range(1, MAX_DIGITS):
        counts = next_digit_counts(counts, i)
        bouncy_count += sum([x_counts[2] for x_counts in counts])

    # calculate and return non-bouncy count
    return 10**MAX_DIGITS - 1 - bouncy_count


if __name__ == '__main__':
    print(solve())
