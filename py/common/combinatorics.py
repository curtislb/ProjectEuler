#!/usr/bin/env python3

"""Common library for performing combinatoric, or counting, operations.

This module provides functions related to combinatorics, or so-called "counting
problems." Examples include counting the number of ways objects can be chosen
from a group and computing the factorial of a number.
"""

from typing import Sequence

import common.sequences as seqs


# Currently computed factorial terms (in sorted order)
_factorial_sequence = [1, 1]


def _compute_factorial(n: int) -> None:
    """Precomputes and stores the factorial terms up to ``n!``.

    Args:
        n: A non-negative integer value. After this function is called with
            ``n`` as an argument, subsequent calls to ``factorial(m)`` where
            ``0 <= m <= n`` will return the precomputed value in ``O(1)`` time.

    Warnings:
        Do not call this function directly. Use :func:`factorial` instead.
    """

    fact_count = len(_factorial_sequence)

    # have the terms up to n! already been computed?
    if n < fact_count:
        return

    # compute numbers iteratively from existing sequence
    product = _factorial_sequence[-1]
    for i in range(fact_count, n + 1):
        product *= i
        _factorial_sequence.append(product)


def _reset_factorial_cache() -> None:
    """Resets the currently cached list of factorial terms.

    Calling this function after :func:`_compute_factorial` will discard any
    values calculated by that function, so that subsequent calls to it or to
    :func:`factorial` will need to calculate them again.

    Warnings:
        This function is provided for testing and shouldn't be called directly.
    """
    global _factorial_sequence
    _factorial_sequence = [1, 1]


def choose(n: int, k: int) -> int:
    """Counts the number of ways to choose ``k`` objects from a group of ``n``.

    Args:
        n: A non-negative integer representing the size of a group.
        k: A non-negative integer representing the number of objects to choose.

    Returns:
        The number of distinct sets of ``k`` objects that can be chosen from a
        group of size ``n``, assuming all ``n`` objects are unique. Or,
        equivalently, the binomial coefficient ``n C k``.

    See Also:
        :func:`permute`, for when the order in which objects are chosen
        matters.
    """
    return permute(n, k) // factorial(k)


def combination_sums(total: int, terms: Sequence[int]) -> int:
    """Counts the number of combinations that sum to a given value.

    Args:
        total: A positive integer, representing the target sum.
        terms: A sequence of positive integer values that can be combined.

    Returns:
        The number of distinct combinations (with replacement) of values in
        ``terms`` that sum to give ``total``.

    Raises:
        ValueError: If ``total`` or any term in ``terms`` is negative or 0.
    """

    if total <= 0:
        raise ValueError("Argument 'total' must be a positive integer")
    for term in terms:
        if term <= 0:
            raise ValueError("Each term in 'terms' must be a positive integer")

    # initialize the combination array
    combos = [0] * (total + 1)
    combos[0] = 1

    # dynamically compute combinations by summing combination dependencies
    for i, term in enumerate(terms):
        for j in range(term, total + 1):
            combos[j] += combos[j - terms[i]]

    return combos[total]


def factorial(n: int) -> int:
    """Finds the factorial of a number.

    Args:
        n: A non-negative integer value.

    Returns:
        The value of ``n! = n * (n - 1)!``, where ``0! = 1``.
    """
    _compute_factorial(n)
    return _factorial_sequence[n]


def permute(n: int, k: int) -> int:
    """Counts the permutations of ``k`` objects from a group of ``n``.

    Args:
        n: A non-negative integer representing the size of a group.
        k: A non-negative integer representing the number of objects to choose.

    Returns:
        The number of distinct sequences of ``k`` objects that can be chosen
        from a group of size ``n``, assuming all ``n`` objects are unique.

    See Also:
        :func:`choose`, for when the order in which objects are chosen doesn't
        matter.
    """

    # no possible permutations if k > n
    if n < k:
        return 0

    # if faster, compute n! and (n - k)! and return their quotient
    fact_count = len(_factorial_sequence)
    if n - fact_count <= k:
        return factorial(n) // factorial(n - k)

    # compute the product (n - k + 1) * (n - k + 2) * ... * n
    return seqs.arithmetic_product(n - k + 1, k)
