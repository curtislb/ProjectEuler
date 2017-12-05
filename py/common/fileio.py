#!/usr/bin/env python3

"""fileio.py

Functions for reading values from and writing to system files.
"""

__author__ = 'Curtis Belmonte'

from typing import Iterator, List


def ints_from_file(input_file: str, sep: str = ' ') -> Iterator[List[int]]:
    """Returns a list of rows of integer numbers read from input_file."""
    with open(input_file) as f:
        for line in f:
            yield [int(token) for token in line.rstrip().split(sep)]


def strings_from_file(input_file: str, sep: str = ',') -> List[str]:
    """Returns a sequence of sep-separated strings read from input_file."""
    with open(input_file) as f:
        return [s.strip('"') for s in f.read().split(sep)]
