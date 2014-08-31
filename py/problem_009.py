"""problem_009.py

Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = S.

Find the product a*b*c.

@author: Curtis Belmonte
"""

import math
import sys

# import common

# PARAMETERS ##################################################################

S = 1000 # default: 1000

# SOLUTION ####################################################################

if __name__ == '__main__':
    # no triplet exists if S is not even
    if S % 2 != 0:
        print("No such triplet")
        sys.exit(0)

    # let a = 2*m*n, b = m^2 - n^2, c = m^2 + n^2. Then, m^2 + m*n = S/2
    s_div_2 = S / 2;
    m_limit = math.ceil(math.sqrt(s_div_2))

    # search for m and n under conditions m > n and m % 2 != n % 2
    for m in range(2, m_limit):
        if S % m == 0:
            s_div_2m = s_div_2 / m;
            for n in range(1 if m % 2 == 0 else 2, m, 2):
                if m + n == s_div_2m:
                    # compute a, b, and c from the definitions of m and n
                    m2 = m * m
                    n2 = n * n
                    print((2 * m * n) * (m2 - n2) * (m2 + n2))
                    sys.exit(0)
