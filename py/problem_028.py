"""problem_028.py

Problem 28: Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in an N by N spiral formed in
the same way?

@author: Curtis Belmonte
"""

# import common

# PARAMETERS ##################################################################

N = 1001 # default: 1001

# SOLUTION ####################################################################

def spiral_diagonal_sum(layers):
    """Returns the sum of the diagonals of the number spiral with the given
    number of layers."""
    
    # base case: spiral with 1 layer has a diagonal sum of 1
    if layers < 2:
        return 1
    
    SIDE = layers * 2 - 1
    SIDE_SQUARED = SIDE * SIDE
    
    # compute the sum of the diagonal entries of the current layer and recurse
    return SIDE_SQUARED * 4 - (SIDE - 1) * 6 + spiral_diagonal_sum(layers - 1)


if __name__ == '__main__':
    print(spiral_diagonal_sum((N + 1) // 2))
