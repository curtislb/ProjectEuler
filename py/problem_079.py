"""problem_079.py

Problem 79: Passcode derivation

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file INPUT_FILE contains a set of successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

INPUT_FILE = '../input/079.txt' # default: '../input/079.txt'

# SOLUTION ####################################################################

def solve():
    with open(INPUT_FILE) as f:
        # keep track of all digits preceding other digits
        pre_digits = {}
        for line in f:
            digits = [int(digit_str) for digit_str in line.rstrip()]
            for i, digit in enumerate(digits):
                # add digit to dict if we haven't seen it before
                if digit not in pre_digits:
                    pre_digits[digit] = set()

                # add all of the preceding digits
                for j in range(i):
                    pre_digits[digit].add(digits[j])

        # sort digits by how many other digits precede them
        ordering = list(pre_digits.items())
        ordering.sort(key=(lambda x: len(x[1])))
        digits = [order[0] for order in ordering]

        return com.concat_digits(digits)


if __name__ == '__main__':
    print(solve())
