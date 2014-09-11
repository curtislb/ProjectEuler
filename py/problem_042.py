"""problem_042.py

Problem 42: Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, t(n) = ½n(n+1);
so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). If the word value
is a triangle number then we shall call the word a triangle word.

Using INPUT_FILE, a text file containing many common English words, how many
are triangle words?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

INPUT_FILE = '../input/042.txt' # default: '../input/042.txt'

# SOLUTION ####################################################################

@common.memoized
def word_value(word):
    """Returns the word value for word, computed as the sum of the alphabetical
    positions of each of its letters."""
    if word == '':
        return 0
    return word_value(word[:-1]) + common.alphabet_index_upper(word[-1])

if __name__ == '__main__':
    # compute word values for all words in the input file
    WORD_VALUES = [word_value(word)
                   for word in common.strings_from_file(INPUT_FILE)]
    MAX_WORD_VALUE = max(WORD_VALUES)
    
    # compute triangle numbers up to maximum word value
    triangle_nums = set()
    i = 0
    triangle_num = common.triangle(i)
    while triangle_num <= MAX_WORD_VALUE:
        triangle_nums.add(triangle_num)
        i += 1
        triangle_num = common.triangle(i)
    
    # count the number of word values that are triangle numbers
    print(sum((word_value in triangle_nums) for word_value in WORD_VALUES))
    