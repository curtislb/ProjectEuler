"""problem_043.py

Problem 43: Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d(1) be the 1st digit, d(2) be the 2nd digit, and so on. In this way, we
note the following:

    d(2)d(3)d(4) = 406 is divisible by 2
    d(3)d(4)d(5) = 063 is divisible by 3
    d(4)d(5)d(6) = 635 is divisible by 5
    d(5)d(6)d(7) = 357 is divisible by 7
    d(6)d(7)d(8) = 572 is divisible by 11
    d(7)d(8)d(9) = 728 is divisible by 13
    d(8)d(9)d(10) = 289 is divisible by 17

Find the sum of all START to END pandigital numbers with the property that each
of the digit substrings with start and end indices in DIGIT_INDICES is
divisible by its respective divisor in DIVISORS.

@author: Curtis Belmonte
"""

import itertools

import common as com

# PARAMETERS ##################################################################

START = 0 # default: 0
END = 9 # default: 9
DIGIT_INDICES = [[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10]]
    # default: [[2,4],[3,5],[4,6],[5,7],[6,8],[7,9],[8,10]]
DIVISORS = [2,3,5,7,11,13,17] # default: [2,3,5,7,11,13,17]

# SOLUTION ####################################################################

# Number of divisors; must match length of DIGIT_INDICES
divisor_count = len(DIVISORS)


def concats_divisible_by_divisors(num_string):
    """Determines if the pandigital number with decimal string representation
    num_string satisfies the problem conditions."""
    
    # check if all concatenated numbers are divisible by divisors in DIVISORS
    for i in range(divisor_count):
        # form number by concatenating digits of num_string
        indices = DIGIT_INDICES[i]
        concat_num = int(num_string[indices[0]-1:indices[1]])
        
        # check if concatenated number is divisible by its divisor in DIVISORS
        if concat_num % DIVISORS[i] != 0:
            return False
    
    return True


def main():
    pandigit_string = com.pandigital_string(START, END)
    
    # check if each pandigital number satisfies the problem conditions
    total = 0
    for digit_chars in itertools.permutations(pandigit_string):
        # form the pandigital string from its permutated digit characters
        num_string = ''.join(digit_chars)
        
        # add to total if pandigital number satisfies the problem conditions
        if concats_divisible_by_divisors(num_string):
            total += int(num_string)
    
    return total


if __name__ == '__main__':
    print(main())
