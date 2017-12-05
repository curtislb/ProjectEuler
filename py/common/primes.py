#!/usr/bin/env python3

"""primes.py

Functions for finding and identifying prime numbers.
"""

__author__ = 'Curtis Belmonte'

import math
from typing import Optional, Sequence

import common.arrays as arrs
import common.sequences as seqs


# Currently computed prime number terms (in sorted order)
_prime_sequence = [2]


def _compute_primes(n: int) -> None:
    """Precomputes and stores at least the first n prime numbers."""
    
    prime_count = len(_prime_sequence)

    # have the first n primes already been computed?
    if n < prime_count:
        return

    # TODO: implement incremental sieve?

    # based on analysis of OEIS data set A006880 and empirical time tests
    estimate = 100 if n <= 25 else int(n * math.log(n) * 1.05 + n * 0.87)
    increment = int(round(n / math.log(n)))

    # compute primes up to estimate, then step forward until n are found
    i = estimate
    while len(_prime_sequence) < n:
        _compute_primes_up_to(i)
        i += increment


def _compute_primes_up_to(n: int) -> None:
    """Precomputes and stores the prime numbers up to n."""

    # have the numbers up to n already been computed?
    prime_max = _prime_sequence[-1]
    if prime_max >= n:
        return

    # prepare sieve of Eratosthenes for numbers prime_max + 1 to n
    sieve_size = n - prime_max
    sieve = [True] * sieve_size

    # sift out composite numbers using previously computed primes
    prime_count = len(_prime_sequence)
    for i in range(prime_count):
        rho = _prime_sequence[i]
        rho_start = seqs.next_multiple(rho, prime_max + 1)
        for j in range(rho_start, n + 1, rho):
            sieve[j - prime_max - 1] = False

    # sift out remaining composite numbers with newly found primes
    for i in range(sieve_size):
        if sieve[i]:
            rho = i + prime_max + 1
            _prime_sequence.append(rho)
            for j in range(rho**2 - prime_max - 1, sieve_size, rho):
                sieve[j] = False


def count_prime_factors(
        n: int,
        prime_nums: Optional[Sequence[int]] = None) -> int:

    """Returns the number of distinct prime factors of the natural number n,
    using the given precomputed list of primes."""

    # generate list of primes up to n if none given
    if prime_nums is None:
        prime_nums = primes_up_to(n)

    # check if n is prime to avoid worst-case performance
    if arrs.binary_search(prime_nums, n) is not None:
        factor_count = 1
    else:
        factor_count = 0
        for prime_num in prime_nums:
            # have all prime factors of n been found?
            if n == 1:
                break

            # if prime divides n, increment count and divide it out of n
            if n % prime_num == 0:
                factor_count += 1
                while n % prime_num == 0:
                    n //= prime_num

    return factor_count


def is_prime(n: int) -> bool:
    """Determines if the natural number n is prime."""

    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3:
        return n > 1

    # check if multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    max_factor = int(math.sqrt(n))
    for i in range(5, max_factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def prime_factorization(n: int) -> Sequence[Sequence[int]]:
    """Computes the prime factorization of the natural number n.
    
    Returns a list of base-exponent pairs containing each prime factor and
    its power in the prime factorization of n."""

    i = 2
    factorization = []
    while i <= int(math.sqrt(n)):
        # compute power of i in factorization
        factor = [i, 0]
        div, mod = divmod(n, i)
        while mod == 0:
            n = div
            factor[1] += 1
            div, mod = divmod(n, i)

        # add factor to factorization if necessary
        if factor[1] > 0:
            factorization.append(factor)

        i += 1

    # no more prime factors above sqrt(n)
    if n > 1:
        factorization.append([n, 1])

    return factorization


def prime(n: int) -> int:
    """Returns the nth prime number."""
    _compute_primes(n)
    return _prime_sequence[n - 1]


def primes(n: int) -> Sequence[int]:
    """Returns the first n prime numbers in sorted order."""
    _compute_primes(n)
    return _prime_sequence[:n]


def primes_up_to(n: int) -> Sequence[int]:
    """Returns the prime numbers up to p in sorted order."""

    _compute_primes_up_to(n)

    # return whole sequence if all primes <= n
    if _prime_sequence[-1] <= n:
        return _prime_sequence[:]

    # find the index of the last prime <= n
    i = 0
    while _prime_sequence[i] <= n:
        i += 1

    return _prime_sequence[:i]
