#!/usr/bin/env python3

"""test_sequences.py

Unit test for the 'sequences' common module.
"""

__author__ = 'Curtis Belmonte'

import itertools
import unittest
from typing import Dict, List, Sequence

import common.sequences as seqs


class TestSequences(unittest.TestCase):
    def test_arithmetic_product(self) -> None:
        self.assertEqual(seqs.arithmetic_product(3, 1), 3)
        self.assertEqual(seqs.arithmetic_product(3, 1, 1), 3)
        self.assertEqual(seqs.arithmetic_product(3, 1, 2), 3)
        self.assertEqual(seqs.arithmetic_product(1, 2, -1), 0)
        self.assertEqual(seqs.arithmetic_product(19, 5, 4), 12801915)
        self.assertEqual(seqs.arithmetic_product(13, 6, -3), -7280)
        self.assertEqual(seqs.arithmetic_product(-2, 6, 3), -7280)

    def test_arithmetic_series(self) -> None:
        self.assertEqual(seqs.arithmetic_series(4, 1), 4)
        self.assertEqual(seqs.arithmetic_series(4, 1, 1), 4)
        self.assertEqual(seqs.arithmetic_series(4, 1, 2), 4)
        self.assertEqual(seqs.arithmetic_series(1, 2, -1), 1)
        self.assertEqual(seqs.arithmetic_series(19, 5, 4), 135)
        self.assertEqual(seqs.arithmetic_series(7, 8, -3), -28)
        self.assertEqual(seqs.arithmetic_series(-14, 8, 3), -28)

    def test_collatz_step(self) -> None:
        self.assertEqual(seqs.collatz_step(1), 4)
        self.assertEqual(seqs.collatz_step(2), 1)
        self.assertEqual(seqs.collatz_step(4), 2)
        self.assertEqual(seqs.collatz_step(-1), -2)
        self.assertEqual(seqs.collatz_step(-2), -1)
        self.assertEqual(seqs.collatz_step(23), 70)
        self.assertEqual(seqs.collatz_step(42), 21)
        self.assertEqual(seqs.collatz_step(1337), 4012)
        self.assertEqual(seqs.collatz_step(2048), 1024)

    def test_compute_chain_lengths(self) -> None:
        lengths = {} # type: Dict[int, int]
        values = [0] + list(range(3, 9))

        def step(x: int) -> int:
            return (2 if x == 0 else
                    4 if x == 3 else
                    6 if x == 5 else
                    x - 1)

        def is_valid(x: int) -> bool:
            return x != 6

        seqs.compute_chain_lengths(lengths, values, step, is_valid)

        self.assertEqual(lengths[0], 3)
        self.assertEqual(lengths[1], 3)
        self.assertEqual(lengths[2], 3)
        self.assertEqual(lengths[3], 2)
        self.assertEqual(lengths[4], 2)
        self.assertFalse(5 in lengths)
        self.assertFalse(6 in lengths)
        self.assertFalse(7 in lengths)
        self.assertFalse(8 in lengths)

    def test_fibonacci(self) -> None:
        self.assertEqual(seqs.fibonacci(0), 1)
        self.assertEqual(seqs.fibonacci(1), 1)
        self.assertEqual(seqs.fibonacci(2), 2)
        self.assertEqual(seqs.fibonacci(3), 3)
        self.assertEqual(seqs.fibonacci(4), 5)
        self.assertEqual(seqs.fibonacci(13), 377)
        self.assertEqual(seqs.fibonacci(37), 39088169)
        self.assertEqual(
            seqs.fibonacci(273),
            818706854228831001753880637535093596811413714795418360007)

    def test_generate_fibonacci(self) -> None:
        def list_fibonacci(i: int, j: int) -> List[int]:
            """Returns a list of the i to jth (exclusive) Fibonacci numbers."""
            return list(itertools.islice(seqs.generate_fibonacci(), i, j))

        self.assertEqual(list_fibonacci(0, 1), [1])
        self.assertEqual(list_fibonacci(0, 2), [1, 1])
        self.assertEqual(list_fibonacci(0, 9), [1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(list_fibonacci(2, 6), [2, 3, 5, 8])
        self.assertEqual(list_fibonacci(12, 15), [233, 377, 610])
        self.assertEqual(list_fibonacci(36, 38), [24157817, 39088169])
        self.assertEqual(
            list_fibonacci(273, 274),
            [818706854228831001753880637535093596811413714795418360007])

    def test_generate_pascal_triangle(self) -> None:
        def list_pascal_rows(i: int, j: int) -> List[Sequence[int]]:
            """Returns a list of the i to jth (exclusive) Pascal rows."""
            return list(itertools.islice(seqs.generate_pascal_triangle(), i, j))

        self.assertEqual(list_pascal_rows(0, 1), [[1]])
        self.assertEqual(list_pascal_rows(0, 2), [[1], [1, 1]])
        self.assertEqual(list_pascal_rows(0, 3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(
            list_pascal_rows(3, 5), [[1, 3, 3, 1], [1, 4, 6, 4, 1]])
        self.assertEqual(
            list_pascal_rows(4, 7),
            [[1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]])
        self.assertEqual(
            list_pascal_rows(9, 10), [[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]])
        self.assertEqual(
            list_pascal_rows(12, 13),
            [[1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]])

    def test_generate_products(self) -> None:
        def list_products(nums: Sequence[int], i: int, j: int) -> List[int]:
            """Returns a list of the i to jth (exclusive) products of nums."""
            return list(itertools.islice(seqs.generate_products(nums), i, j))

        self.assertEqual(
            list_products([2], 0, 14),
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])
        self.assertEqual(list_products([2], 42, 43), [4398046511104])
        self.assertEqual(
            list_products([2, 3], 0, 18),
            [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72])
        self.assertEqual(
            list_products([3, 2], 31, 41),
            [432, 486, 512, 576, 648, 729, 768, 864, 972, 1024])
        self.assertEqual(
            list_products([2, 3, 5], 0, 18),
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30])
        self.assertEqual(list_products([5, 2, 3], 1690, 1691), [2125764000])
        self.assertEqual(
            list_products([3, 11], 0, 15),
            [1, 3, 9, 11, 27, 33, 81, 99, 121, 243, 297, 363, 729, 891, 1089])
        self.assertEqual(
            list_products([2310, 30030, 2, 6, 30, 210, 510510], 0, 29),
            [1, 2, 4, 6, 8, 12, 16, 24, 30, 32, 36, 48, 60, 64, 72, 96, 120,
             128, 144, 180, 192, 210, 216, 240, 256, 288, 360, 384, 420])
        self.assertEqual(
            list_products([2, 6, 30, 210, 2310, 30030, 510510], 420, 427),
            [5292000, 5308416, 5322240, 5336100, 5405400, 5443200, 5529600])
        self.assertEqual(
            list_products([2, 3, 5, 8, 13, 21, 34, 55, 89], 161, 174),
            [729, 750, 756, 768, 780, 800, 801, 810, 816, 819, 825, 832, 840])

    def test_hexagonal(self) -> None:
        hex_nums = [0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325]
        for i, n in enumerate(hex_nums):
            self.assertEqual(seqs.hexagonal(i), n)
        self.assertEqual(seqs.hexagonal(42), 3486)
        self.assertEqual(seqs.hexagonal(6438), 82889250)

    def test_is_fibonacci(self) -> None:
        fib_nums = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987}
        for n in range(1, 1000):
            self.assertEqual(seqs.is_fibonacci(n), n in fib_nums)
        self.assertFalse(seqs.is_fibonacci(3416454622906706))
        self.assertTrue(seqs.is_fibonacci(3416454622906707))
        self.assertFalse(seqs.is_fibonacci(3416454622906708))
        self.assertFalse(seqs.is_fibonacci(218922995834555169027))
        self.assertTrue(seqs.is_fibonacci(218922995834555169026))
        self.assertFalse(seqs.is_fibonacci(218922995834555169025))

    def test_is_hexagonal(self) -> None:
        hex_nums = {1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325}
        for n in range(1, 350):
            self.assertEqual(seqs.is_hexagonal(n), n in hex_nums)
        self.assertFalse(seqs.is_hexagonal(971530876952))
        self.assertTrue(seqs.is_hexagonal(971530876953))
        self.assertFalse(seqs.is_hexagonal(971530876954))

    def test_is_pentagonal(self) -> None:
        pent_nums = {1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247}
        for n in range(1, 250):
            self.assertEqual(seqs.is_pentagonal(n), n in pent_nums)
        self.assertFalse(seqs.is_pentagonal(728648331956))
        self.assertTrue(seqs.is_pentagonal(728648331957))
        self.assertFalse(seqs.is_pentagonal(728648331958))

    def test_is_power(self) -> None:
        self.assertTrue(seqs.is_power(1, 305))
        self.assertTrue(seqs.is_power(2, 1))
        self.assertTrue(seqs.is_power(3, 1))
        self.assertTrue(seqs.is_power(9024, 1))

        squares = set([n**2 for n in range(1, 23)])
        for n in range(1, 500):
            self.assertEqual(seqs.is_power(n, 2), n in squares)

        cubes = {1, 8, 27, 64, 125, 216, 343}
        for n in range(1, 350):
            self.assertEqual(seqs.is_power(n, 3), n in cubes)

        quarts = {1, 16, 81, 256}
        for n in range(1, 300):
            self.assertEqual(seqs.is_power(n, 4), n in quarts)

        self.assertFalse(seqs.is_power(48566960, 2))
        self.assertTrue(seqs.is_power(48566961, 2))
        self.assertFalse(seqs.is_power(48566962, 2))
        self.assertFalse(seqs.is_power(48566961, 3))
        self.assertFalse(seqs.is_power(48566961, 4))
        self.assertFalse(seqs.is_power(338463151208, 3))
        self.assertTrue(seqs.is_power(338463151209, 3))
        self.assertFalse(seqs.is_power(338463151210, 3))
        self.assertFalse(seqs.is_power(338463151209, 2))
        self.assertFalse(seqs.is_power(338463151209, 4))
        self.assertFalse(seqs.is_power(30821664720, 4))
        self.assertTrue(seqs.is_power(30821664721, 4))
        self.assertFalse(seqs.is_power(30821664722, 4))
        self.assertTrue(seqs.is_power(30821664721, 2))
        self.assertFalse(seqs.is_power(30821664721, 3))
        self.assertFalse(seqs.is_power(96889010406, 13))
        self.assertTrue(seqs.is_power(96889010407, 13))
        self.assertFalse(seqs.is_power(96889010408, 13))
        self.assertFalse(seqs.is_power(96889010407, 7))

    def test_is_square(self) -> None:
        squares = set([n**2 for n in range(1, 32)])
        for n in range(1, 1000):
            self.assertEqual(seqs.is_power(n, 2), n in squares)
        self.assertFalse(seqs.is_square(1769800759))
        self.assertFalse(seqs.is_square(1769800760))
        self.assertTrue(seqs.is_square(1769800761))
        self.assertFalse(seqs.is_square(1769800762))
        self.assertFalse(seqs.is_square(1769800763))

    def test_is_triangular(self) -> None:
        tri_nums = {1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120}
        for n in range(1, 125):
            self.assertEqual(seqs.is_triangular(n), n in tri_nums)
        self.assertFalse(seqs.is_triangular(884921413))
        self.assertFalse(seqs.is_triangular(884921414))
        self.assertTrue(seqs.is_triangular(884921415))
        self.assertFalse(seqs.is_triangular(884921416))
        self.assertFalse(seqs.is_triangular(884921417))

    def test_next_multiple(self) -> None:
        self.assertEqual(seqs.next_multiple(1, 0), 0)
        self.assertEqual(seqs.next_multiple(1, 1), 1)
        self.assertEqual(seqs.next_multiple(1, 2), 2)
        self.assertEqual(seqs.next_multiple(2, 1), 2)
        self.assertEqual(seqs.next_multiple(2, 2), 2)
        self.assertEqual(seqs.next_multiple(2, 3), 4)
        self.assertEqual(seqs.next_multiple(3, 2), 3)
        self.assertEqual(seqs.next_multiple(7, 365), 371)
        self.assertEqual(seqs.next_multiple(365, 42), 365)
        self.assertEqual(seqs.next_multiple(73, 820), 876)
        self.assertEqual(seqs.next_multiple(264, 5133), 5280)
        self.assertEqual(seqs.next_multiple(6376, 913259), 918144)
        self.assertEqual(seqs.next_multiple(9448487, 589545477), 595254681)

    def test_pentagonal(self) -> None:
        pent_nums = [0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247]
        for i, n in enumerate(pent_nums):
            self.assertEqual(seqs.pentagonal(i), n)
        self.assertEqual(seqs.pentagonal(53), 4187)
        self.assertEqual(seqs.pentagonal(8952), 120202980)

    def test_sum_of_squares(self) -> None:
        self.assertEqual(seqs.sum_of_squares(1), 1)
        self.assertEqual(seqs.sum_of_squares(2), 5)
        self.assertEqual(seqs.sum_of_squares(3), 14)
        self.assertEqual(seqs.sum_of_squares(4), 30)
        self.assertEqual(seqs.sum_of_squares(5), 55)
        self.assertEqual(seqs.sum_of_squares(6), 91)
        self.assertEqual(seqs.sum_of_squares(7), 140)
        self.assertEqual(seqs.sum_of_squares(401), 21574201)
        self.assertEqual(seqs.sum_of_squares(34594), 13800661997045)

    def test_triangular(self) -> None:
        tri_nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
        for i, n in enumerate(tri_nums):
            self.assertEqual(seqs.triangular(i + 1), n)
        self.assertEqual(seqs.triangular(292), 42778)
        self.assertEqual(seqs.triangular(38483), 740489886)
        self.assertEqual(seqs.triangular(4946666), 12234754731111)


if __name__ == '__main__':
    unittest.main()
