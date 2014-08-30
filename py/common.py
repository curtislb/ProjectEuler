"""common.py

Common utility functions and classes for various Project Euler problems.

@author: Curtis Belmonte
"""

def arith_series(a, n, d):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def gcd(m, n):
    """Returns the greatest common divisor of natural numbers m and n."""
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m


def lcm(m, n):
    """Returns the least common multiple of natural numbers m and n."""
    return m * n // gcd(m, n)