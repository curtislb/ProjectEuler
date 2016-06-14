"""problem_017.py

Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to MAX_NUMBER inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of 'and' when writing out numbers is in compliance with
British usage.

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

MAX_NUMBER = 1000 # default: 1000

# SOLUTION ####################################################################

and_letters = len('and')

# letter counts for unique numbers (see common.NUMBER_WORDS)
num_letters = {0: 0}
for number, word in com.NUMBER_WORDS.items():
    num_letters[number] = len(word)

# letter counts for relevant powers of 10
pow10_letters = {
    100: len('hundred'),
    1000: len('thousand'),
    10**6: len('million'),
}


@com.memoized
def count_letters(n):
    """Returns the number of letters in the written representation of the
    natural number n (in compliance with British usage)."""

    count = 0

    # count letters for powers of 10
    pow10_flag = False
    for pow10 in sorted(pow10_letters.keys(), reverse=True):
        if n >= pow10:
            pow10_flag = True

            div, mod = divmod(n, pow10)
            count += count_letters(div) + pow10_letters[pow10]
            n = mod

    # count letters for "and" if necessary
    if pow10_flag and n > 0:
        count += and_letters

    # count letters for tens place (at and above 20)
    if n >= 20:
        ones_digit = n % 10
        count += num_letters[n - ones_digit]
        n = ones_digit
    
    # count letters for ones place
    count += num_letters[n]

    return count


def solve():
    total = 0
    for n in range(1, MAX_NUMBER + 1):
        total += count_letters(n)
    return total


if __name__ == '__main__':
    print(solve())
