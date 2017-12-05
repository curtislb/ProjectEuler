#!/usr/bin/env python3

"""problem_011.py

Problem 11: Largest product in a grid

In the 20×20 grid below, four numbers along a diagonal line have been marked
with parentheses.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10(26)38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95(63)94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17(78)78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35(14)00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of N adjacent numbers in the same direction (up,
down, left, right, or diagonally) in the grid contained in the file INPUT_FILE?
"""

__author__ = 'Curtis Belmonte'

import common.fileio as fio


# PARAMETERS ##################################################################

N = 4 # default: 4

INPUT_FILE = '../input/011.txt' # default: '../input/011.txt'


# SOLUTION ####################################################################


def solve() -> int:
    # read the matrix from the input file
    matrix = list(fio.ints_from_file(INPUT_FILE))
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    max_product = 0

    # compute all row products
    for i in range(num_rows):
        num_zeros = 0
        product = 1

        # compute product of initial N digits in row
        j = 0
        while j < N:
            if matrix[i][j] == 0:
                num_zeros += 1
            else:
                product *= matrix[i][j]
            j += 1

        # set as initial max product if it contains no 0 factors
        if num_zeros == 0:
            max_product = product

        # compute products of remaining sets of N digits in row
        while j < num_cols:
            # remove leftmost digit from product
            if matrix[i][j - N] == 0:
                num_zeros -= 1
            else:
                product //= matrix[i][j - N]

            # add new rightmost digit to product
            if matrix[i][j] == 0:
                num_zeros += 1
            else:
                product *= matrix[i][j]

            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product

            j += 1

    # compute all column products
    for i in range(num_cols):
        num_zeros = 0
        product = 1

        # compute product of initial N digits in column
        j = 0
        while j < N:
            if matrix[j][i] == 0:
                num_zeros += 1
            else:
                product *= matrix[j][i]
            j += 1

        # set as new max product if necessary
        if num_zeros == 0 and product > max_product:
            max_product = product

        # compute products of remaining sets of N digits in column
        while j < num_rows:
            # remove top digit from product
            if matrix[j - N][i] == 0:
                num_zeros -= 1
            else:
                product //= matrix[j - N][i]

            # add new bottom digit to product
            if matrix[j][i] == 0:
                num_zeros += 1
            else:
                product *= matrix[j][i]

            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product

            j += 1

    # compute / diagonal products starting along top row
    for i in range(N - 1, num_cols):
        num_zeros = 0
        product = 1

        # compute product of initial N digits along diagonal
        j = 0
        while j < N:
            if matrix[j][i - j] == 0:
                num_zeros += 1
            else:
                product *= matrix[j][i - j]
            j += 1

        # set as new max product if necessary
        if num_zeros == 0 and product > max_product:
            max_product = product

        # compute products of remaining sets of N digits along diagonal
        while j <= i:
            # remove top-rightmost digit from product
            if matrix[j - N][i - j + N] == 0:
                num_zeros -= 1
            else:
                product //= matrix[j - N][i - j + N]

            # add new bottom-leftmost digit to product
            if matrix[j][i - j] == 0:
                num_zeros += 1
            else:
                product *= matrix[j][i - j]

            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product

            j += 1

    # compute / diagonal products starting along bottom row
    for i in range(1, num_cols - N + 1):
        num_zeros = 0
        product = 1

        # compute product of initial N digits along diagonal
        j = 0
        while j < N:
            if matrix[-1 - j][i + j] == 0:
                num_zeros += 1
            else:
                product *= matrix[-1 - j][i + j]
            j += 1

        # set as new max product if necessary
        if num_zeros == 0 and product > max_product:
            max_product = product

        # compute products of remaining sets of N digits along diagonal
        while j < num_cols - i:
            # remove bottom-leftmost digit from product
            if matrix[-1 - j + N][i + j - N] == 0:
                num_zeros -= 1
            else:
                product //= matrix[-1 - j + N][i + j - N]

            # add new top-rightmost digit to product
            if matrix[-1 - j][i + j] == 0:
                num_zeros += 1
            else:
                product *= matrix[-1 - j][i + j]

            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product

            j += 1
    
    # compute \ diagonal products starting along bottom row
    for i in range(N - 1, num_cols):
        num_zeros = 0
        product = 1

        # compute product of initial N digits along diagonal
        j = 0
        while j < N:
            if matrix[-1 - j][i - j] == 0:
                num_zeros += 1
            else:
                product *= matrix[-1 - j][i - j]
            j += 1

        # set as new max product if necessary
        if num_zeros == 0 and product > max_product:
            max_product = product

        # compute products of remaining sets of N digits along diagonal
        while j <= i:
            # remove bottom-rightmost digit from product
            if matrix[-1 - j + N][i - j + N] == 0:
                num_zeros -= 1
            else:
                product //= matrix[-1 - j + N][i - j + N]

            # add new top-leftmost digit to product
            if matrix[-1 - j][i - j] == 0:
                num_zeros += 1
            else:
                product *= matrix[-1 - j][i - j]

            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product

            j += 1

    # compute \ diagonal products starting along top row
    for i in range(1, num_cols - N + 1):
        num_zeros = 0
        product = 1

        # compute product of initial N digits along diagonal
        j = 0
        while j < N:
            if matrix[j][i + j] == 0:
                num_zeros += 1
            else:
                product *= matrix[j][i + j]
            j += 1

        # set as new max product if necessary
        if num_zeros == 0 and product > max_product:
            max_product = product

        # compute products of remaining sets of N digits along diagonal
        while j < num_cols - i:
            # remove top-leftmost digit from product
            if matrix[j - N][i + j - N] == 0:
                num_zeros -= 1
            else:
                product //= matrix[j - N][i + j - N]

            # add new bottom-rightmost digit to product
            if matrix[j][i + j] == 0:
                num_zeros += 1
            else:
                product *= matrix[j][i + j]

            # set as new max product if necessary
            if num_zeros == 0 and product > max_product:
                max_product = product

            j += 1
    
    return max_product


if __name__ == '__main__':
    print(solve())
