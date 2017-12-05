#!/usr/bin/env python3

"""problem_096.py

Problem 96: Su Doku

Su Doku (Japanese meaning number place) is the name given to a popular puzzle
concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
who invented a similar, and much more difficult, puzzle idea called Latin
Squares. The objective of Su Doku puzzles, however, is to replace the blanks
(or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box
contains each of the digits 1 to 9. Below is an example of a typical starting
puzzle grid and its solution grid.

    +-------+-------+-------+    +-------+-------+-------+
    | 0 0 3 | 0 2 0 | 6 0 0 |    | 4 8 3 | 9 2 1 | 6 5 7 |
    | 9 0 0 | 3 0 5 | 0 0 1 |    | 9 6 7 | 3 4 5 | 8 2 1 |
    | 0 0 1 | 8 0 6 | 4 0 0 |    | 2 5 1 | 8 7 6 | 4 9 3 |
    +-------+-------+-------+    +-------+-------+-------+
    | 0 0 8 | 1 0 2 | 9 0 0 |    | 5 4 8 | 1 3 2 | 9 7 6 |
    | 7 0 0 | 0 0 0 | 0 0 8 |    | 7 2 9 | 5 6 4 | 1 3 8 |
    | 0 0 6 | 7 0 8 | 2 0 0 |    | 1 3 6 | 7 9 8 | 2 4 5 |
    +-------+-------+-------+    +-------+-------+-------+
    | 0 0 2 | 6 0 9 | 5 0 0 |    | 3 7 2 | 6 8 9 | 5 1 4 |
    | 8 0 0 | 2 0 3 | 0 0 9 |    | 8 1 4 | 2 5 3 | 7 6 9 |
    | 0 0 5 | 0 1 0 | 3 0 0 |    | 6 9 5 | 4 1 7 | 3 8 2 |
    +-------+-------+-------+    +-------+-------+-------+

A well constructed Su Doku puzzle has a unique solution and can be solved by
logic, although it may be necessary to employ "guess and test" methods in order
to eliminate options (there is much contested opinion over this). The
complexity of the search determines the difficulty of the puzzle; the example
above is considered easy because it can be solved by straight forward direct
deduction.

The text file, INPUT_FILE, contains different Su Doku puzzles ranging in
difficulty, but all with unique solutions.

By solving all puzzles find the sum of the 3-digit numbers found in the top
left corner of each solution grid; for example, 483 is the 3-digit number found
in the top left corner of the solution grid above.
"""

__author__ = 'Curtis Belmonte'

import copy
from typing import *

from common.types import IntMatrix


# PARAMETERS ##################################################################


INPUT_FILE = '../input/096.txt' # default: '../input/096.txt'


# SOLUTION ####################################################################


def get_valid_digits(grid: IntMatrix, i: int, j: int) -> Set[int]:
    """Returns a set of all digits that could be placed in cell (i, j) based on
    the current configuration of grid.
    """

    digits = set(range(1, 10))

    # remove digits in same row or column
    for k in range(9):
        row_digit = grid[i][k]
        if row_digit in digits:
            digits.remove(row_digit)

        col_digit = grid[k][j]
        if col_digit in digits:
            digits.remove(col_digit)

    # remove digits in same 3x3 box
    box_i = (i // 3) * 3
    box_j = (j // 3) * 3
    for row in range(box_i, box_i + 3):
        for col in range(box_j, box_j + 3):
            box_digit = grid[row][col]
            if box_digit in digits:
                digits.remove(box_digit)

    return digits


def solve_puzzle(grid: IntMatrix) -> Optional[IntMatrix]:
    """Solves the puzzle represented by grid and returns the solution grid."""

    # deterministically fill in puzzle grid as much as possible
    puzzle_changed = True
    best_digits = None
    best_cell = None
    while puzzle_changed:
        puzzle_changed = False
        best_count = float('inf')
        best_digits = None
        best_cell = None
        for i, row in enumerate(grid):
            for j, digit in enumerate(row):
                if digit == 0:
                    digits = get_valid_digits(grid, i, j)
                    valid_count = len(digits)
                    if valid_count == 0:
                        # no possible solutions
                        return None
                    elif valid_count == 1:
                        # only one valid digit; fill it in
                        grid[i][j] = list(digits)[0]
                        puzzle_changed = True
                    elif valid_count < best_count:
                        # keep track of cell with fewest valid digits
                        best_count = valid_count
                        best_digits = digits
                        best_cell = (i, j)

    # solve puzzle recursively and return solution grid
    if best_digits is None:
        # puzzle is already solved
        return grid
    else:
        # try each valid digit for cell with fewest possible
        i, j = best_cell
        for digit in best_digits:
            grid_copy = copy.deepcopy(grid)
            grid_copy[i][j] = digit
            solved = solve_puzzle(grid_copy)
            if solved:
                return solved
    
    # no possible solutions
    return None


def solve() -> int:
    # read intial puzzle grids from input file
    grids = []
    with open(INPUT_FILE) as f:
        while f.readline():
            grid = []
            for i in range(9):
                line = f.readline().strip()
                row = [int(c) for c in line]
                grid.append(row)

            grids.append(grid)

    # solve each puzzle and sum top-left values
    total = 0
    for grid in grids:
        solution = solve_puzzle(grid)
        solved_grid = solution if solution is not None else grid
        total += int(''.join(map(str, solved_grid[0][:3])))

    return total


if __name__ == '__main__':
    print(solve())
