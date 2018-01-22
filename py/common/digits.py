#!/usr/bin/env python3

"""digits.py

Functions for manipulating and operating on numerical digits.
"""

__author__ = 'Curtis Belmonte'

import itertools
import string
from typing import Callable, Iterable, Optional, Sequence, Set, Union


def concat_digits(digit_list: Iterable[Union[int, str]], base: int = 10) -> int:
    """Concatenates the digits in digit_list in order and returns the result.

    If provided, base determines the numeric base in which the digits of
    digit_list should be interpreted when deriving the resulting integer.
    """
    return int(''.join(map(str, digit_list)), base)


def concat_numbers(n: int, m: int) -> int:
    """Concatenates two natural numbers n and m and returns the result."""
    return int('{0:d}{1:d}'.format(n, m))


def count_digits(n: int) -> int:
    """Returns the number of digits of the natural number n."""
    return len(str(n))


def decimal_digits(x: float, precision: int) -> int:
    """Forms an integer of the digits of x rounded to precision decimal places.

    If x <= -1 or x >= 1, the resulting integer will contain the additional
    high-order digits of x preceding the decimal point.

    If x < 0, the resulting integer will be negative.
    """
    return int(round(x, precision) * 10**precision)


def digit_counts(n: int, base: int = 10) -> Sequence[int]:
    """Returns a sequence with the count of each digit of n in the given base.

    The result is an integer sequence of length base, where each entry
    represents the number of times each digit from 0 to base - 1 appears in the
    given base representation of the natural number n.
    """

    counts = [0] * base
    while n != 0:
        n, digit = divmod(n, base)
        counts[digit] += 1

    return counts


def digit_function_sum(
        n: int, func: Callable[[int], int], base: int = 10) -> int:

    """Sums the result of func applied to each digit of n in the given base."""

    total = 0
    while n != 0:
        n, digit = divmod(n, base)
        total += func(digit)

    return total


def digit_permutations(n: int) -> Set[int]:
    """Returns all unique digit permutations of the natural number n.

    The resulting integer set excludes any permutations with leading zeros.
    """

    perms = set()
    for perm_tuple in itertools.permutations(str(n)):
        if perm_tuple[0] != '0':
            perms.add(int(''.join(perm_tuple)))

    return perms


def digit_rotations(n: int) -> Set[int]:
    """Returns all unique digit rotations of the natural number n."""

    n_str = str(n)
    rotations = set()
    for i in range(len(n_str)):
        rotations.add(int(n_str[i:] + n_str[:i]))

    return rotations


def digit_truncations_left(n: int) -> Set[int]:
    """Returns all left-to-right digit truncations of the natural number n."""

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
    """Returns all right-to-left digit truncations of the natural number n."""

    truncations = set()

    # remove each rightmost digit from n
    while n != 0:
        truncations.add(n)
        n //= 10

    return truncations


def digits(n: int, base: int = 10) -> Sequence[int]:
    """Returns the digits of the natural number n as a sequence."""

    digit_list = []

    while n != 0:
        n, digit = divmod(n, base)
        digit_list.append(digit)

    return digit_list[::-1]


def get_digit(n: int, digit: int) -> int:
    """Returns the given decimal digit of the natural number n."""
    return int(str(n)[digit - 1])


def int_to_base(
        n: int,
        base: int,
        numerals: Sequence[str] = '0123456789' + string.ascii_lowercase) -> str:

    """Forms a string representation of the natural number n in the given base.

    The sequence numerals defines the set of strings that are used to represent
    each digit value from 0 to base - 1. Thus, len(numerals) must be >= base.

    Adapted from: http://stackoverflow.com/questions/2267362/
    """

    # base case: 0 is represented as numerals[0] in any base
    if n == 0:
        return numerals[0]

    # compute the low-order digit and recurse to compute higher order digits
    div, mod = divmod(n, base)
    return int_to_base(div, base, numerals).lstrip(numerals[0]) + numerals[mod]


def is_bouncy(n: int) -> bool:
    """Determines if the natural number n is a bouncy number.

    A number is bouncy iff its digits are in neither non-decreasing or
    non-increasing order. That is, they increase and then decrease, or decrease
    and then increase.
    """

    n_digits = digits(n)
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
    """Determines if the natural number n is a palindrome in the given base."""

    # create a copy of n and number to hold its reversed value
    n_copy = n
    reverse_n = 0

    # append each of the digits of n to reverse_n in reverse order
    while n_copy != 0:
        n_copy, digit = divmod(n_copy, base)
        reverse_n = (reverse_n * base) + digit

    # compare the original n to its reversed version
    return n == reverse_n


def make_palindrome(n: int, base: int = 10, odd_length: bool = False) -> int:
    """Returns a palindrome in the given base formed from the natural number n.

    If odd_length is True, the generated palindrome will have an odd number of
    digits in the given base; otherwise, it will have an even number of digits.

    Adapted from: https://projecteuler.net/overview=036
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
    """Returns a string with each of the digits from first to last in order."""
    return ''.join(map(str, range(first, last + 1)))


def sum_digits(n: int, base: int = 10) -> int:
    """Sums the digits of the natural number n in the given base."""
    digit_sum = 0
    while n != 0:
        n, digit = divmod(n, base)
        digit_sum += digit
    return digit_sum


def sum_keep_digits(m: int, n: int, d: Optional[int] = None) -> int:
    """Returns the last d decimal digits of the sum of m and n.

    If d is None, the result is the entire sum m + n.
    """
    if d is None:
        return m + n
    else:
        mod = 10**d
        return ((m % mod) + (n % mod)) % mod
