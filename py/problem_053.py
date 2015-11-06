"""problem_053.py

Problem 53: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr = n! / (r!(n−r)!), where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr, for 1 ≤ n ≤ MAX_N, are
greater than MIN_VALUE?

@author: Curtis Belmonte
"""

import math

import common as com

# PARAMETERS ##################################################################

MAX_N = 100 # default: 100
MIN_VALUE = 1000000 # default: 1000000

# SOLUTION ####################################################################

def solve():
    count = 0

    for n in range(2, MAX_N + 1):
        # find first r for which nCr is greater than MIN_VALUE
        r = 1
        while r <= n // 2:
            if com.choose(n, r) > MIN_VALUE:
                break
            r += 1

        div, mod = divmod(n, 2)
        if r <= div:
            # double-count terms from r to middle of row of Pascal's triangle
            count += 2 * (int(math.ceil(n / 2)) - r)

            # count additional middle term for even-numbered rows
            if mod == 0:
                count += 1

    return count


if __name__ == '__main__':
    print(solve())
