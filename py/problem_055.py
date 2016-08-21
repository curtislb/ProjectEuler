#!/usr/bin/env python3

"""problem_055.py

Problem 55: Lychrel numbers

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196,
never produce a palindrome. A number that never forms a palindrome through the
reverse and add process is called a Lychrel number. Due to the theoretical
nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise. In addition you are given that
for every number below LIMIT, it will either (n) become a palindrome in less
than MAX_ITER iterations, or, (ii) no one, with all the computing power that
exists, has managed so far to map it to a palindrome.

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers;
the first example is 4994.

How many Lychrel numbers are there below LIMIT?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 10000 # default: 1000
MAX_ITER = 50 # default: 50

# SOLUTION ####################################################################

def solve():
    count = 0
    for n in range(10, LIMIT):
        for __ in range(MAX_ITER):
            n += int(str(n)[::-1])
            if com.is_palindrome(n):
                break
        else:
            count += 1

    return count


if __name__ == '__main__':
    print(solve())
