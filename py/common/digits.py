#!/usr/bin/env python3

"""Common library for working with numerical digits.

This module provides functions for manipulating and operating on digits in
various bases. Examples include converting between numbers and their digit
representations, building and checking for palindromic numbers, and counting or
summing the digits of a number.
"""

import itertools
import string
from typing import Callable, Iterable, Sequence, Set, Union


def concat_numbers(n: int, m: int) -> int:
    """Concatenates two non-negative integers in base 10.

    Args:
        n: The non-negative integer that will be prepended to ``m``.
        m: The non-negative integer that will be appended to ``n``.

    Returns:
        An integer containing all base-10 digits of ``n`` (from most to least
        significant), followed by all base-10 digits of ``m``.
    """
    return int('{0:d}{1:d}'.format(n, m))


def count_digits(n: int) -> int:
    """Counts the digits of number in base 10.

    Args:
        n: A non-negative integer.

    Returns:
        The number of digits in the base-10 representation of ``n``.
    """
    return len(str(n))


def decimal_digits(x: float, precision: int) -> int:
    """Forms an integer from the base-10 digits of a floating-point number.

    Args:
        x: A floating point number, which may be negative.
        precision: The number of digits after the decimal point to include.

    Returns:
        An integer containing all base-10 digits of ``x`` before the decimal
        point, followed by ``precision`` digits after the decimal point in
        ``x``. If ``x < 0``, the resulting integer will be negative.
    """
    return int(round(x, precision) * 10**precision)


def digit_counts(n: int, base: int = 10) -> Sequence[int]:
    """Counts the occurrences of each possible digit in a number.

    Args:
        n: A positive integer value.
        base: The base in which ``n`` will be represented. Must be at least 2.

    Returns:
        An integer sequence of length ``base``, where each entry represents the
        number of times a digit from 0 to ``base - 1`` (in that order) appears
        in the given base representation of ``n``.
    """
    counts = [0] * base
    while n != 0:
        n, digit = divmod(n, base)
        counts[digit] += 1
    return counts


def digit_function_sum(
    n: int,
    func: Callable[[int], int],
    base: int = 10,
) -> int:
    """Sums the results of applying a function to each digit of a number.

    Args:
        n: A positive integer value.
        func: The function to be applied to each digit of ``n``.
        base: The base in which ``n`` will be represented. Must be at least 2.

    Returns:
        The sum obtained by applying ``func`` to each digit in the given base
        representation of ``n`` and adding the results.
    """
    total = 0
    while n != 0:
        n, digit = divmod(n, base)
        total += func(digit)
    return total


def digit_permutations(n: int) -> Set[int]:
    """Finds all unique digit permutations of a positive integer in base 10.

    Args:
        n: A positive integer value.

    Returns:
        A set of all distinct integers that result from reordering the digits
        in the base-10 representation of ``n``, excluding any permutations with
        leading zeros.
    """
    perms = set()
    for perm_tuple in itertools.permutations(str(n)):
        if perm_tuple[0] != '0':
            perms.add(int(''.join(perm_tuple)))
    return perms


def digit_rotations(n: int) -> Set[int]:
    """Finds all unique digit rotations of a positive integer in base 10.

    Args:
        n: A positive integer value.

    Returns:
        A set of all distinct integers that result from rotating the base-10
        digits of ``n``. A rotation is given by truncating the ``d`` least
        significant digits of ``n`` and prepending them to the resulting
        number, where ``d`` is any integer from 0 to the number of digits in
        the base-10 representation of ``n``, inclusive.
    """
    n_str = str(n)
    rotations = set()
    for i in range(len(n_str)):
        rotations.add(int(n_str[i:] + n_str[:i]))
    return rotations


def digit_truncations_left(n: int) -> Set[int]:
    """Finds all left-to-right digit truncations of a positive base-10 integer.

    Args:
        n: A positive integer value.

    Returns:
        A set of all distinct integers that result from removing the ``d`` most
        significant digits of ``n``, where ``d`` is any integer from 0 to the
        number of digits in the base-10 representation of ``n``, inclusive.
    """

    truncations = set()

    # prepend the digits of n from right to left to truncated
    truncated = 0
    factor_10 = 1
    while n != 0:
        n, digit = divmod(n, 10)
        truncated += digit * factor_10
        truncations.add(truncated)
        factor_10 *= 10

    return truncations


def digit_truncations_right(n: int) -> Set[int]:
    """Finds all right-to-left digit truncations of a positive base-10 integer.

    Args:
        n: A positive integer value.

    Returns:
        A set of all distinct integers that result from removing the ``d``
        least significant digits of ``n``, where ``d`` is any integer from 0 to
        the number of digits in the base-10 representation of ``n``, inclusive.
    """
    truncations = set()
    while n != 0:
        truncations.add(n)
        n //= 10
    return truncations


def get_digit(n: int, position: int) -> int:
    """Finds a particular base-10 digit of a non-negative integer.

    Args:
        n: A non-negative integer value.
        position: The index (starting from 1) of the desired digit.

    Returns:
        Returns a non-negative integer representing the digit at ``position``
        in ``n``, ordered from most significant (``position = 1``) to least
        significant (``position = count_digits(n)``).
    """
    return int(str(n)[position - 1])


def get_digits(n: int, base: int = 10) -> Sequence[int]:
    """Decomposes a positive integer into digit values in a given base.

    Args:
        n: A positive integer value.
        base: The base in which ``n`` will be represented. Must be at least 2.

    Returns:
        An integer sequence, where each entry represents the value of a single
        digit in the given base representation of ``n``, from most to least
        significant.
    """
    digit_list = []
    while n != 0:
        n, digit = divmod(n, base)
        digit_list.append(digit)
    return digit_list[::-1]


