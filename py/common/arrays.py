#!/usr/bin/env python3

"""Common library for working with one-dimensional arrays.

This module provides functions for operating on lists and other array-like
collections. Examples include finding the argmin/argmax of a sequence,
calculating the cumulative sums of a list of numbers, and checking if two
sequences are permutations of one another.
"""

import collections
from typing import Deque, Dict, Iterable, List, Mapping, Optional, Sequence

from common.typex import Comparable, T


def argmax(values: Sequence[Comparable]) -> int:
    """Finds the index of the maximum value in a sequence.

    Args:
        values: A sequence of values that can be compared to one another.

    Returns:
        The index (from 0 to ``len(values) - 1``) of the first element in
        ``values`` that is greater than or equal to all others.
    """
    max_index = 0
    max_value = values[0]
    for i, value in enumerate(values):
        if value > max_value:
            max_index = i
            max_value = value
    return max_index


def argmin(values: Sequence[Comparable]) -> int:
    """Finds the index of the minimum value in a sequence.

    Args:
        values: A sequence of values that can be compared to one another.

    Returns:
        The index (from 0 to ``len(values) - 1``) of the first element in
        ``values`` that is less than or equal to all others.
    """
    min_index = 0
    min_value = values[0]
    for i, value in enumerate(values):
        if value < min_value:
            min_index = i
            min_value = value
    return min_index


def binary_search(
    sorted_list: Sequence[Comparable],
    item: Comparable,
) -> Optional[int]:
    """Searches for the position of an element in a sorted sequence.

    Args:
        sorted_list: A sorted sequence of comparable values.
        item: The element to search for in ``sorted_list``.

    Returns:
        An index from 0 to ``len(sorted_list) - 1`` representing the position
        of ``item`` in ``sorted_list``, if present. If ``item`` is not present
        in ``sorted_list``, returns ``None`` instead.
    """

    # initialize search indices
    lo = 0
    hi = len(sorted_list)

    while lo < hi:
        # check middle element in list
        mid = lo + (hi - lo) // 2
        if item < sorted_list[mid]:
            # item is in first half of list or not at all
            hi = mid
        elif item > sorted_list[mid]:
            # item is in second half of list or not at all
            lo = mid + 1
        else:
            # item found at middle position in list
            return mid

    # item not found in list
    return None


def cumulative_partial_sums(nums: Sequence[int], limit: int) -> Sequence[int]:
    """Finds the partial cumulative sums of a sequence of integers.

    Args:
        nums: An arbitrary integer sequence.
        limit: The maximum number of terms to include in each partial sum.

    Returns:
        An integer sequence with length ``len(nums)``, where each term is the
        sum of up to the previous ``limit`` terms in ``nums``, including the
        term at the current index.
    """

    sums: List[int] = []
    terms: Deque[int] = collections.deque()

    total = 0
    for num in nums:
        total += num
        terms.append(num)

        if len(terms) > limit:
            total -= terms.popleft()

        sums.append(total)

    return sums


def cumulative_products(nums: Sequence[int]) -> Sequence[int]:
    """Finds the cumulative products of a sequence of integers.

    Args:
        nums: An arbitrary integer sequence.

    Returns:
        An integer sequence with length ``len(nums)``, where each term is the
        product of the current and all previous terms in ``nums``.
    """
    products: List[int] = []
    product = 1
    for num in nums:
        product *= num
        products.append(product)
    return products


def inverse_index_map(values: Sequence[T]) -> Mapping[T, int]:
    """Creates a map from each unique item in a sequence to its index.

    Args:
        values: A sequence of distinct values.

    Returns:
        A mapping from each item in ``values`` to its index in the sequence.

    See Also:
        :func:`inverse_index_map_all`, if ``values`` may contain duplicates.
    """
    inverse_map: Dict[T, int] = {}
    for i, value in enumerate(values):
        inverse_map[value] = i
    return inverse_map


def inverse_index_map_all(values: Sequence[T]) -> Mapping[T, Sequence[int]]:
    """Creates a map from each distinct item in a sequence to its indices.

    Args:
        values: A sequence of distinct values.

    Returns:
        A mapping from each distinct item in ``values`` to a sequence of all
        indices in ``values`` at which it appears.

    See Also:
        :func:`inverse_index_map`, if ``values`` contains no duplicates.
    """
    inverse_map: Dict[T, List[int]] = collections.defaultdict(list)
    for i, value in enumerate(values):
        inverse_map[value].append(i)
    return inverse_map


def is_permutation(
    iter_a: Iterable[T],
    iter_b: Iterable[T],
    compare_counts: bool = False
) -> bool:
    """Checks if two iterables are permutations of one another.

    Args:
        iter_a: The first iterable to be compared.
        iter_b: The second iterable to be compared.
        compare_counts: If ``iter_a`` and ``iter_b`` have the same length, this
            flag determines how they will be compared. If ``True``, the counts
            of items in the two iterables will be compared. If ``False``,
            sorted copies of the iterables will be compared.

    Returns:
        ``True`` if ``iter_a`` is a permutation of ``iter_b`` (and vice-versa),
        or ``False`` otherwise.
    """

    # convert iterables to lists if necessary
    list_a: List = iter_a if isinstance(iter_a, list) else list(iter_a)
    list_b: List = iter_b if isinstance(iter_b, list) else list(iter_b)

    # if lengths of a and b are different, they cannot be permutations
    if len(list_a) != len(list_b):
        return False

    if compare_counts:
        # check if a and b contain the same numbers of the same items
        for item in set(list_a):
            if list_a.count(item) != list_b.count(item):
                return False
        return True
    else:
        # check if a and b are equal when sorted
        return sorted(list_a) == sorted(list_b)
