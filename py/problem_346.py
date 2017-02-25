#!/usr/bin/env python3

"""problem_346.py

Problem 346: Strong Repunits

The number 7 is special, because 7 is 111 written in base 2, and 11 written in
base 6 (i.e. 710 = 116 = 1112). In other words, 7 is a repunit in at least two
bases B > 1.

We shall call a positive integer with this property a strong repunit. It can be
verified that there are 8 strong repunits below 50: {1,7,13,15,21,31,40,43}.
Furthermore, the sum of all strong repunits below 1000 equals 15864.

Find the sum of all strong repunits below N.

Author: Curtis Belmonte
"""

import math


# PARAMETERS ##################################################################


N = 10**12 # default: 10**12


# SOLUTION ####################################################################


def solve():
    total = 1
    repunits = {1}
    for k in range(3, int(math.ceil(math.log(N, 2)))):
        max_b = 2
        while (max_b**k - 1) // (max_b - 1) < N:
            max_b += 1

        for b in range(2, max_b):
            n = (b**k - 1) // (b - 1)
            if n not in repunits:
                repunits.add(n)
                total += n

    return total


if __name__ == '__main__':
    print(solve())