def int_to_base(
    n: int,
    base: int,
    numerals: Sequence[str] = '0123456789' + string.ascii_lowercase,
) -> str:
    """Forms a string representation of a non-negative integer in a given base.

    Args:
        n: A non-negative integer value.
        base: The base in which ``n`` will be represented. Must be a positive
            integer from 2 to ``len(numerals)``.
        numerals: A sequence of string tokens that will be used to represent
            the digits from 0 to ``base - 1`` in order.

    Returns:
        A string representation of ``n`` in the given base, where each digit is
        given by the corresponding value of ``numerals``.

    References:
        Adapted from http://stackoverflow.com/questions/2267362/.
    """

    # base case: 0 is represented as numerals[0] in any base
    if n == 0:
        return numerals[0]

    # compute the low-order digit and recurse to compute higher order digits
    div, mod = divmod(n, base)
    return int_to_base(div, base, numerals).lstrip(numerals[0]) + numerals[mod]


def is_bouncy(n: int) -> bool:
    """Checks if a positive integer is a bouncy number in base 10.

    Args:
        n: A positive integer value.

    Returns:
        ``False`` if the base-10 digits of ``n`` are in non-decreasing or
        non-increasing order, or ``True`` otherwise.
    """

    n_digits = get_digits(n)
    max_index = len(n_digits) - 1

    # search for first increasing or decreasing consecutive digit pair
    i = 0
    while i < max_index and n_digits[i] == n_digits[i + 1]:
        i += 1

    # if all digit pairs are equal, number is not bouncy
    if i == max_index:
        return False

    # check whether first non-equal pair is increasing or decreasing
    increasing = n_digits[i] < n_digits[i + 1]

    # determine if subsequent pairs are also increasing/decreasing
    i += 1
    while i < max_index:
        # if order is reversed, the number is bouncy
        if (increasing and n_digits[i] > n_digits[i + 1]
                or not increasing and n_digits[i] < n_digits[i + 1]):
            return True
        i += 1

    # number is increasing or decreasing
    return False


def is_palindrome(n: int, base: int = 10) -> bool:
    """Checks if a non-negative integer is a palindrome in a given base.

    Args:
        n: A non-negative integer value.
        base: The base in which ``n`` will be represented. Must be at least 2.

    Returns:
        ``True`` if ``n`` is a palindrome (its digits read the same forward and
        backward) in the given base, or ``False`` otherwise.
    """

    # create a copy of n and number to hold its reversed value
    n_copy = n
    reverse_n = 0

    # append each of the digits of n to reverse_n in reverse order
    while n_copy != 0:
        n_copy, digit = divmod(n_copy, base)
        reverse_n = (reverse_n * base) + digit

    # compare the original n to its reversed version
    return n == reverse_n


def join_digits(digits: Iterable[Union[int, str]], base: int = 10) -> int:
    """Forms an integer from a sequence of digits in a given base.

    Args:
        digits: An iterable sequence of digits, which can be either integers or
            characters, from most to least significant.
        base: The base representation of the resulting number. Must be at least
            2.

    Returns:
        An integer value whose digits (from most to least significant) are
        given by ``digits`` when written in the given base.
    """
    return int(''.join(map(str, digits)), base)


def make_palindrome(n: int, base: int = 10, odd_length: bool = False) -> int:
    """Forms a palindrome in the given base, using a positive integer seed.

    Args:
        n: A positive integer value.
        base: The base in which the resulting number will be a palindrome. Must
            be at least 2.
        odd_length: If ``True``, the resulting palindrome will contain
            ``2 * count_digits(n, base) - 1`` digits. If ``False``, the
            resulting palindrome will contain ``2 * count_digits(n, base)``
            digits.

    Returns:
        An integer containing an odd (if ``odd_length`` is ``True``) or even
        (if ``odd_length`` is ``False``) number of digits which read the same
        forward and backward in the given base.

    References:
        Adapted from https://projecteuler.net/overview=036.
    """

    # set beginning of palindrome to be the digits of n
    palindrome = n

    # remove final digit of n if palindrome should be odd in length
    if odd_length:
        n //= base

    # append each digit of n to palindrome in reverse order
    while n != 0:
        n, digit = divmod(n, base)
        palindrome = (palindrome * base) + digit

    return palindrome


def pandigital_string(first: int = 0, last: int = 9) -> str:
    """Forms a string containing all of the digits in a range.

    Args:
        first: A digit from 0 to 9 representing the start of the range. Must be
            less than or equal to ``last``.
        last: A digit from 0 to 9 representing the end of the range. Must be
            greater than or equal to ``first``.

    Returns:
        A string containing all of the digits from ``first`` to ``last`` in
        increasing order.
    """
    return ''.join(map(str, range(first, last + 1)))


def sum_digits(n: int, base: int = 10) -> int:
    """Sums the digits of a non-negative integer in a given base.

    Args:
        n: A non-negative integer value.
        base: The base in which ``n`` will be represented. Must be at least 2.
    """
    digit_sum = 0
    while n != 0:
        n, digit = divmod(n, base)
        digit_sum += digit
    return digit_sum


def sum_keep_digits(m: int, n: int, digit_count: int) -> int:
    """Finds the last base-10 digits of the sum of two non-negative integers.

    Args:
        m: The first non-negative integer addend.
        n: The second non-negative integer addend.
        digit_count: The number of least significant digits of the resulting
            sum that should be preserved.

    Returns:
        An integer consisting of the last ``digit_count`` digits (from most to
        least significant) of the sum ``m + n`` when written in base 10.
    """
    mod = 10**digit_count
    return ((m % mod) + (n % mod)) % mod
