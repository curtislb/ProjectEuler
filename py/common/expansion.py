#!/usr/bin/env python3

"""expansion.py

Functions for producing expanded representations of real numbers.
"""

__author__ = 'Curtis Belmonte'

import math
from typing import *

import common.divisors as divs


def sqrt_decimal_expansion(n: int, precision: int) -> str:
    """Returns the square root of the natural number n to arbitrary precision.

    Result is a string with precision digits following the decimal point."""

    # break n into two-digit chunks
    n_digits = []
    while n > 0:
        n, mod = divmod(n, 100)
        n_digits.append(mod)
    n_digits.reverse()

    expansion = []
    remainder = 0
    root_part = 0

    def f(x: int) -> int:
        return x * (20 * root_part + x)

    # compute digits before decimal point
    for carry in n_digits:
        a = 1
        b = f(a)
        c = remainder * 100 + carry
        while b <= c:
            a += 1
            b = f(a)

        a -= 1
        b = f(a)
        remainder = c - b
        root_part = root_part * 10 + a
        expansion.append(str(a))

    expansion.append('.')

    # compute digits after decimal point
    for _ in range(precision):
        a = 1
        b = f(a)
        c = remainder * 100
        while b <= c:
            a += 1
            b = f(a)

        a -= 1
        b = f(a)
        remainder = c - b
        root_part = root_part * 10 + a
        expansion.append(str(a))

    return ''.join(expansion)


def sqrt_fraction_expansion(n: int) -> Tuple[int, Sequence[int]]:
    """Returns the terms in the continued fraction expansion of the square root
    of the non-square natural number n, in the format (a0, a1..ar)."""

    # perform the first expansion step
    sqrt_n = math.sqrt(n)
    a0 = int(sqrt_n)
    addend = -a0
    denom = 1

    # continue expansion until terms begin to cycle
    block = []
    end_term = 2 * a0
    while True:
        # compute newly expanded denominator
        new_denom = n - addend**2
        new_denom //= divs.gcd(denom, new_denom)

        # extract term and compute new addend
        term = int((sqrt_n - addend) / new_denom)
        new_addend = -addend - (term * new_denom)

        # add term to expansion and update rational value
        block.append(term)
        addend = new_addend
        denom = new_denom

        # check if term completes cycle
        if term == end_term:
            return a0, block
