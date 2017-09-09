#!/usr/bin/env python3

"""arithmetic.py



Author: Curtis Belmonte
"""

import math


def int_log(x, base=math.e):
    """Returns the rounded integer logarithm of x for the given base."""
    return int(round(math.log(x, base)))


def int_pow(x, exponent):
    """Returns the rounded integer power of x to the exponent power."""
    return int(round(x**exponent))


def int_sqrt(x):
    """Returns the rounded integer square root of the number x."""
    return int(round(math.sqrt(x)))


def mod_multiply(n, m, mod):
    """Returns the the product of natural numbers n and m modulo mod."""
    return ((n % mod) * (m % mod)) % mod


def quadratic_roots(a, b, c):
    """Finds all roots of the equation a*x^2 + b*x + c = 0, where a != 0.

    Returns a tuple (x0, x1), where x0 and x1 are solutions for x in the above
    equation and x0 <= x1, assuming a natural ordering. Both x0 and x1 may
    contain an imaginary part if no real solution exists."""

    axis = -b
    delta = (b**2 - 4 * a * c)**0.5
    denom = 2 * a
    return (axis - delta) / denom, (axis + delta) / denom
