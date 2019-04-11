#!/usr/bin/env python3

"""Common library for producing expanded representations of real numbers.

This module provides functions for expanding (possibly irrational) numbers to
arbitrary precision. This can mean finding additional digits after the decimal
point or terms in the continued fraction expansion of a number.
"""

import math
from typing import Sequence, Tuple

import common.divisors as divs


def sqrt_decimal_expansion(n: int, precision: int) -> str:
    """Finds the square root of a number to arbitrary decimal precision.

    Args:
        n: A positive integer value.
        precision: The desired number of digits following the decimal point.

    Returns:
        A string representation of ``sqrt(n)`` in base 10 that includes the
        first ``precision`` digits after the decimal point.
    """

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
    """Finds terms in the continued fraction expansion of a square root.

    Args:
        n: A positive integer that is not a perfect square.

    Returns:
        A tuple of the form ``(a0, [a1, a2, ..., ar])``, where ``a0`` is the
        first term in the continued fraction expansion of ``sqrt(n)`` and the
        sequence of terms from ``a1`` to ``ar`` repeats indefinitely in the
        expansion. That is::

            sqrt(n) = a0 + 1/(a1 + 1/(a2 + ... 1/(ar + 1/(a1 + 1/(a2 + ...)))))

    Warnings:
        If ``n`` is a perfect square, no continued fraction expansion exists
        for ``sqrt(n)``, and the behavior of this function is undefined.
    """

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
