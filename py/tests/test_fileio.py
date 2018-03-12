#!/usr/bin/env python3

"""test_fileio.py

Unit test for the 'fileio' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest
from tempfile import NamedTemporaryFile

import common.fileio as fio


class TestFileio(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_file = NamedTemporaryFile()

    def tearDown(self) -> None:
        self.temp_file.close()

    def write_to_file(self, output: str) -> None:
        with open(self.temp_file.name, 'w') as output_file:
            output_file.write(output)

    def test_ints_from_file(self) -> None:
        self.write_to_file('0\n')
        self.assertEqual(
            list(fio.ints_from_file(self.temp_file.name)), [[0]])

        self.write_to_file('-1 2 3 -4 5\n')
        self.assertEqual(
            list(fio.ints_from_file(self.temp_file.name)), [[-1, 2, 3, -4, 5]])

        self.write_to_file('1|-2|-3|4|5\n')
        self.assertEqual(
            list(fio.ints_from_file(self.temp_file.name, sep='|')),
            [[1, -2, -3, 4, 5]])

        self.write_to_file('11 12 13\n21 22\n31 32 33 34\n')
        self.assertEqual(
            list(fio.ints_from_file(self.temp_file.name)),
            [[11, 12, 13], [21, 22], [31, 32, 33, 34]])

        self.write_to_file('3.14\n127.0.0.1\n0.2.1')
        self.assertEqual(
            list(fio.ints_from_file(self.temp_file.name, sep='.')),
            [[3, 14], [127, 0, 0, 1], [0, 2, 1]])

    def test_strings_from_file(self) -> None:
        self.write_to_file('"hello"\n')
        self.assertEqual(
            list(fio.strings_from_file(self.temp_file.name)), ['hello'])

        self.write_to_file('"hello","world"\n')
        self.assertEqual(
            list(fio.strings_from_file(self.temp_file.name)),
            ['hello', 'world'])

        self.write_to_file('"hello"\n"world"\n')
        self.assertEqual(
            list(fio.strings_from_file(self.temp_file.name)),
            ['hello', 'world'])

        self.write_to_file('hello,world\n')
        self.assertEqual(
            list(fio.strings_from_file(self.temp_file.name, quote=None)),
            ['hello', 'world'])

        self.write_to_file('hello,world\n')
        self.assertEqual(
            list(fio.strings_from_file(self.temp_file.name, quote='')),
            ['hello', 'world'])

        self.write_to_file('"hello" "world"\n')
        self.assertEqual(
            list(fio.strings_from_file(self.temp_file.name, sep=' ')),
            ['hello', 'world'])

        self.write_to_file('_hello_:_world_\n')
        self.assertEqual(
            list(
                fio.strings_from_file(self.temp_file.name, sep=':', quote='_')),
            ['hello', 'world'])

        self.write_to_file('`Lorem` `ipsum` `dolor`\n`sit` `amet.`\n')
        self.assertEqual(
            list(
                fio.strings_from_file(self.temp_file.name, sep=' ', quote='`')),
            ['Lorem', 'ipsum', 'dolor', 'sit', 'amet.'])


if __name__ == '__main__':
    unittest.main()
