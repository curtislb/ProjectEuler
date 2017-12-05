#!/usr/bin/env python3

"""arithmetic.py

Functions for performing common arithmetic operations.
"""

__author__ = 'Curtis Belmonte'

import math
from typing import *


def int_log(x: float, base: float = math.e) -> int:
    """Returns the rounded integer logarithm of x for the given base."""
    return int(round(math.log(float(x), float(base))))


def int_pow(x: float, exponent: float) -> int:
    """Returns the rounded integer power of x to the exponent power."""
    return int(round(x**exponent))


def int_sqrt(x: float) -> int:
    """Returns the rounded integer square root of the number x."""
    return int(round(math.sqrt(x)))


def min_present(a: Optional[int], b: Optional[int]) -> Optional[int]:
    """Returns the minimum of two optional integers, if present."""
    return (a if b is None else
            b if a is None else
            min(a, b))


def mod_multiply(n: int, m: int, mod: int) -> int:
    """Returns the the product of natural numbers n and m modulo mod."""
    return ((n % mod) * (m % mod)) % mod


def quadratic_roots(a: float, b: float, c: float)\
        -> Tuple[Union[float, complex], Union[float, complex]]:
    """Finds all roots of the equation a*x^2 + b*x + c = 0, where a != 0.

    Returns a tuple (x0, x1), where x0 and x1 are solutions for x in the above
    equation and x0 <= x1, assuming a natural ordering. Both x0 and x1 may
    contain an imaginary part if no real solution exists."""

    axis = -b
    delta = (b**2 - 4 * a * c)**0.5
    denom = 2 * a
    return (axis - delta) / denom, (axis + delta) / denom
