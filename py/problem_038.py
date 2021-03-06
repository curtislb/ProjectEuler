#!/usr/bin/env python3

"""problem_038.py

Problem 38: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1, 2, ... , n) where n > 1?
"""

__author__ = 'Curtis Belmonte'

import itertools

import common.arrays as arrs
import common.digits as digs


# PARAMETERS ##################################################################


# N/A


# SOLUTION ####################################################################


def solve() -> int:
    max_num = 0
    pandigit_string = digs.pandigital_string(1)
    
    # try all starting numbers with up to 4 digits
    for num_digits in range(1, 5):
        # try all permutations of count_digits digits from pandigital string
        for permutation in itertools.permutations(pandigit_string, num_digits):
            # form the starting number by joining the string digits
            start_num = int(''.join(permutation))
            
            # search for n that gives the correct number of digits
            n = 2
            product_str = str(start_num) + str(start_num * 2)
            while len(product_str) < 9:
                # concatenate each new product to product_str
                n += 1
                product_str += str(start_num * n)
            
            # check if number of digits is greater than pandigital string
            if len(product_str) > 9:
                continue
            
            # check if concatenated products are 1 to 9 pandigital
            if arrs.is_permutation(product_str, pandigit_string):
                num = int(product_str)
                
                # set new maximum pandigital number if necessart
                if num > max_num:
                    max_num = num
     
    return max_num


if __name__ == '__main__':
    print(solve())
