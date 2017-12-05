#!/usr/bin/env python3

"""digits.py

Functions for manipulating and operating on numerical digits.
"""

__author__ = 'Curtis Belmonte'

import itertools
from typing import *


def concat_digits(digit_list: Iterable[int], base: int = 10) -> int:
    """Returns the integer that results from concatenating digits in order."""
    return int(''.join(map(str, digit_list)), base)


def concat_numbers(n: int, m: int) -> int:
    """Returns the number that results from concatenating the natural numbers
    n and m, in that order."""
    return int('{0:d}{1:d}'.format(n, m))


def count_digits(n: int) -> int:
    """Returns the number of digits of the natural number n."""
    return len(str(n))


def digit_counts(n: int) -> Sequence[int]:
    """Returns a sequence with the count of each decimal digit in the natural
    number n."""

    counts = [0] * 10
    while n != 0:
        n, digit = divmod(n, 10)
        counts[digit] += 1

    return counts


def digit_function_sum(n: int, func: Callable[[int], int]) -> int:
    """Returns the sum of the results of applying function to each of the
    digits of the natural number n."""

    total = 0
    while n != 0:
        n, digit = divmod(n, 10)
        total += func(digit)

    return total


def digit_permutations(n: int) -> Set[int]:
    """Returns all unique digit permutations of the natural number n,
    excluding permutations with leading zeros."""

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
    """Returns all unique left-to-right digit truncations of the natural number
    n."""

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
        numerals: Sequence[str] = '0123456789abcdefghijklmnopqrstuvwxyz')\
        -> str:

    """Returns the string representation of the natural number n in the given
    base using the given set of numerals.

    Adapted from: http://stackoverflow.com/questions/2267362/"""

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
    and then increase."""

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

    If the odd_length flag is set to True, the generated palindrome will have
    an odd number of digits when written in the given base; otherwise, it will
    have an even number of digits.

    Adapted from: https://projecteuler.net/overview=036"""

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


def sum_digits(n: int) -> int:
    """Returns the sum of the decimal digits of the natural number n."""
    digit_sum = 0
    while n != 0:
        n, digit = divmod(n, 10)
        digit_sum += digit
    return digit_sum


def sum_keep_digits(m: int, n: int, d: Optional[int] = None) -> int:
    """Returns the last d decimal digits of the sum of m and n. If d is None,
    returns the entire sum."""
    if d is None:
        return m + n
    else:
        mod = 10**d
        return ((m % mod) + (n % mod)) % mod
