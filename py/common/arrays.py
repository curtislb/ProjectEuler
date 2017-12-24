#!/usr/bin/env python3

"""arrays.py

Functions for operating on lists and related sequences.
"""

__author__ = 'Curtis Belmonte'

from collections import defaultdict, deque
from typing import Dict, Iterable, List, Mapping, Optional, Sequence

from common.types import Comparable, T


def argmax(values: Sequence[Comparable]) -> int:
    """Returns the first index of the maximum value in values."""
    max_index = 0
    max_value = values[0]
    for i, value in enumerate(values):
        if value > max_value:
            max_index = i
            max_value = value
    return max_index


def argmin(values: Sequence[Comparable]) -> int:
    """Returns the first index of the minimum value in values."""
    min_index = 0
    min_value = values[0]
    for i, value in enumerate(values):
        if value < min_value:
            min_index = i
            min_value = value
    return min_index


def binary_search(
        sorted_list: Sequence[Comparable], item: Comparable) -> Optional[int]:

    """Returns the index position of item in the sorted list sorted_list or
    None if item is not found in sorted_list."""

    # initialize search indices
    lo = 0
    hi = len(sorted_list)

    while lo < hi:
        # check middle element in list
        mid = (lo + hi) // 2
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


def cumulative_partial_sum(
        nums: Sequence[float],
        limit: float = float('inf')) -> Sequence[float]:

    """Returns a sequence of cumulative sums of the numbers in nums, keeping
    the sum of only the previous limit elements."""

    sums = [] # type: List[float]
    terms = deque() # type: deque
    total = 0 # type: float
    for i, num in enumerate(nums):
        total += num
        terms.append(num)

        if len(terms) > limit:
            total -= terms.popleft()

        sums.append(total)

    return sums


def inverse_index_map(values: Sequence[T]) -> Mapping[T, int]:
    """Returns a map from each item in values to its unique index.

    Items in values must be distinct. If values may contain duplicates, use
    inverse_index_map_nd.
    """

    inverse_map = {} # type: Dict[T, int]
    for i, value in enumerate(values):
        inverse_map[value] = i

    return inverse_map


def inverse_index_map_nd(values: Sequence[T]) -> Mapping[T, Sequence[int]]:
    """Returns a map from each item in values to a sequence of its indices."""

    inverse_map = defaultdict(list) # type: Dict[T, List[int]]
    for i, value in enumerate(values):
        inverse_map[value].append(i)

    return inverse_map


def is_permutation(
        iter_a: Iterable[T],
        iter_b: Iterable[T],
        compare_counts: bool = False) -> bool:

    """Determines if iterables iter_a, iter_b are permutations of each other.

    If iter_a and iter_b have the same length, then the compare_counts flag
    determines how the two will be compared. If compare_counts is True, this
    function will compare counts of items in the two iterables. Otherwise, this
    function will compare sorted copies of the iterables.
    """

    # convert iterables to lists if necessary
    list_a = iter_a if isinstance(iter_a, list) else list(iter_a) # type: List
    list_b = iter_b if isinstance(iter_b, list) else list(iter_b) # type: List

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
