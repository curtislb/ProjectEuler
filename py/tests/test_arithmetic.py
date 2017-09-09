#!/usr/bin/env python3

"""test_arithmetic.py



Author: Curtis Belmonte
"""

import unittest

from .context import arithmetic as arith


class TestArithmetic(unittest.TestCase):
    def test_int_log(self):
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

    def test_int_pow(self):
        self.assertEqual(arith.int_pow(0, 1), 0)
        self.assertEqual(arith.int_pow(1, 0), 1)
        self.assertEqual(arith.int_pow(2, 0), 1)
        self.assertEqual(arith.int_pow(2, 1), 2)
        self.assertEqual(arith.int_pow(5, 9), 1953125)
        self.assertEqual(arith.int_pow(5.2, 3.8), 526)
        self.assertEqual(arith.int_pow(7.36, 4.42), 6786)
        self.assertEqual(arith.int_pow(4.84, 2.226), 33)
        self.assertEqual(arith.int_pow(0.21, 0.35), 1)

    def test_int_sqrt(self):
        self.assertEqual(arith.int_sqrt(0), 0)
        self.assertEqual(arith.int_sqrt(1), 1)
        self.assertEqual(arith.int_sqrt(2), 1)
        self.assertEqual(arith.int_sqrt(2.27), 2)
        self.assertEqual(arith.int_sqrt(4.1), 2)
        self.assertEqual(arith.int_sqrt(50.35), 7)
        self.assertEqual(arith.int_sqrt(80166.213), 283)
        self.assertEqual(arith.int_sqrt(0.148), 0)
        self.assertEqual(arith.int_sqrt(0.541), 1)
        
    def test_mod_mutliply(self):
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

    def test_quadratic_roots(self):
        roots = sorted(arith.quadratic_roots(1, 0, -1))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -1)
        self.assertAlmostEqual(roots[1], 1)

        roots = sorted(arith.quadratic_roots(1, -1, -1))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -0.61803399)
        self.assertAlmostEqual(roots[1], 1.61803399)

        roots = sorted(arith.quadratic_roots(1, 3, -4))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -4)
        self.assertAlmostEqual(roots[1], 1)

        roots = sorted(arith.quadratic_roots(2, 4, -4))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -2.7320508)
        self.assertAlmostEqual(roots[1], 0.7320508)

        roots = sorted(arith.quadratic_roots(2, -4, -3))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], -0.58113883)
        self.assertAlmostEqual(roots[1], 2.58113883)

        roots = sorted(arith.quadratic_roots(-27, 643, -11))
        self.assertEqual(len(roots), 2)
        self.assertAlmostEqual(roots[0], 0.01711962)
        self.assertAlmostEqual(roots[1], 23.7976952)

        def get_imag(x):
            return x.imag

        roots = sorted(arith.quadratic_roots(1, 0, 1), key=get_imag)
        self.assertEqual(len(roots), 2)
        self.assertTrue(isinstance(roots[0], complex))
        self.assertTrue(isinstance(roots[1], complex))
        self.assertAlmostEqual(roots[0].real, 0)
        self.assertAlmostEqual(roots[0].imag, -1)
        self.assertAlmostEqual(roots[1].real, 0)
        self.assertAlmostEqual(roots[1].imag, 1)

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
