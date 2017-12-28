#!/usr/bin/env python3

"""sequences.py

Functions for producing and operating on numerical sequences.
"""

__author__ = 'Curtis Belmonte'

import functools
import math
import operator
from typing import Callable, Dict, Iterable, Optional, Set

import common.arithmetic as arith


# Currently computed terms of the Fibonacci sequence (in sorted order)
_fibonacci_sequence = [1, 1]


def _compute_chain_length(
        lengths: Dict[int, int],
        n: int,
        step: Callable[[int], int],
        is_valid: Callable[[int], bool],
        invalid_set: Set[int],
        terms: Optional[Dict[int, int]] = None) -> None:

    """Recursive helper function for compute_chain_lengths that updates lengths
    with appropriate chain lengths starting from n.
    """

    if terms is None:
        terms = {}

    # if chain is invalid, mark all terms accordingly
    if not is_valid(n) or n in invalid_set or n in lengths:
        for n in terms:
            invalid_set.add(n)

    # if completed chain, set length for all terms in it and invalidate others
    elif n in terms:
        index = terms[n]
        length = len(terms) - index
        for n, i in terms.items():
            if i < index:
                invalid_set.add(n)
            else:
                lengths[n] = length

    # otherwise, continue building the current chain
    else:
        terms[n] = len(terms)
        _compute_chain_length(
            lengths,
            step(n),
            step,
            is_valid,
            invalid_set,
            terms)


def _compute_fibonacci(n: int) -> None:
    """Precomputes and stores the Fibonacci numbers up to F(n)."""

    fib_count = len(_fibonacci_sequence)

    # have the numbers up to F(n) already been computed?
    if n < fib_count:
        return

    # compute numbers iteratively from existing sequence
    f0 = _fibonacci_sequence[-2]
    f1 = _fibonacci_sequence[-1]
    for i in range(fib_count, n + 1):
        f0, f1 = f1, f0 + f1
        _fibonacci_sequence.append(f1)


def arithmetic_product(a: int, n: int, d: int = 1) -> int:
    """Returns the product of the arithmetic sequence with first term a, number
    of terms n, and difference between terms d.
    """
    return functools.reduce(operator.mul, range(a, a + n * d, d), 1)


def arithmetic_series(a: int, n: int, d: int = 1) -> int:
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d.
    """
    return n * (2 * a + (n - 1) * d) // 2


def collatz_step(n: int) -> int:
    """Returns the next number in the Collatz sequence following n."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def compute_chain_lengths(
        lengths: Dict[int, int],
        values: Iterable[int],
        step: Callable[[int], int],
        is_valid: Callable[[int], bool] = lambda x: True) -> None:

    """Populates lengths with chain lengths starting from each term in values.

    lengths   the dict to be populated, mapping each term to its chain length
    values    an iterable of all valid starting terms for a chain
    step      for any term n, step(n) gives the next term in the chain
    is_valid  is_valid(n) returns True iff n is a valid chain member
    """

    invalid_set = set() # type: Set[int]
    for n in values:
        _compute_chain_length(lengths, n, step, is_valid, invalid_set)


def fibonacci(n: int) -> int:
    """Returns the nth Fibonacci number, with F(0) = F(1) = 1."""
    _compute_fibonacci(n)
    return _fibonacci_sequence[n]


def hexagonal(n: int) -> int:
    """Returns the nth hexagonal number."""
    return n * (2 * n - 1)


def is_hexagonal(n: int) -> bool:
    """Determines if the natural number n is a hexagonal number."""
    radical_sum = 1 + (8 * n)
    return is_square(radical_sum) and arith.int_sqrt(radical_sum) % 4 == 3


def is_pentagonal(n: int) -> bool:
    """Determines if the natural number n is a pentagonal number."""
    radical_sum = 1 + (24 * n)
    return is_square(radical_sum) and arith.int_sqrt(radical_sum) % 6 == 5


def is_power(n: int, p: int) -> bool:
    """Determines if the natural number n is a perfect power with exponent p.

    Specifically, returns True iff n = m**p for some natural number m.
    """

    root_n = n**(1 / p)
    lo_power = (int(root_n))**p
    hi_power = (int(math.ceil(root_n)))**p
    return lo_power == n or hi_power == n


def is_square(n: int) -> bool:
    """Determines if the natural number n is a perfect square."""
    return (int(math.sqrt(n)))**2 == n


def is_triangular(n: int) -> bool:
    """Determines if the natural number n is a triangle number."""
    return is_square(8 * n + 1)


def next_multiple(n: int, min_val: int) -> int:
    """Returns the next multiple of the natural number n >= min_val."""
    return min_val + ((n - (min_val % n)) % n)


def pentagonal(n: int) -> int:
    """Returns the nth pentagonal number."""
    return n * (3 * n - 1) // 2


def sum_of_squares(n: int) -> int:
    """Returns the sum of the squares of the first n natural numbers."""
    return (2 * n**3 + 3 * n**2 + n) // 6


def triangular(n: int) -> int:
    """Returns the nth triangle number, or the sum of the natural numbers up to
    and including n.
    """
    return n * (n + 1) // 2
