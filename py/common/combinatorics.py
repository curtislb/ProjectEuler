#!/usr/bin/env python3

"""combinatorics.py



Author: Curtis Belmonte
"""

import common.sequences as seqs


# Currently computed factorial terms (in sorted order)
_factorial_sequence = [1, 1]


def _compute_factorial(n):
    """Precomputes and stores the factorial terms up to n!."""

    fact_count = len(_factorial_sequence)

    # have the terms up to n! already been computed?
    if n < fact_count:
        return

    # compute numbers iteratively from existing sequence
    product = _factorial_sequence[-1]
    for i in range(fact_count, n + 1):
        product *= i
        _factorial_sequence.append(product)


def choose(n, k):
    """Returns the number of ways to choose k objects from a group of n."""
    return permute(n, k) // factorial(k)


def combination_sums(total, terms):
    """Returns the number of unique combinations of terms that sum to total.

    Both total and each term in terms must be a natural number."""

    if total <= 0:
        raise ValueError("Argument 'total' must be a natural number")
    for term in terms:
        if term <= 0:
            raise ValueError("Each term in 'terms' must be a natural number")

    # initialize the combination array
    combos = [0] * (total + 1)
    combos[0] = 1

    # dynamically compute combinations by summing combination dependencies
    for i, term in enumerate(terms):
        for j in range(term, total + 1):
            combos[j] += combos[j - terms[i]]

    return combos[total]


def factorial(n):
    """Returns the value of n! = n * (n - 1) * ... * 1."""
    _compute_factorial(n)
    return _factorial_sequence[n]


def permute(n, k):
    """Returns the number of permutations of k objects from a group of n."""

    # if faster, compute n! and (n - k)! and return their quotient
    fact_count = len(_factorial_sequence)
    if n - fact_count <= k:
        return factorial(n) // factorial(n - k)

    # compute the product (n - k + 1) * (n - k + 2) * ... * n
    return seqs.arithmetic_product(n - k + 1, k)
