#!/usr/bin/env python3

"""test_arithmetic.py

Unit test for the 'arithmetic' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest
from typing import Union

import common.arithmetic as arith


class TestArithmetic(unittest.TestCase):
    def test_eval_postfix(self):
        self.assertEqual(arith.eval_postfix('3 4 +'), 7)
        self.assertEqual(arith.eval_postfix('34+', is_space_sep=False), 7)
        self.assertEqual(arith.eval_postfix('3 4 5 * -'), -17)
        self.assertEqual(arith.eval_postfix('345*-', is_space_sep=False), -17)
        self.assertEqual(arith.eval_postfix('3 3 3 ^ ^'), 7625597484987)
        self.assertEqual(arith.eval_postfix('10 3 ^'), 1000)
        self.assertEqual(arith.eval_postfix('222^^', is_space_sep=False), 16)
        self.assertEqual(arith.eval_postfix('10 20 /'), 0.5)
        self.assertEqual(arith.eval_postfix('12/', is_space_sep=False), 0.5)
        self.assertEqual(
            arith.eval_postfix('15 7 1 1 + - / 3 * 2 1 1 + + -'), 5)
        self.assertEqual(
            arith.eval_postfix(
                '2 2 ^ 5 7 2 + - * 17 2 3 ^ - 9 3 / 3 4 + 2  * 7 / + * - 95 +'),
            34)

    def test_int_log(self) -> None:
        self.assertEqual(arith.int_log(1), 0)
        self.assertEqual(arith.int_log(2), 1)
        self.assertEqual(arith.int_log(3), 1)
        self.assertEqual(arith.int_log(0.9), 0)
        self.assertEqual(arith.int_log(4.2), 1)
        self.assertEqual(arith.int_log(1, 2), 0)
        self.assertEqual(arith.int_log(2, 2), 1)
        self.assertEqual(arith.int_log(3, 2), 2)
        self.assertEqual(arith.int_log(0.9, 2), 0)
        self.assertEqual(arith.int_log(4.2, 2), 2)
        self.assertEqual(arith.int_log(317), 6)
        self.assertEqual(arith.int_log(150.01, 10), 2)
        self.assertEqual(arith.int_log(783651481.7329, 11.1), 9)
        self.assertEqual(arith.int_log(0.28, 0.7), 4)

    def test_int_pow(self) -> None:
        self.assertEqual(arith.int_pow(0, 1), 0)
        self.assertEqual(arith.int_pow(1, 0), 1)
        self.assertEqual(arith.int_pow(2, 0), 1)
        self.assertEqual(arith.int_pow(2, 1), 2)
        self.assertEqual(arith.int_pow(5, 9), 1953125)
        self.assertEqual(arith.int_pow(5.2, 3.8), 526)
        self.assertEqual(arith.int_pow(7.36, 4.42), 6786)
        self.assertEqual(arith.int_pow(4.84, 2.226), 33)
        self.assertEqual(arith.int_pow(0.21, 0.35), 1)

    def test_int_sqrt(self) -> None:
        self.assertEqual(arith.int_sqrt(0), 0)
        self.assertEqual(arith.int_sqrt(1), 1)
        self.assertEqual(arith.int_sqrt(2), 1)
        self.assertEqual(arith.int_sqrt(2.27), 2)
        self.assertEqual(arith.int_sqrt(4.1), 2)
        self.assertEqual(arith.int_sqrt(50.35), 7)
        self.assertEqual(arith.int_sqrt(80166.213), 283)
        self.assertEqual(arith.int_sqrt(0.148), 0)
        self.assertEqual(arith.int_sqrt(0.541), 1)
        
    def test_mod_mutliply(self) -> None:
        self.assertEqual(arith.mod_multiply(1, 1, 1), 0)
        self.assertEqual(arith.mod_multiply(1, 2, 1), 0)
        self.assertEqual(arith.mod_multiply(1, 2, 2), 0)
        self.assertEqual(arith.mod_multiply(1, 2, 3), 2)
        self.assertEqual(arith.mod_multiply(2, 1, 3), 2)
        self.assertEqual(arith.mod_multiply(2, 3, 4), 2)
        self.assertEqual(arith.mod_multiply(3, 3, 4), 1)
        self.assertEqual(arith.mod_multiply(63, 52, 47), 33)
        self.assertEqual(arith.mod_multiply(5052, 8658, 3010), 1906)
        self.assertEqual(
            arith.mod_multiply(86**95, 64**28, 38**8),
            261051428608)
        self.assertEqual(
            arith.mod_multiply(8177**4018, 9470**1990, 27**29),
            24247430663168320345760575144348378592065)

    def test_mod_power(self) -> None:
        self.assertEqual(arith.mod_power(1, 1, 1), 0)
        self.assertEqual(arith.mod_power(1, 2, 1), 0)
        self.assertEqual(arith.mod_power(2, 3, 4), 0)
        self.assertEqual(arith.mod_power(2, 4, 3), 1)
        self.assertEqual(arith.mod_power(3, 5, 7), 5)
        self.assertEqual(arith.mod_power(5, 3, 13), 8)
        self.assertEqual(arith.mod_power(13, 11, 7), 6)
        self.assertEqual(arith.mod_power(2, 90, 13), 12)
        self.assertEqual(arith.mod_power(7, 256, 13), 9)
        self.assertEqual(arith.mod_power(5, 117, 19), 1)
        self.assertEqual(arith.mod_power(4, 13, 497), 445)
        self.assertEqual(arith.mod_power(2, 500500, 500500507), 339969113)
        self.assertEqual(arith.mod_power(44192, 562280, 8479175), 7136176)

    def test_quadratic_roots(self) -> None:
        roots = sorted(arith.quadratic_roots(1, 0, -1))
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], float):
            self.assertAlmostEqual(roots[0], -1)
        else:
            self.fail('Expected float, got complex: ' + str(roots[0]))
        if isinstance(roots[1], float):
            self.assertAlmostEqual(roots[1], 1)
        else:
            self.fail('Expected float, got complex: ' + str(roots[1]))

        roots = sorted(arith.quadratic_roots(1, -1, -1))
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], float):
            self.assertAlmostEqual(roots[0], -0.61803399)
        else:
            self.fail('Expected float, got complex: ' + str(roots[0]))
        if isinstance(roots[1], float):
            self.assertAlmostEqual(roots[1], 1.61803399)
        else:
            self.fail('Expected float, got complex: ' + str(roots[1]))

        roots = sorted(arith.quadratic_roots(1, 3, -4))
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], float):
            self.assertAlmostEqual(roots[0], -4)
        else:
            self.fail('Expected float, got complex: ' + str(roots[0]))
        if isinstance(roots[1], float):
            self.assertAlmostEqual(roots[1], 1)
        else:
            self.fail('Expected float, got complex: ' + str(roots[1]))

        roots = sorted(arith.quadratic_roots(2, 4, -4))
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], float):
            self.assertAlmostEqual(roots[0], -2.7320508)
        else:
            self.fail('Expected float, got complex: ' + str(roots[0]))
        if isinstance(roots[1], float):
            self.assertAlmostEqual(roots[1], 0.7320508)
        else:
            self.fail('Expected float, got complex: ' + str(roots[1]))

        roots = sorted(arith.quadratic_roots(2, -4, -3))
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], float):
            self.assertAlmostEqual(roots[0], -0.58113883)
        else:
            self.fail('Expected float, got complex: ' + str(roots[0]))
        if isinstance(roots[1], float):
            self.assertAlmostEqual(roots[1], 2.58113883)
        else:
            self.fail('Expected float, got complex: ' + str(roots[1]))

        roots = sorted(arith.quadratic_roots(-27, 643, -11))
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], float):
            self.assertAlmostEqual(roots[0], 0.01711962)
        else:
            self.fail('Expected float, got complex: ' + str(roots[0]))
        if isinstance(roots[1], float):
            self.assertAlmostEqual(roots[1], 23.7976952)
        else:
            self.fail('Expected float, got complex: ' + str(roots[1]))

        def get_imag(x: Union[float, complex]) -> float:
            if isinstance(x, float):
                self.fail('Expected complex, got float: ' + str(x))
                # noinspection PyUnreachableCode
                return 0.0
            else:
                return x.imag

        roots = sorted(arith.quadratic_roots(1, 0, 1), key=get_imag)
        self.assertEqual(len(roots), 2)
        if isinstance(roots[0], complex):
            self.assertAlmostEqual(roots[0].real, 0)
            self.assertAlmostEqual(roots[0].imag, -1)
        else:
            self.fail('Expected complex, got float: ' + str(roots[0]))
        if isinstance(roots[1], complex):
            self.assertAlmostEqual(roots[1].real, 0)
            self.assertAlmostEqual(roots[1].imag, 1)
        else:
            self.fail('Expected complex, got float: ' + str(roots[1]))

        roots = sorted(arith.quadratic_roots(24, 41, 35), key=get_imag)
        self.assertEqual(len(roots), 2)
        self.assertTrue(isinstance(roots[0], complex))
        self.assertTrue(isinstance(roots[1], complex))
        self.assertAlmostEqual(roots[0].real, -0.85416667)
        self.assertAlmostEqual(roots[0].imag, -0.85365839)
        self.assertAlmostEqual(roots[1].real, -0.85416667)
        self.assertAlmostEqual(roots[1].imag, 0.85365839)


if __name__ == '__main__':
    unittest.main()
