"""problem_145.py

Problem 145: How many reversible numbers are there below one-billion?

Some positive integers n have the property that the sum n + reverse(n) consists
entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 =
1313. We will call such numbers reversible; so 36, 63, 409, and 904 are
reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below 10**DIGIT_LIMIT?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

DIGIT_LIMIT = 9 # default: 9

# SOLUTION ####################################################################

def solve():
    count = 0
    for digits in range(2, DIGIT_LIMIT):
        if digits % 2 == 0:
            count += 20 * 30**((digits // 2) - 1)

        elif digits % 4 == 3:
            count += 100 * 500**(digits // 4)

    return count


if __name__ == '__main__':
    print(solve())
