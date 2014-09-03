"""problem_017.py

Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of 'and' when writing out numbers is in compliance with
British usage.

@author: Curtis Belmonte
"""

# import common

# PARAMETERS ##################################################################

# TODO: parameterize upper limit

# SOLUTION ####################################################################

# Sum of all digit letter counts, excluding 0
ALL_DIGIT_LETTERS = (
    3 # len('one')
  + 3 # len('two')
  + 5 # len('three')
  + 4 # len('four')
  + 4 # len('five')
  + 3 # len('six')
  + 5 # len('seven')
  + 5 # len('eight')
  + 4 # len('nine')
)

# Sum of all 'teen' letter counts, including 10, 11, and 12
ALL_TEEN_LETTERS = (
    3 # len('ten')
  + 6 # len('eleven')
  + 6 # len('twelve')
  + 8 # len('thirteen')
  + 8 # len('fourteen')
  + 7 # len('fifteen')
  + 7 # len('sixteen')
  + 9 # len('seventeen')
  + 8 # len('eighteen')
  + 8 # len('nineteen')
)

# Sum of all multiples of ten letter counts, excluding 10
ALL_TEN_LETTERS = (
    6 # len('twenty')
  + 6 # len('thirty')
  + 5 # len('forty')
  + 5 # len('fifty')
  + 5 # len('sixty')
  + 7 # len('seventy')
  + 6 # len('eighty')
  + 6 # len('ninety')
)

# Letter counts of other useful number words
AND_LETTERS = 3 # len('and')
HUNDRED_LETTERS = 7 # len('hundred')
ONE_LETTERS = 3 # len('one')
THOUSAND_LETTERS = 8 # len('thousand')

if __name__ == '__main__':
    # count the letters of all numbers below 20
    letter_count = ALL_DIGIT_LETTERS + ALL_TEEN_LETTERS

    # count the letters of all numbers from 20 to 99
    DIGIT_COUNT = 9
    TEN_COUNT = 8
    letter_count += (ALL_TEN_LETTERS * (DIGIT_COUNT + 1)
                     + ALL_DIGIT_LETTERS * TEN_COUNT)
    LETTERS_BELOW_100 = letter_count

    # count the letters of all numbers from 100 to 999
    AND_WORD_COUNT = DIGIT_COUNT * 99
    HUNDRED_WORD_COUNT = AND_WORD_COUNT + DIGIT_COUNT
    letter_count += ((ALL_DIGIT_LETTERS * 100)
                     + (HUNDRED_LETTERS * HUNDRED_WORD_COUNT)
                     + (AND_LETTERS * AND_WORD_COUNT)
                     + (LETTERS_BELOW_100 * DIGIT_COUNT))

    # count the letters of 1000
    letter_count += ONE_LETTERS + THOUSAND_LETTERS

    print(letter_count)
