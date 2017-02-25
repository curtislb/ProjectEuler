#!/usr/bin/env python3

"""problem_089.py

Problem 89: Roman numerals

For a number written in Roman numerals to be considered valid there are basic
rules which must be followed. Even though the rules allow some numbers to be
expressed in more than one way there is always a "best" way of writing a
particular number.

For example, it would appear that there are at least six ways of writing the
number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last
example is considered to be the most efficient, as it uses the least number of
numerals.

The text file INPUT_FILE contains numbers written in valid, but not necessarily
minimal, Roman numerals.

Find the number of characters saved by writing each of these in their minimal
form.

Note: You can assume that all the Roman numerals in the file contain no more
than four consecutive identical units.

Author: Curtis Belmonte
"""


# PARAMETERS ##################################################################


INPUT_FILE = '../input/089.txt' # default: '../input/089.txt'


# SOLUTION ####################################################################


numeral_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def numeral_to_int(numeral):
    """Returns the integer value represented by the given Roman numeral."""
    i = 0
    numeral_len = len(numeral)
    total = 0
    while i < numeral_len:
        curr_value = numeral_values[numeral[i]]
        if i < numeral_len - 1:
            next_value = numeral_values[numeral[i + 1]]
            if curr_value < next_value:
                total += next_value - curr_value
                i += 2
            else:
                total += curr_value
                i += 1
        else:
            total += curr_value
            i += 1
    return total


def int_to_numeral(n):
    """Returns the minimal Roman numeral representation of the integer n."""

    numerals = []

    while n >= 1000:
        numerals.append('M')
        n -= 1000

    if n >= 900:
        numerals.append('C')
        numerals.append('M')
        n -= 900
    elif n >= 500:
        numerals.append('D')
        n -= 500
    elif n >= 400:
        numerals.append('C')
        numerals.append('D')
        n -= 400

    while n >= 100:
        numerals.append('C')
        n -= 100

    if n >= 90:
        numerals.append('X')
        numerals.append('C')
        n -= 90
    elif n >= 50:
        numerals.append('L')
        n -= 50
    elif n >= 40:
        numerals.append('X')
        numerals.append('L')
        n -= 40

    while n >= 10:
        numerals.append('X')
        n -= 10

    if n >= 9:
        numerals.append('I')
        numerals.append('X')
        n -= 9
    elif n >= 5:
        numerals.append('V')
        n -= 5
    elif n >= 4:
        numerals.append('I')
        numerals.append('V')
        n -= 4

    while n >= 1:
        numerals.append('I')
        n -= 1

    return ''.join(numerals)


def solve():
    chars_saved = 0
    with open(INPUT_FILE) as f:
        for line in f:
            numeral = line.rstrip()
            orig_len = len(numeral)
            mini_numeral = int_to_numeral(numeral_to_int(numeral))
            mini_len = len(mini_numeral)
            chars_saved += orig_len - mini_len
    return chars_saved


if __name__ == '__main__':
    print(solve())
