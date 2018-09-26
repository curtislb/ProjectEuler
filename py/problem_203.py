#!/usr/bin/env python3

"""problem_2 3.py

Problem 2 3: Squarefree Binomial Coefficients

The binomial coefficients nCk can be arranged in triangular form, Pascal's
triangle, like this:

                  1
                1   1
              1   2   1
            1   3   3   1
          1   4   6   4   1
        1   5  10  10   5   1
      1   6  15  20  15   6   1
    1   7  21  35  35  21   7   1
            ............

It can be seen that the first eight rows of Pascal's triangle contain twelve
distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n. Of
the twelve distinct numbers in the first eight rows of Pascal's triangle, all
except 4 and 20 are squarefree. The sum of the distinct squarefree numbers in
the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first NUM_ROWS rows of
Pascal's triangle.
"""

__author__ = 'Curtis Belmonte'

import itertools
import math

import common.primes as prime
import common.sequences as seqs


# PARAMETERS ##################################################################


NUM_ROWS = 51 # default: 51


# SOLUTION ####################################################################


def solve() -> int:
    # find distinct numbers in first NUM_ROWS rows, keeping track of maximum
    distinct_nums = set()
    max_num = 0
    for row in itertools.islice(seqs.generate_pascal_triangle(), NUM_ROWS):
        for i in range(int(math.ceil(len(row) / 2))):
            num = row[i]
            distinct_nums.add(num)
            if num > max_num:
                max_num = num

    # determine which distinct numbers are squarefree
    total = 0
    prime_squares = [p**2 for p in prime.primes_up_to(int(math.sqrt(max_num)))]
    for num in distinct_nums:
        is_squarefree = True
        for square in prime_squares:
            # stop checking for factors once they exceed num
            if square > num:
                break

            # if square is a factor, num is not squarefree
            if num % square == 0:
                is_squarefree = False
                break

        # add squarefree num to total
        if is_squarefree:
            total += num

    return total


if __name__ == '__main__':
    print(solve())
