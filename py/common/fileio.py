#!/usr/bin/env python3

"""fileio.py



Author: Curtis Belmonte
"""


def ints_from_file(input_file, sep=' '):
    """Returns a list of rows of integer numbers read from input_file."""
    with open(input_file) as f:
        for line in f:
            yield [int(token) for token in line.rstrip().split(sep)]


def strings_from_file(input_file, sep=','):
    """Returns a list of sep-separated quoted strings read from input_file."""
    with open(input_file) as f:
        return [string.strip('"') for string in f.read().split(sep)]
