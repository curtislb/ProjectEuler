#!/usr/bin/env python3

"""problem_032.py

Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through MAX_DIGIT pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.

Author: Curtis Belmonte
"""

from typing import *

import common.arrays as arrs
import common.digits as digs


# PARAMETERS ##################################################################


MAX_DIGIT = 9 # default: 9


# SOLUTION ####################################################################


# A 1 to MAX_DIGIT pandigital string
pandigit_string = digs.pandigital_string(1, MAX_DIGIT)


def max_multiplicand(digit_count: int) -> int:
    """Returns the maximum possible multiplicand with digit_count digits that
    could satisfy the problem conditions."""
    return int(pandigit_string[digit_count::-1])


def min_multiplicand(digit_count: int) -> int:
    """Returns the minimum possible multiplicand with digit_count digits that
    could satisfy the problem conditions."""
    return int(pandigit_string[:digit_count])


def solve() -> int:
    # determine possible numbers of digits for multiplicands a and b, a <= b
    candidates = [] # type: List[Tuple[int, int]]
    for a_digits in range(1, MAX_DIGIT + 1):
        for b_digits in range(a_digits, MAX_DIGIT + 1):
            # compute min and max products of a and b
            min_a = min_multiplicand(a_digits)
            max_a = max_multiplicand(a_digits)
            min_b = min_multiplicand(b_digits)
            max_b = max_multiplicand(b_digits)
            min_digits = digs.count_digits(min_a * min_b)
            max_digits = digs.count_digits(max_a * max_b)
            
            # check if target digit count is within min and max product range
            target_digits = MAX_DIGIT - a_digits - b_digits
            if min_digits <= target_digits <= max_digits:
                candidates.append((a_digits, b_digits))
    
    # search for products that are 1 to n pandigital with their multiplicands
    total = 0
    products = set() # type: Set[int]
    for a_digits, b_digits in candidates:
        # compute min and max values of a and b
        min_a = min_multiplicand(a_digits)
        max_a = max_multiplicand(a_digits)
        min_b = min_multiplicand(b_digits)
        max_b = max_multiplicand(b_digits)
        
        # try all possible combinations of multiplicands a and b
        for a in range(max(min_a, 2), max_a + 1):
            for b in range(max(min_b, 2), max_b + 1):
                product = a * b
                # check if product has already been found
                if product not in products:
                    # check if product is pandigital with its multiplicands
                    digit_string = str(a) + str(b) + str(product)
                    if arrs.is_permutation(digit_string, pandigit_string):
                        products.add(product)
                        total += product
    
    return total


if __name__ == '__main__':
    print(solve())
