#!/usr/bin/env python3

"""sequences.py



Author: Curtis Belmonte
"""

import functools
import operator
import math

import common.arithmetic as arith


# Currently computed terms of the Fibonacci sequence (in sorted order)
_fibonacci_sequence = [1, 1]


def _compute_chain_length(lengths, n, incr, is_valid, invalid_set, terms=None):
    """Recursive helper function for compute_chain_lengths that updates lengths
    with appropriate chain lengths starting from n."""

    if terms is None:
        terms = {}

    # if chain is invalid, mark all terms accordingly
    if not is_valid(n) or n in invalid_set or n in lengths:
        for term in terms:
            invalid_set.add(term)

    # if completed chain, set length for all terms in it and invalidate others
    elif n in terms:
        index = terms[n]
        length = len(terms) - index
        for term, i in terms.items():
            if i < index:
                invalid_set.add(term)
            else:
                lengths[term] = length

    # otherwise, continue building the current chain
    else:
        terms[n] = len(terms)
        _compute_chain_length(
            lengths,
            incr(n),
            incr,
            is_valid,
            invalid_set,
            terms)


def _compute_fibonacci(n):
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


def arithmetic_product(a, n, d=1):
    """Returns the product of the arithmetic sequence with first term a, number
    of terms n, and difference between terms d."""
    return functools.reduce(operator.mul, range(a, a + n * d, d), 1)


def arithmetic_series(a, n, d=1):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def collatz_step(n):
    """Returns the next number in the Collatz sequence following n."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def compute_chain_lengths(lengths, values, incr, is_valid=lambda x: True):
    """Populates lengths with chain lengths starting from each term in values.

    lengths   the dict to be populated, mapping each term to its chain length
    values    an iterable of all valid starting terms for a chain
    incr      for any term n, incr(n) gives the next term in the chain
    is_valid  is_valid(n) returns True iff n is a valid chain member
    """

    invalid_set = set()
    for n in values:
        _compute_chain_length(lengths, n, incr, is_valid, invalid_set)


def fibonacci(n):
    """Returns the nth Fibonacci number, with F(0) = F(1) = 1."""
    _compute_fibonacci(n)
    return _fibonacci_sequence[n]


def hexagonal(n):
    """Returns the nth hexagonal number."""
    return n * (2 * n - 1)


def is_hexagonal(n):
    """Determines if the natural number n is a hexagonal number."""
    radical_sum = 1 + (8 * n)
    return is_square(radical_sum) and arith.int_sqrt(radical_sum) % 4 == 3


def is_pentagonal(n):
    """Determines if the natural number n is a pentagonal number."""
    radical_sum = 1 + (24 * n)
    return is_square(radical_sum) and arith.int_sqrt(radical_sum) % 6 == 5


def is_power(n, p):
    """Determines if the natural number n is a perfect power with exponent p.

    Specifically, returns True iff n = m**p for some natural number m."""

    root_n = n**(1 / p)
    lo_power = (int(root_n))**p
    hi_power = (int(math.ceil(root_n)))**p
    return lo_power == n or hi_power == n


def is_square(n):
    """Determines if the natural number n is a perfect square."""
    sqrt_n = math.sqrt(n)
    lo_power = (int(sqrt_n))**2
    hi_power = (int(math.ceil(sqrt_n)))**2
    return lo_power == n or hi_power == n


def is_triangular(n):
    """Determines if the natural number n is a triangle number."""
    return is_square(8 * n + 1)


def next_multiple(n, min_val):
    """Returns the next multiple of the natural number n >= min_val."""
    return min_val + ((n - (min_val % n)) % n)


def pentagonal(n):
    """Returns the nth pentagonal number."""
    return n * (3 * n - 1) // 2


def sum_of_squares(n):
    """Returns the sum of the squares of the first n natural numbers."""
    return (2 * n**3 + 3 * n**2 + n) // 6


def triangular(n):
    """Returns the nth triangle number, or the sum of the natural numbers up to
    and including n."""
    return n * (n + 1) // 2
