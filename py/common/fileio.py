#!/usr/bin/env python3

"""Common library for reading from and writing to files.

This module provides functions for reading in formatted data from system files
and writing it back out. Examples include reading a string list or integer
matrix from a file.
"""

import csv
from typing import Iterable, Iterator, List, Optional


def ints_from_file(file_name: str, sep: str = ' ') -> Iterator[List[int]]:
    """Reads a list of integer rows from a file.

    Args:
        file_name: A relative path to the file to read from.
        sep: A separator token that appears between integers within a row.

    Yields:
        Each integer row, in sequence, from ``file_name``, where each row is on
        a separate line and integers within a row are separated by ``sep``.
    """
    with open(file_name) as input_file:
        for line in input_file:
            yield [int(token) for token in line.rstrip().split(sep)]


def strings_from_file(
    file_name: str,
    sep: str = ',',
    quote: Optional[str] = '"',
) -> Iterable[str]:
    """Reads a sequence of formatted strings from a file.

    Args:
        file_name: A relative path to the file to read from.
        sep: A separator token that appears between input strings in the file.
        quote: If present, designates a custom quotation mark character to be
            stripped from the start and end of each input string. If ``None``,
            each input string will be interpreted verbatim.

    Yields:
        Each input string, in sequence, from ``file_name``, where strings are
        separated by ``sep`` and quoted with ``quote`` characters.
    """

    with open(file_name, newline='') as input_file:
        if quote is None or quote == '':
            quote_style = csv.QUOTE_NONE
        else:
            quote_style = csv.QUOTE_ALL

        reader = csv.reader(
            input_file, delimiter=sep, quotechar=quote, quoting=quote_style)
        for row in reader:
            for token in row:
                yield token
