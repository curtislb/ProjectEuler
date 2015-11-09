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

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

INPUT_FILE = '../input/096.txt'

# SOLUTION ####################################################################

def read_puzzles(filename):
    with open(INPUT_FILE) as f:
        puzzles = []
        while True:
            line = f.readline()
            if line == '':
                break
            grid = []
            for __ in range(9):
                row = [int(digit) for digit in f.readline().rstrip()]
                grid.append(row)
            puzzles.append(grid)
    return puzzles


def box_coords(n_box, row, col):
    i_box, j_box = divmod(n_box, 3)
    delta_i = (row // 3) * 3
    delta_j = (col // 3) * 3
    return (i_box + delta_i, j_box + delta_j)


def valid_digits(grid, row, col):
    digits = set(range(1, 10))
    
    # 1-9 in row
    for j in range(9):
        if j != col:
            try:
                digits.remove(grid[row][j])
            except KeyError:
                pass
    
    # 1-9 in column
    for i in range(9):
        if i != row:
            try:
                digits.remove(grid[i][col])
            except KeyError:
                pass
    
    # 1-9 in box
    for n_box in range(9):
        i, j = box_coords(n_box, row, col)
        if (i, j) != (row, col):
            try:
                digits.remove(grid[i][j])
            except KeyError:
                pass
            
    return list(digits)


def solve_puzzle(puzzle):
    grid = [row[:] for row in puzzle]
    
    modified = True
    min_digits = (None, 10)
    min_square = None
    while modified:
        modified = False
        for i, row in enumerate(grid):
            for j, square in enumerate(row):
                if square == 0:
                    digits = valid_digits(grid, i, j)
                    num_digits = len(digits)
                    if num_digits == 0:
                        return None
                    elif num_digits == 1:
                        grid[i][j] = digits[0]
                        modified = True  
                    elif num_digits < min_digits[1]:
                        min_digits = (digits, num_digits)
                        min_square = (i, j)
    
    if min_square is None:
        return [row[:] for row in grid]
    else:
        i, j = min_square
        for digit in min_digits[0]:
            grid[i][j] = digit
            soln = solve_puzzle(grid)
            if soln is not None:
                return [row[:] for row in soln]
        return None


if __name__ == '__main__':
    puzzles = read_puzzles(INPUT_FILE)
    total = 0
    for puzzle in puzzles[40:41]:
        grid = solve_puzzle(puzzle)
        
#         for row in puzzle:
#             print(row)
#         print()
        for row in grid:
            print(row)
        
        total += com.concat_digits((grid[0][0], grid[0][1], grid[0][2]))
    print(total)
