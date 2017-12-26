#!/usr/bin/env python3

"""arithmetic.py

Functions for performing common arithmetic operations.
"""

__author__ = 'Curtis Belmonte'

import math
import operator
from typing import Callable, List, Mapping, Optional, Tuple, Union


# Mapping from string tokens of binary arithmetic operations to their functions
BINARY_OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
} # type: Mapping[str, Callable[[float, float], float]]


def eval_postfix(expr: str, is_space_sep: bool = True) -> float:
    """Evaluates an arithmetic expression written in postfix notation.

    If is_space_sep is False, whitespace between tokens is disallowed, and
    each digit is treated as a separate operand in the expression.
    """

    stack = [] # type: List[Union[str, float]]
    for token in (expr.split() if is_space_sep else expr):
        if token in BINARY_OPS:
            y = float(stack.pop())
            x = float(stack.pop())
            stack.append(BINARY_OPS[token](x, y))
        else:
            stack.append(token)
    return float(stack.pop())


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
