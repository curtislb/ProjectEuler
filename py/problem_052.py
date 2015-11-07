"""problem_052.py

Problem 52: Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, ..., Nx contain the
same digits.

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

N = 6 # default: 6

# SOLUTION ####################################################################

def has_permuted_multiples(x):
    """Determines if all multiples of x up to Nx contain the same digits."""
    x_digits = com.digit_counts(x)
    for n in range(2, N + 1):
        if com.digit_counts(n * x) != x_digits:
            return False
    return True


def solve():
    x = 125874
    while not has_permuted_multiples(x):
        x += 1
    return x


if __name__ == '__main__':
    print(solve())
