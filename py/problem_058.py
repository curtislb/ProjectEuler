#!/usr/bin/env python3

"""problem_058.py

Problem 58: Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square
spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right
diagonal, but what is more interesting is that 8 out of the 13 numbers lying
along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral
with side length 9 will be formed. If this process is continued, what is the
side length of the square spiral for which the ratio of primes along both
diagonals first falls below MIN_FRACTION?

Author: Curtis Belmonte
"""

import common.primes as prime


# PARAMETERS ##################################################################


MIN_FRACTION = 0.1 # default: 0.1


# SOLUTION ####################################################################


def solve() -> int:
    side = 1
    value = 1
    diag_count = 0
    prime_count = 0
    prime_frac = 1.0
    while prime_frac > MIN_FRACTION:
        # each layer has side length 2 greater than previous
        side += 2

        # count primes along diagonals of spiral
        side_sub_1 = side - 1
        for _ in range(4):
            # each diagonal is (side - 1) greater than previous
            value += side_sub_1

            # increment number of diagonal values and primes as necessary
            diag_count += 1
            if prime.is_prime(value):
                prime_count += 1

            prime_frac = prime_count / diag_count

    return side


if __name__ == '__main__':
    print(solve())
