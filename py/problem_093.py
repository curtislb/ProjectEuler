#!/usr/bin/env python3

"""problem_093.py

Problem 93: Arithmetic expressions

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
making use of the four arithmetic operations (+, −, *, /) and parentheses, it
is possible to form different positive integer targets.

For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) − 1
    36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can
be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set
of consecutive positive integers, 1 to n, can be obtained, giving your answer
as a string: abcd.
"""

__author__ = 'Curtis Belmonte'

import itertools
import operator
from typing import Callable, Iterable, Optional, Sequence, Tuple

import common.digits as digs


# PARAMETERS ##################################################################


# N/A


# SOLUTION ####################################################################


# All valid binary arithmetic operations
ops = (operator.add, operator.sub, operator.mul, operator.truediv)


def digit_results(a: int, b: int, c: int, d: int) -> Iterable[int]:
    """Returns all results obtained by evaluating permutations of the digits
    a, b, c, d with all possible operators and parentheses placements."""

    results = set()
    for d1, d2, d3, d4 in itertools.permutations((a, b, c, d)):
        for f in ops:
            for g in ops:
                for h in ops:
                    for r in expr_results(d1, d2, d3, d4, f, g, h):
                        # filter out non-positive and non-integer values
                        if r > 0 and (isinstance(r, int) or
                                      isinstance(r, float) and r.is_integer()):
                            results.add(int(r))
    return results


def expr_results(
        d1: int,
        d2: int,
        d3: int,
        d4: int,
        f: Callable[[float, float], float],
        g: Callable[[float, float], float],
        h: Callable[[float, float], float]) -> Sequence[float]:

    """Returns all results obtained by evaluating the digits d1..d4 with
    operators f, g, h in order, with all possible parentheses placements."""

    results = []

    # try all distinct operation orders, ignoring any that divide by 0
    try:
        results.append(f(g(d1, d2), h(d3, d4)))
    except ZeroDivisionError:
        pass
    try:
        results.append(f(d1, g(d2, h(d3, d4))))
    except ZeroDivisionError:
        pass
    try:
        results.append(f(g(h(d1, d2), d3), d4))
    except ZeroDivisionError:
        pass

    return results


def natural_prefix_len(values: Iterable[int]) -> int:
    """Counts the consecutive integers from 1 to n from the start of values."""
    index = 0
    for index, value in enumerate(values):
        if value - 1 != index:
            break
    return index


def solve() -> Optional[int]:
    best_digits: Optional[Tuple[int, int, int, int]] = None
    max_count = 0

    # check all digit combinations 0 <= a < b < c < d <= 9
    for a in range(0, 7):
        for b in range(a + 1, 8):
            for c in range(b + 1, 9):
                for d in range(c + 1, 10):
                    results = digit_results(a, b, c, d)
                    count = natural_prefix_len(sorted(results))
                    if count > max_count:
                        max_count = count
                        best_digits = (a, b, c, d)

    return None if best_digits is None else digs.concat_digits(best_digits)


if __name__ == '__main__':
    print(solve())
