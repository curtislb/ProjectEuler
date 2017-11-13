#!/usr/bin/env python3

"""problem_097.py

Problem 97: Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 2^6972593 - 1; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p - 1, have
been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433 × 2^7830457 + 1.

Find the last NUM_DIGITS digits of this prime number.

Author: Curtis Belmonte
"""

import common.arithmetic as arith


# PARAMETERS ##################################################################


NUM_DIGITS = 10 # default: 10


# SOLUTION ####################################################################


def solve() -> int:
    factor = 28433
    exponent = 7830457

    # use periodicity of power of 2 digits to decrease exponent
    period = 4 * 5**(NUM_DIGITS - 1)
    new_exponent = exponent - period
    while new_exponent > NUM_DIGITS:
        exponent = new_exponent
        new_exponent = exponent - period

    # calculate product, keeping only relevant digits
    mod_product = arith.mod_multiply(factor, 2**exponent, 10**NUM_DIGITS)
    return mod_product + 1


if __name__ == '__main__':
    print(solve())
