#!/usr/bin/env python3

"""arrays.py



Author: Curtis Belmonte
"""

import collections


def argmax(values):
    """Returns the first index of the maximum value in values."""
    max_index = 0
    max_value = values[0]
    for i, value in enumerate(values):
        if value > max_value:
            max_index = i
            max_value = value
    return max_index


def argmin(values):
    """Returns the first index of the minimum value in values."""
    min_index = 0
    min_value = values[0]
    for i, value in enumerate(values):
        if value < min_value:
            min_index = i
            min_value = value
    return min_index


def binary_search(sorted_list, item, _lo=0, _hi=None):
    """Returns the index position of item in the sorted list sorted_list or
    None if item is not found in sorted_list."""

    # if hi has not been initialized, set it to end of sorted_list
    if _hi is None:
        _hi = len(sorted_list)

    # base case: no elements left to search
    if _lo >= _hi:
        return None

    # check the middle element in list, then recurse if necessary
    mid = (_lo + _hi) // 2
    if item < sorted_list[mid]:
        # item must be in first half of list or not at all
        return binary_search(sorted_list, item, _lo, mid)
    elif item > sorted_list[mid]:
        # item must be in second half of list or not at all
        return binary_search(sorted_list, item, mid + 1, _hi)
    else:
        # item found at middle position in list
        return mid


def cumulative_partial_sum(nums, limit=float('inf')):
    """Returns a list of cumulative sums of the numbers in nums, keeping the
    sum of only the previous limit elements."""

    sums = []
    total = 0
    terms = collections.deque()
    for i, num in enumerate(nums):
        total += num
        terms.append(num)

        if len(terms) > limit:
            total -= terms.popleft()

        sums.append(total)

    return sums


def inverse_index_map(values, distinct=True):
    """Returns a map from each item in values to its index.

    If distinct is False, then items in values can be repeated, and each will
    be mapped to a list of its indices."""

    inverse_map = {} if distinct else collections.defaultdict(list)

    if distinct:
        for i, value in enumerate(values):
            inverse_map[value] = i
    else:
        for i, value in enumerate(values):
            inverse_map[value].append(i)

    return inverse_map


def is_permutation(iter_a, iter_b, compare_counts=False):
    """Determines if iterables iter_a, iter_b are permutations of each other.

    If iter_a and iter_b have the same length, then the compare_counts flag
    determines how the two will be compared. If compare_counts is True, this
    function will compare counts of items in the two iterables. Otherwise, this
    function will compare sorted copies of the iterables.
    """

    # convert iterables to lists if necessary
    if not hasattr(iter_a, 'count'):
        iter_a = list(iter_a)
    if not hasattr(iter_b, 'count'):
        iter_b = list(iter_b)

    # if lengths of a and b are different, they cannot be permutations
    if len(iter_a) != len(iter_b):
        return False

    if compare_counts:
        # check if a and b contain the same numbers of the same items
        for item in set(iter_a):
            if iter_a.count(item) != iter_b.count(item):
                return False
        return True
    else:
        # check if a and b are equal when sorted
        return sorted(iter_a) == sorted(iter_b)
