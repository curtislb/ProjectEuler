#!/usr/bin/env python3

"""test_matrices.py

Unit test for the 'matrices' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.matrices as mat


class TestMatrices(unittest.TestCase):
    def test_cross_product_3d(self):
        self.assertEqual(mat.cross_product_3d((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(mat.cross_product_3d([0, 0, 0], [0, 0, 0]), (0, 0, 0))
        self.assertEqual(
            mat.cross_product_3d((2, 3, 4), (5, 6, 7)),
            (-3, 6, -3))
        self.assertEqual(
            mat.cross_product_3d((3, -3, 1), (4, 9, 2)),
            (-15, -2, 39))
        self.assertEqual(
            mat.cross_product_3d((3, -3, 1), (-12, 12, -4)),
            (0, 0, 0))
        
    def test_dot_product(self) -> None:
        self.assertEqual(mat.dot_product((2,), (3,)), 6)
        self.assertEqual(mat.dot_product([2], [3]), 6)
        self.assertEqual(mat.dot_product((1, 2), (3, 4)), 11)
        self.assertEqual(mat.dot_product((2, 3, 4), (5, 6, 7)), 56)
        self.assertEqual(
            mat.dot_product((10, -3, -10, 8, 1), (7, 5, -1, -9, 8)),
            1)
        
    def test_flatten_matrix(self) -> None:
        self.assertEqual(mat.flatten_matrix([[]]), [])
        self.assertEqual(mat.flatten_matrix([[]], keep_indices=True), [])
        self.assertEqual(mat.flatten_matrix([[1]]), [1])
        self.assertEqual(
            mat.flatten_matrix([[1]], keep_indices=True),
            [(1, 0, 0)])
        self.assertEqual(mat.flatten_matrix([[4, 3], [2, 1]]), [4, 3, 2, 1])
        self.assertEqual(
            mat.flatten_matrix([['4', 3], [2, '1']], keep_indices=True),
            [('4', 0, 0), (3, 0, 1), (2, 1, 0), ('1', 1, 1)])
        self.assertEqual(
            mat.flatten_matrix([[1, 2], [3], [4, 5, 6]], keep_indices=True),
            [(1, 0, 0), (2, 0, 1), (3, 1, 0), (4, 2, 0), (5, 2, 1), (6, 2, 2)])
        
    def test_make_spiral(self) -> None:
        self.assertEqual(mat.make_spiral(1), [[1]])
        self.assertEqual(
            mat.make_spiral(2),
            [
                [7, 8, 9],
                [6, 1, 2],
                [5, 4, 3],
            ])
        self.assertEqual(
            mat.make_spiral(3),
            [
                [21, 22, 23, 24, 25],
                [20,  7,  8,  9, 10],
                [19,  6,  1,  2, 11],
                [18,  5,  4,  3, 12],
                [17, 16, 15, 14, 13],
            ])
        self.assertEqual(
            mat.make_spiral(4),
            [
                [43, 44, 45, 46, 47, 48, 49],
                [42, 21, 22, 23, 24, 25, 26],
                [41, 20,  7,  8,  9, 10, 27],
                [40, 19,  6,  1,  2, 11, 28],
                [39, 18,  5,  4,  3, 12, 29],
                [38, 17, 16, 15, 14, 13, 30],
                [37, 36, 35, 34, 33, 32, 31],
            ])
        self.assertEqual(
            mat.make_spiral(5),
            [
                [73, 74, 75, 76, 77, 78, 79, 80, 81],
                [72, 43, 44, 45, 46, 47, 48, 49, 50],
                [71, 42, 21, 22, 23, 24, 25, 26, 51],
                [70, 41, 20,  7,  8,  9, 10, 27, 52],
                [69, 40, 19,  6,  1,  2, 11, 28, 53],
                [68, 39, 18,  5,  4,  3, 12, 29, 54],
                [67, 38, 17, 16, 15, 14, 13, 30, 55],
                [66, 37, 36, 35, 34, 33, 32, 31, 56],
                [65, 64, 63, 62, 61, 60, 59, 58, 57]
            ])

    def test_max_bipartite_matching(self) -> None:
        self.assertEqual(len(mat.max_bipartite_matching([[False]])), 0)
        self.assertCountEqual(mat.max_bipartite_matching([[True]]), [(0, 0)])
        self.assertCountEqual(
            mat.max_bipartite_matching([
                [True, False],
                [False, True]]),
            [(0, 0), (1, 1)])
        self.assertEqual(
            len(mat.max_bipartite_matching([
                [False, False],
                [True,  True]])),
            1)
        self.assertEqual(
            len(mat.max_bipartite_matching([
                [False, True],
                [False, True]])),
            1)
        self.assertCountEqual(
            mat.max_bipartite_matching([
                [False, True],
                [True,  True]]),
            [(0, 1), (1, 0)])
        self.assertCountEqual(
            mat.max_bipartite_matching([
                [True,  False, False],
                [False, False, True],
                [False, True,  False]]),
            [(0, 0), (1, 2), (2, 1)])
        self.assertEqual(
            len(mat.max_bipartite_matching([
                [True,  False, True, False, False],
                [False, False, True, False, False],
                [False, True,  True, True,  False],
                [False, False, True, False, False],
                [False, True,  True, False, True]])),
            4)
        self.assertCountEqual(
            mat.max_bipartite_matching([
                [True,  False, False, False, False],
                [True,  False, True,  False, False],
                [False, True,  False, True,  False],
                [False, False, True,  False, True],
                [False, True,  False, False, True]]),
            [(0, 0), (1, 2), (2, 3), (3, 4), (4, 1)])
        self.assertEqual(
            len(mat.max_bipartite_matching([
                [False, True,  True,  False, False, False],
                [True,  False, False, True,  False, False],
                [False, False, True,  False, False, False],
                [False, False, True,  True,  False, False],
                [False, False, False, False, False, False],
                [False, False, False, False, False, True]])),
            5)

    def test_minimum_line_cover(self) -> None:
        self.assertEqual(len(mat.minimum_line_cover([[1]])), 0)
        self.assertEqual(len(mat.minimum_line_cover([[0]])), 1)
        self.assertEqual(len(mat.minimum_line_cover([[-1, 0]])), 1)
        self.assertCountEqual(mat.minimum_line_cover([[0, 0]]), [(False, 0)])
        self.assertCountEqual(mat.minimum_line_cover([[0], [0]]), [(True, 0)])
        self.assertCountEqual(
            mat.minimum_line_cover([[0, 0, 0]]),
            [(False, 0)])
        self.assertCountEqual(
            mat.minimum_line_cover([[0], [0], [0]]),
            [(True, 0)])
        self.assertEqual(len(mat.minimum_line_cover([[0, 1], [2, 3]])), 1)
        self.assertEqual(len(mat.minimum_line_cover([[5, 7], [4, 0]])), 1)
        self.assertCountEqual(
            mat.minimum_line_cover([[0, 0], [-2, 6]]),
            [(False, 0)])
        self.assertCountEqual(
            mat.minimum_line_cover([[-3, 0], [12, 0]]),
            [(True, 1)])
        self.assertEqual(len(mat.minimum_line_cover([[8, 0], [0, 0]])), 2)
        self.assertCountEqual(
            mat.minimum_line_cover([
                [1, 2, 0],
                [3, 4, 0],
                [0, 0, 0]]),
            [(False, 2), (True, 2)])
        self.assertEqual(
            len(mat.minimum_line_cover([
                [0, 0, 0],
                [9, 2, 0],
                [4, 0, 6],
                [0, 3, 1]])),
            3)
        self.assertEqual(
            len(mat.minimum_line_cover([
                [0, 4, 2, 2],
                [7, 6, 4, 0],
                [0, 5, 3, 5],
                [4, 3, 0, 0],
                [0, 0, 0, 0]])),
            4)
        self.assertEqual(
            len(mat.minimum_line_cover([
                [0, 4, 2, 2, 3],
                [7, 6, 4, 0, 1],
                [0, 5, 3, 5, 7],
                [4, 3, 0, 0, 2],
                [0, 0, 0, 0, 0]])),
            4)
        self.assertEqual(
            len(mat.minimum_line_cover([
                [0, 4, 2, 2, 3, 9],
                [7, 6, 4, 0, 1, -1],
                [0, 5, 3, 5, 7, 8],
                [4, 3, 0, 0, 2, 11],
                [0, 0, 0, 0, 0, 0]])),
            4)
        self.assertEqual(
            len(mat.minimum_line_cover([
                [0, 3, 0, 2, 2],
                [7, 5, 4, 0, 0],
                [0, 4, 3, 5, 6],
                [4, 2, 0, 0, 1],
                [1, 0, 1, 1, 0]])),
            5)
        self.assertEqual(
            len(mat.minimum_line_cover([
                [0, 1, 0, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 0, 1, 1],
                [1, 0, 0, 1, 0]])),
            4)
        self.assertCountEqual(
            mat.minimum_line_cover([
                [0, 1, 0, 1, 1],
                [0, 1, 0, 1, 1],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 0]]),
            [(True, 0), (True, 2), (True, 4)])
        self.assertEqual(
            len(mat.minimum_line_cover([
                [5, 1, 2, 6, 7, 4, 3, 6, 4, 7],
                [2, 2, 0, 0, 1, 0, 3, 0, 4, 3],
                [6, 4, 2, 1, 1, 2, 0, 6, 6, 1],
                [4, 0, 2, 4, 4, 4, 4, 0, 2, 0],
                [2, 2, 4, 6, 2, 7, 1, 2, 5, 4],
                [3, 1, 4, 3, 2, 0, 6, 5, 5, 1],
                [2, 3, 6, 4, 0, 1, 6, 2, 2, 2],
                [1, 3, 1, 0, 0, 0, 1, 5, 1, 2]])),
            6)
        
    def test_optimal_assignment(self) -> None:
        self.assertCountEqual(mat.optimal_assignment([[0]]), [(0, 0)])
        self.assertCountEqual(mat.optimal_assignment([[1]]), [(0, 0)])
        self.assertCountEqual(mat.optimal_assignment([[-2]]), [(0, 0)])
        self.assertCountEqual(
            mat.optimal_assignment([[1, 2], [3, 5]]),
            [(0, 1), (1, 0)])
        self.assertCountEqual(
            mat.optimal_assignment([[-1, -2], [-3, -5]]),
            [(0, 0), (1, 1)])
        self.assertCountEqual(
            mat.optimal_assignment([[-1, 2], [-3, 4]]),
            [(0, 1), (1, 0)])
        self.assertCountEqual(
            mat.optimal_assignment([
                [1, 6, 4],
                [8, 7, 9],
                [9, 0, 5]]),
            [(0, 0), (1, 2), (2, 1)])
        self.assertCountEqual(
            mat.optimal_assignment([
                [52, 78, 91, 63, 14],
                [78, 45, 67, 43, 12],
                [85, 84, 43, 45, 36],
                [37, 60, 52, 54, 67],
                [48, 86, 23, 58, 99]]),
            [(0, 4), (1, 1), (2, 3), (3, 0), (4, 2)])
        self.assertCountEqual(
            mat.optimal_assignment([
                [990, 621, 440, 679, 366, 961,  62, 609, 325, 188],
                [408, 172,  52,   0, 901, 168, 525, 705,  68,  25],
                [761, 187, 835, 508, 310, 216, 218, 351, 166, 263],
                [712,  78, 879, 530, 451, 564,   2,  49, 423, 394],
                [725, 558, 862, 243, 325, 509, 542, 448, 800, 760],
                [893, 341, 126, 547, 184, 199, 479, 282, 419, 508],
                [619, 297, 193, 182, 706, 558, 621, 393, 883, 922],
                [594, 192, 770, 523,  87, 295, 367, 744, 146, 700],
                [491, 386, 719,  14, 360, 673, 579, 413, 546, 427],
                [730, 392, 968, 587, 177, 291, 743,  63, 329, 717]]),
            [(0, 6), (1, 9), (2, 8), (3, 1), (4, 3), (5, 5), (6, 2), (7, 4),
             (8, 0), (9, 7)])


if __name__ == '__main__':
    unittest.main()
