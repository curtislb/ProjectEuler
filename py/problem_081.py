"""problem_081.py

Problem 81: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated by parentheses
and is equal to 2427.

    (131)  673   234   103    18
    (201)  (96) (342)  965   150
     630   803  (746) (422)  111
     537   699   497  (121)  956
     805   732   524   (37) (331)

Find the minimal path sum in INPUT_FILE, a text file containing a square
matrix, from the left column to the right column.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

INPUT_FILE = '../input/081.txt' # default: '../input/081.txt'

# SOLUTION ####################################################################

def solve():
    matrix = com.numbers_from_file(INPUT_FILE, sep=',')
    n = len(matrix[0])
    
    # dynamically update costs along diagonals from bottom-right to middle
    for diag in range(2, n + 1):
        i = -1
        j = -diag
        while j < 0:
            down_cost = matrix[i + 1][j] if i < -1 else com.INFINITY
            right_cost = matrix[i][j + 1] if j < -1 else com.INFINITY
            matrix[i][j] += min(down_cost, right_cost)
            i -= 1
            j += 1

    # dynamically update costs along diagonals from middle to top-left
    for diag in range(2, n + 1):
        i = -diag
        j = -n
        while i >= -n:
            down_cost = matrix[i + 1][j] if i < -1 else com.INFINITY
            right_cost = matrix[i][j + 1] if j < -1 else com.INFINITY
            matrix[i][j] += min(down_cost, right_cost)
            i -= 1
            j += 1

    return matrix[0][0]


if __name__ == '__main__':
    print(solve())
