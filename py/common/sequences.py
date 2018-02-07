#!/usr/bin/env python3

"""sequences.py

Functions for producing and operating on numerical sequences.
"""

__author__ = 'Curtis Belmonte'

import functools
import itertools
import math
import operator
from typing import (
    Callable,
    Dict,
    Iterable,
    Iterator,
    Sequence,
    Set,
)

import common.arithmetic as arith


def _compute_chain_length(
        lengths: Dict[int, int],
        n: int,
        step: Callable[[int], int],
        is_valid: Callable[[int], bool],
        invalid_set: Set[int]) -> None:

    """Single-chain helper function for compute_chain_lengths.

    Updates lengths and invalid_set based on the sequence starting from n.
    """

    # initialize map of terms to their positions in sequence
    terms = {} # type: Dict[int, int]

    while True:
        # if chain is invalid, mark all terms accordingly
        if not is_valid(n) or n in invalid_set or n in lengths:
            for n in terms:
                invalid_set.add(n)
            return

        # if completed chain, set length for all terms in it
        elif n in terms:
            index = terms[n]
            length = len(terms) - index
            for n, i in terms.items():
                invalid_set.add(n)
                if i >= index:
                    lengths[n] = length
            return

        # otherwise, continue building the current chain
        else:
            terms[n] = len(terms)

        # advance to next number in chain
        n = step(n)


def arithmetic_product(a: int, n: int, d: int = 1) -> int:
    """Returns the product of the arithmetic sequence with parameters a, n, d.

    a: The first term in the sequence
    n: The total number of terms in the sequence
    d: The difference between any two terms in the sequence
    """

    return functools.reduce(operator.mul, range(a, a + n * d, d), 1)


def arithmetic_series(a: int, n: int, d: int = 1) -> int:
    """Returns the sum of the arithmetic sequence with parameters a, n, d.

    a: The first term in the sequence
    n: The total number of terms in the sequence
    d: The difference between any two terms in the sequence
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

    lengths: The dict to be populated, mapping each term to its chain length
    values: An iterable of all valid starting terms for a chain
    step: For any term n, step(n) gives the next term in the chain
    is_valid: is_valid(n) should return True iff n is a valid chain member
    """

    invalid_set = set() # type: Set[int]
    for n in values:
        _compute_chain_length(lengths, n, step, is_valid, invalid_set)


def fibonacci(n: int) -> int:
    """Returns the nth Fibonacci number, with F(0) = F(1) = 1."""
    return next(itertools.islice(generate_fibonacci(), n, n + 1))


def generate_fibonacci() -> Iterator[int]:
    """Yields each number in the Fibonacci sequence, beginning with 1, 1."""
    fib_prev = 0
    fib_curr = 1
    while True:
        yield fib_curr
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr


def generate_products(factors: Sequence[int], cache_capacity: int = 1000)\
        -> Iterator[int]:

    """Yields all distinct products of powers of factors in increasing order.

    Generates an infinite sequence of integers, starting with 1. If provided,
    cache_capacity determines the maximum size of the internal list used for
    caching previous products.

    Adapted from: https://rosettacode.org/wiki/Hamming_numbers#Python
    """

    # initialize product, cache, and next multiples
    product = 1
    product_cache = [product]
    indices = [0] * len(factors)
    multiples = [x * product_cache[i] for x, i in zip(factors, indices)]
    yield product

    while True:
        # poll next product and update list of next multiples
        product = min(multiples)
        product_cache.append(product)
        for i, (m, d, j) in enumerate(zip(multiples, factors, indices)):
            if m == product:
                j += 1
                indices[i] = j
                multiples[i] = d * product_cache[j]

        # trim the cache if it's over capacity
        min_index = min(indices)
        if min_index >= cache_capacity:
            del product_cache[:min_index]
            indices = [i - min_index for i in indices]

        yield product


def hexagonal(n: int) -> int:
    """Returns the nth hexagonal number, starting with 1."""
    return n * (2 * n - 1)


def is_fibonacci(n: int) -> bool:
    """Determines if the natural number n is a Fibonacci number."""
    if n < 2**52:
        # use arithmetic test if within floating-point precision
        term = 5 * n**2
        return is_square(term + 4) or is_square(term - 4)
    else:
        # generate Fibonacci numbers until n is found or exceeded
        for fib_num in generate_fibonacci():
            if fib_num >= n:
                return fib_num == n


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

    Specifically, returns True iff n = m^p for some natural number m.
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
    """Returns the nth pentagonal number, starting with 1."""
    return n * (3 * n - 1) // 2


def sum_of_squares(n: int) -> int:
    """Returns the sum of the squares of the first n natural numbers."""
    return (2 * n**3 + 3 * n**2 + n) // 6


def triangular(n: int) -> int:
    """Returns the nth triangle number, starting with 1.

    The resulting value is also the sum of the first n natural numbers.
    """

    return n * (n + 1) // 2
