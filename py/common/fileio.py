#!/usr/bin/env python3

"""fileio.py

Functions for reading values from and writing to system files.
"""

__author__ = 'Curtis Belmonte'

import csv
from typing import Iterable, Iterator, List, Optional


def ints_from_file(file_name: str, sep: str = ' ') -> Iterator[List[int]]:
    """Returns a list of rows of sep-separated integers read from file_name."""
    with open(file_name) as input_file:
        for line in input_file:
            yield [int(token) for token in line.rstrip().split(sep)]


def strings_from_file(
        file_name: str,
        sep: str = ',',
        quote: Optional[str] = '"') -> Iterable[str]:

    """Returns a sequence of sep-separated strings read from file_name.

    If specified, quote designates a custom quotation mark character to be
    stripped from the start and end of each string token before it's returned.
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
