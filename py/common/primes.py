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

    # set estimate and increment values according to PNT
    approx_gap = _estimate_prime_gap(n)
    estimate = 100 if n <= 25 else int(n * approx_gap)
    increment = int(approx_gap)

    # compute primes up to estimate, then step forward until n are found
    while len(_prime_sequence) < n:
        _compute_primes_up_to(estimate)
        estimate += increment


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


def _estimate_prime_gap(n: int) -> float:
    """Returns an estimate for the average gap between the first n primes.

    Formula is based on a result derived from the Prime Number Theorem:
    https://en.wikipedia.org/wiki/Prime_number_theorem
    """

    log_n = math.log(n)
    log_log_n = math.log(log_n)
    log_n_sqr = log_n**2
    log_log_n_sqr = log_log_n**2
    return (log_n + log_log_n - 1 + (log_log_n - 2)/log_n
            - (log_log_n_sqr - 6 * log_log_n + 11)/(2 * log_n_sqr)
            + math.exp(1)/log_n_sqr)


def count_prime_factors(
        n: int,
        prime_nums: Optional[Sequence[int]] = None) -> int:

    """Returns the number of distinct prime factors of the natural number n.

    If provided, prime_nums must be an ordered sequence of prime numbers that
    contains at least the prime factors of n. If prime_factors is None, it will
    be calculated by this function.
    """

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
    its power in the prime factorization of n.
    """

    d = 2
    factorization = []
    while d <= int(math.sqrt(n)):
        # compute power of i in factorization
        factor = [d, 0]
        div, mod = divmod(n, d)
        while mod == 0:
            n = div
            factor[1] += 1
            div, mod = divmod(n, d)

        # add factor to factorization if necessary
        if factor[1] > 0:
            factorization.append(factor)

        d += 1

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
    """Returns a sequence of the prime numbers <= n in sorted order."""

    _compute_primes_up_to(n)

    # return whole sequence if all primes <= n
    if _prime_sequence[-1] <= n:
        return _prime_sequence[:]

    # find the index of the last prime <= n
    i = 0
    while _prime_sequence[i] <= n:
        i += 1

    return _prime_sequence[:i]


def primorials(n: int) -> Sequence[int]:
    """Returns the first n primorial numbers in sorted order.

    The result is a sequence of n integers where each kth term is the product
    of the first k prime numbers, for 1 <= k <= n.
    """
    _compute_primes(n)
    return arrs.cumulative_products(_prime_sequence[:n])
