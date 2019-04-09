#!/usr/bin/env python3

"""Common library for performing arithmetic operations.

This module provides functions for performing common arithmetic operations.
Examples include evaluating a postfix expression, finding the modular product
of two numbers, and finding the roots of a quadratic polynomial.
"""

import math
import operator
from typing import Callable, List, Mapping, Tuple, Union


#: Mapping from string tokens of binary arithmetic operations to functions.
BINARY_OPS: Mapping[str, Callable[[float, float], float]] = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}


def eval_postfix(expr: str, is_space_sep: bool = True) -> float:
    """Evaluates an arithmetic expression written in postfix notation.

    Args:
        expr: A string consisting of digits (0-9), operators (``+ - * / ^``),
            and/or spaces (iff ``is_space_sep`` is ``True``).
        is_space_sep: If ``True``, expects operators and operands to be
            space-separated in ``expr``. If ``False``, ``expr`` cannot contain
            spaces, and each digit is treated as a separate operand.

    Returns:
        The number that results from evaluating the expression.
    """
    stack: List[Union[str, float]] = []
    for token in (expr.split() if is_space_sep else expr):
        if token in BINARY_OPS:
            y = float(stack.pop())
            x = float(stack.pop())
            stack.append(BINARY_OPS[token](x, y))
        else:
            stack.append(token)
    return float(stack.pop())


def int_log(x: float, base: float = math.e) -> int:
    """Finds the nearest integer to ``log(x, base)``.

    Args:
        x: The number whose logarithm will be found.
        base: The numeric base of the logarithm.

    Returns:
        The result of rounding ``log(x, base)`` to the nearest integer.
    """
    return int(round(math.log(float(x), float(base))))


def int_pow(x: float, exponent: float) -> int:
    """Finds the nearest integer to ``pow(x, exponent)``.

    Args:
        x: The number whose power will be found.
        exponent: The number to which ``x`` will be raised.

    Returns:
        The result of rounding ``pow(x, exponent)`` to the nearest integer.
    """
    return int(round(x**exponent))


def int_sqrt(x: float) -> int:
    """Finds the nearest integer to the square root of ``x``.

    Args:
        x: The number whose square root will be found.

    Returns:
        The result of rounding ``sqrt(x)`` to the nearest integer.
    """
    return int(round(math.sqrt(x)))


def mod_multiply(n: int, m: int, mod: int) -> int:
    """Finds the the modular product of two non-negative integers.

    Args:
        n: The first non-negative integer multiplicand.
        m: The second non-negative integer multiplicand.
        mod: The positive integer modulus for the calculation.

    Returns:
        The result of multiplying ``n`` by ``m``, modulo ``mod``.
    """
    return ((n % mod) * (m % mod)) % mod


def mod_power(base: int, exponent: int, mod: int) -> int:
    """Finds the the modular power of ``base`` raised to ``exponent``.

    Args:
        base: The non-negative integer to be raised to a power.
        exponent: The non-negative integer power to be applied.
        mod: The positive integer modulus for the calculation.

    Returns:
        The result of raising ``base`` to ``exponent``, modulo ``mod``.
    """

    # set initial result to base % mod if exponent is odd
    result = 1
    sub_ans = base
    n, m = divmod(exponent, 2)
    if m == 1:
        result = sub_ans % mod

    # find result by decomposing into powers of two
    while n > 0:
        # compute 2^k % mod for each k up to log_2(exponent)
        sub_ans = mod_multiply(sub_ans, sub_ans, mod)

        # combine with result if exponent's kth binary digit is 1
        n, m = divmod(n, 2)
        if m == 1:
            result = mod_multiply(result, sub_ans, mod)

    return result


def quadratic_roots(
    a: float,
    b: float,
    c: float,
) -> Tuple[Union[float, complex], Union[float, complex]]:
    """Finds all roots of the quadratic polynomial ``ax^2 + bx + c = 0``.

    Args:
        a: The coefficient of ``x^2`` in the polynomial. Must be non-zero.
        b: The coefficient of ``x`` in the polynomial.
        c: The constant addend term in the polynomial.

    Returns:
        A tuple ``(x0, x1)``, where ``x0`` and ``x1`` are solutions for ``x``
        in ``ax^2 + bx + c = 0`` and ``x0 <= x1``, assuming a natural ordering.
    """
    axis = -b
    delta = (b**2 - 4 * a * c)**0.5
    denom = 2 * a
    return (axis - delta) / denom, (axis + delta) / denom
