#!/usr/bin/env python3

"""problem_345.py

Problem 345: Matrix Sum

We define the Matrix Sum of a matrix as the maximum sum of matrix elements with
each element being the only one in his row and column. For example, the Matrix
Sum of the matrix below equals 3315 ( = 863 + 383 + 343 + 959 + 767):

       7   53  183  439 (863)
     497 (383) 563   79  973
     287   63 (343) 169  583
     627  343  773 (959) 943
    (767) 473  103  699  303

Find the Matrix Sum of the matrix contained in the file FILE_NAME.
"""

__author__ = 'Curtis Belmonte'

import copy

import common.fileio as fio
import common.matrices as mat


# PARAMETERS ##################################################################


FILE_NAME = '../input/345.txt'  # default: '../input/345.txt'


# SOLUTION ####################################################################


def solve() -> int:
    # read matrix from input file
    matrix = list(fio.ints_from_file(FILE_NAME))

    # build cost matrix by subtracting each entry from max entry
    cost_matrix = copy.deepcopy(matrix)
    max_value = max([max(row) for row in cost_matrix])
    for i, row in enumerate(cost_matrix):
        for j, value in enumerate(row):
            cost_matrix[i][j] = max_value - value

    # find optimal assignment in cost matrix
    assignment = mat.optimal_assignment(cost_matrix)

    # sum values in original matrix that correspond with assignment
    return sum([matrix[i][j] for i, j in assignment])


if __name__ == '__main__':
    print(solve())
