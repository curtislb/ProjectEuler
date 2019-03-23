#!/usr/bin/env python3

"""problem_008.py

Problem 8: Largest product in a series

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the N adjacent digits in the number contained in the file FILE_NAME that
have the greatest product. What is the value of this product?
"""

__author__ = 'Curtis Belmonte'


# PARAMETERS ##################################################################


N = 13  # default: 13

FILE_NAME = '../input/008.txt'  # default: '../input/008.txt'


# SOLUTION ####################################################################


def solve() -> int:
    with open(FILE_NAME) as input_file:
        # read number from input file
        num_str = ''.join(line.rstrip() for line in input_file)
        
        num_zeros = 0  # number of zeros in the current product
        product = 1  # current product of N digits (ignoring zeros)
        max_product = 0  # largest product of N digits
    
        # compute product of initial N digits
        i = 0
        while i < N:
            digit = int(num_str[i])
            if digit == 0:
                num_zeros += 1
            else:
                product *= digit
            i += 1
    
        # set as initial max product if it contains no 0 factors
        if num_zeros == 0:
            max_product = product
    
        # compute products of remaining sets of N digits
        digit_count = len(num_str)
        while i < digit_count:
            # remove leftmost digit from product
            left_digit = int(num_str[i - N])
            if left_digit == 0:
                num_zeros -= 1
            else:
                product //= left_digit
    
            # add new rightmost digit to product
            right_digit = int(num_str[i])
            if right_digit == 0:
                num_zeros += 1
            else:
                product *= right_digit
    
            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product
    
            i += 1
        
        return max_product


if __name__ == '__main__':
    print(solve())
