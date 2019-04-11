#!/usr/bin/env python3

"""Common library for finding and working with integer divisors.

This module provides function for determining and operating on the divisors (or
factors) of positive integers. Examples include counting the divisors of a
number, checking if two numbers are relatively prime, and finding the lowest
common multiple of two or more numbers.
"""

import functools
import operator
from typing import Dict, Iterable, List, Optional, Sequence

import common.primes as prime


def count_divisors(n: int) -> int:
    """Counts the positive integer divisors of a number.

    Args:
        n: A positive integer value.

    Returns:
        The number of positive integers that evenly divide ``n``.

    See Also:
        :func:`count_divisors_up_to`
            For counting the divisors of all numbers up to and including a
            number.
        :func:`count_power_divisors`
            For counting the divisors of the power of a number.
    """
    return count_power_divisors(n, 1)


def count_divisors_up_to(n: int) -> Sequence[int]:
    """Finds the divisor counts of the first ``n`` non-negative integers.

    Args:
        n: A non-negative integer value.

    Returns:
        An integer sequence of length ``n + 1``, where the value at each index
        ``m`` is the number of positive integers that evenly divide ``m``.

    See Also:
        :func:`count_divisors`
            For counting the divisors of a single number.
        :func:`count_power_divisors`
            For counting the divisors of the power of a single number.
    """

    # initialize counts for integers 0 to n
    divisor_counts = [1] * (n + 1)
    divisor_counts[0] = 0

    # increment counts for multiples of each number up to n
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            divisor_counts[j] += 1

    return divisor_counts


def count_power_divisors(n: int, p: int) -> int:
    """Counts the positive integer divisors of a number raised to a power.

    Args:
        n: A positive integer value.
        p: The non-negative integer power to which ``n`` will be raised.

    Returns:
        The number of positive integers that evenly divide ``n^p``.

    See Also:
        :func:`count_divisors`
            For counting the divisors of any number.
        :func:`count_divisors_up_to`
            For counting the divisors of all numbers up to and including a
            number.
    """

    # compute product of (p*a + 1) for each prime factor power a of n
    divisor_count = 1
    factorization = prime.prime_factorization(n)
    for _, power in factorization:
        divisor_count *= (p * power) + 1

    return divisor_count


def gcd(m: int, n: int) -> int:
    """Finds the greatest common divisor of two numbers.

    Args:
        m: A positive integer value.
        n: A second positive integer value.

    Returns:
        The greatest positive integer that evenly divides both ``m`` and ``n``.
    """
    while n != 0:
        m, n = n, m % n
    return m


def is_coprime_pair(m: int, n: int) -> int:
    """Checks if two numbers are relatively prime.

    Args:
        m: A positive integer value.
        n: A second positive integer value.

    Returns:
        ``True`` if ``m`` and ``n`` share no positive integer divisors other
        than 1, or ``False`` otherwise.
    """
    return gcd(m, n) == 1


def lcm(m: int, n: int) -> int:
    """Returns the least common multiple of two numbers.

    Args:
        m: A positive integer value.
        n: A second positive integer value

    Returns:
        The lowest positive integer that can be evenly divided by both ``m``
        and ``n``.

    See Also:
        :func:`lcm_all`
            For finding the least common multiple of three or more numbers.
    """
    return m * n // gcd(m, n)


def lcm_all(nums: Iterable[int]) -> int:
    """Returns the least common multiple of a collection of numbers.

    Args:
        nums: An iterable sequence of positive integers.

    Returns:
        The lowest positive integer that can be evenly divided by all numbers
        in ``nums``.

    See Also:
        :func:`lcm`
            For finding the least common multiple of exactly two numbers.
    """

    max_powers: Dict[int, int] = {}
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
    """Finds the product of the distinct prime factors of a number.

    Args:
        n: A positive integer value.

    Returns:
        The product of all distinct prime numbers that evenly divide ``n``.
    """

    # find the distinct prime factors of n
    factors = [factor for (factor, _) in prime.prime_factorization(n)]

    # multiply factors to find their product
    return functools.reduce(operator.mul, factors, 1)


def sum_divisors(n: int) -> int:
    """Finds the sum of the positive integer divisors of a number.

    Args:
        n: A positive integer value.

    Returns:
        The sum that results from adding all of the positive integer values
        that evenly divide ``n``.

    See Also:
        :func:`sum_proper_divisors`
            For summing only the proper divisors of a number.
    """

    factorization = prime.prime_factorization(n)

    # compute sum of divisors of n as the product of (p^(a+1) - 1)/(p - 1) for
    # each prime factor p^a of n
    # Source: http://mathschallenge.net/?section=faq&ref=number/sum_of_divisors
    product = 1
    for factor, power in factorization:
        product *= (factor**(power + 1) - 1) // (factor - 1)
    return product


def sum_proper_divisors(n: int) -> int:
    """Finds the sum of the proper divisors of a number.

    Args:
        n: A positive integer value.

    Returns:
        The sum that results from adding all positive integer values less than
        ``n`` that evenly divide ``n``.
    """
    return sum_divisors(n) - n


def totient(n: int, prime_factors: Optional[Iterable[int]] = None) -> int:
    """Counts the relatively prime positive integers below a number.

    Args:
        n: A positive integer value.
        prime_factors: If provided, must be an ordered iterable of the prime
            factors of ``n``. If ``None``, the prime factors of ``n`` will be
            calculated by this function (at a cost to performance).

    Returns:
        The number of integers from 1 to ``n``, inclusive, which are relatively
        prime to ``n``.

    See Also:
        :func:`totients_up_to`
            For finding the totients of all numbers from 2 up to and including
            a number.
    """

    # determine prime factors of n if not provided
    if prime_factors is None:
        prime_factors = [
            factor for (factor, _) in prime.prime_factorization(n)
        ]

    # calculate totient using Euler's product formula
    numer = n
    denom = 1
    for p in prime_factors:
        numer *= p - 1
        denom *= p

    return numer // denom


def totients_up_to(n: int) -> Sequence[int]:
    """Calculates Euler's totient function for the integers from 2 to ``n``.

    Args:
        n: A positive integer value greater than or equal to 2.

    Returns:
        An integer sequence of length ``n - 1`` where the value at each index
        ``m`` is the number of integers from 1 to ``m + 2`` that are relatively
        prime to ``m + 2``.

    See Also:
        :func:`totient`
            For finding the totient of a single number.
    """

    # initialize sieve of Eratosthenes up to n
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    prime_factors: List[List[int]] = [[] for _ in range(n + 1)]

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
