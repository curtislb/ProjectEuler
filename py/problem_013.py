"""problem_013.py

Problem 13: Large sum

Work out the first D digits of the sum of the numbers contained in the file
INPUT_FILE (all of which have the same number of digits).

@author: Curtis Belmonte
"""

# import common

# PARAMETERS ##################################################################

INPUT_FILE = '../input/013.txt' # default: '../input/013.txt'

# SOLUTION ####################################################################

if __name__ == '__main__':
    total = 0
    with open(INPUT_FILE) as file:
        for line in file:
            total += int(line[:-1])
    print(str(total)[:10])
