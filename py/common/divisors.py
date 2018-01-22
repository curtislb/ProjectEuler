#!/usr/bin/env python3

"""divisors.py

Functions for determining and operating on the divisors of natural numbers.
"""

__author__ = 'Curtis Belmonte'

import functools
import operator
from typing import Dict, Iterable, List, Optional, Sequence

import common.primes as prime


def count_divisors(n: int) -> int:
    """Returns the number of divisors of the natural number n."""
    return count_power_divisors(n, 1)


def count_divisors_up_to(n: int) -> Sequence[int]:
    """Returns a sequence of divisor counts for integers 0 to n, inclusive."""

    # initialize counts for integers 0 to n
    divisor_counts = [1] * (n + 1)
    divisor_counts[0] = 0

    # increment counts for multiples of each number up to n
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            divisor_counts[j] += 1

    return divisor_counts


def count_power_divisors(n: int, p: int) -> int:
    """Returns the number of divisors of n^p, for natural numbers n and p."""

    # compute product of (p*a + 1) for each prime factor power a of n
    divisor_count = 1
    factorization = prime.prime_factorization(n)
    for _, power in factorization:
        divisor_count *= (p * power) + 1

    return divisor_count


def gcd(m: int, n: int) -> int:
    """Returns the greatest common divisor of the natural numbers m and n."""
    while n != 0:
        m, n = n, m % n
    return m


def is_coprime_pair(m: int, n: int) -> int:
    """Determines if the natural numbers m and n are relatively prime."""
    return gcd(m, n) == 1


def lcm(m: int, n: int) -> int:
    """Returns the least common multiple of the natural numbers m and n."""
    return m * n // gcd(m, n)


def lcm_all(nums: Iterable[int]) -> int:
    """Returns the least common multiple of all natural numbers in nums."""

    max_powers = {} # type: Dict[int, int]
    for num in nums:
        # compute powers of unique prime factors of the current number
        factorization = prime.prime_factorization(num)
        for factor, power in factorization:
            if (factor in max_powers and power > max_powers[factor]
                    or factor not in max_powers):
                max_powers[factor] = power

    # return the product of prime factors raised to their highest powers
    product = 1
    for factor in max_powers:
        product *= factor**max_powers[factor]
    return product


def radical(n: int) -> int:
    """Returns the product of the distinct prime factors of n."""

    # find the distinct prime factors of n
    factors = [factor for (factor, _) in prime.prime_factorization(n)]

    # multiply factors to find their product
    return functools.reduce(operator.mul, factors, 1)


def sum_divisors(n: int) -> int:
    """Returns the sum of the divisors of the natural number n."""

    factorization = prime.prime_factorization(n)

    # compute sum of divisors of n as the product of (p^(a+1) - 1)/(p - 1) for
    # each prime factor p^a of n
    # Source: http://mathschallenge.net/?section=faq&ref=number/sum_of_divisors
    product = 1
    for factor, power in factorization:
        product *= (factor**(power + 1) - 1) // (factor - 1)
    return product


def sum_proper_divisors(n: int) -> int:
    """Returns the sum of the proper divisors of the natural number n."""
    return sum_divisors(n) - n


def totient(n: int, prime_factors: Optional[Iterable[int]] = None) -> int:
    """Returns the number of integers between 0 and n relatively prime to n.

    If provided, prime_factors must be an ordered iterable of the prime factors
    of n. If prime_factors is None, it will be calculated by this function.
    """

    # determine prime factors of n if not provided
    if prime_factors is None:
        prime_factors = [factor for (factor, _)
                         in prime.prime_factorization(n)]

    # calculate totient using Euler's product formula
    numer = n
    denom = 1
    for p in prime_factors:
        numer *= p - 1
        denom *= p

    return numer // denom


def totients_up_to(n: int) -> Sequence[int]:
    """Returns the values of Euler's totient function for the integers 2 to n.

    The result is an integer sequence of length n - 2 where the ith entry is
    the number of integers between 0 and i + 2 relatively prime to i + 2.
    """

    # initialize sieve of Eratosthenes up to n
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    prime_factors = [[] for _ in range(n + 1)] # type: List[List[int]]

    # run sieve algorithm, keeping track of prime factors
    for curr_num in range(2, n + 1):
        if sieve[curr_num]:
            prime_factors[curr_num].append(curr_num)
            for multiple in range(2 * curr_num, n + 1, curr_num):
                sieve[multiple] = False
                prime_factors[multiple].append(curr_num)

    # calculate each totient using its prime factors
    totients = []
    for i in range(2, len(prime_factors)):
        totients.append(totient(i, prime_factors[i]))

    return totients
