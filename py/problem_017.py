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

Author: Curtis Belmonte
"""

# import common as com

# PARAMETERS ##################################################################

# TODO: parameterize upper limit

# SOLUTION ####################################################################

# Sum of all digit letter counts, excluding 0
all_digit_letters = (
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
all_teen_letters = (
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
all_ten_letters = (
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
and_letters = 3 # len('and')
hundred_letters = 7 # len('hundred')
one_letters = 3 # len('one')
thousand_letters = 8 # len('thousand')


def solve():
    # count the letters of all numbers below 20
    letter_count = all_digit_letters + all_teen_letters

    # count the letters of all numbers from 20 to 99
    digit_count = 9
    ten_count = 8
    letter_count += (all_ten_letters * (digit_count + 1)
                     + all_digit_letters * ten_count)
    letters_below_100 = letter_count

    # count the letters of all numbers from 100 to 999
    and_word_count = digit_count * 99
    hundred_word_count = and_word_count + digit_count
    letter_count += ((all_digit_letters * 100)
                     + (hundred_letters * hundred_word_count)
                     + (and_letters * and_word_count)
                     + (letters_below_100 * digit_count))

    # count the letters of 1000
    letter_count += one_letters + thousand_letters

    return letter_count


if __name__ == '__main__':
    print(solve())
