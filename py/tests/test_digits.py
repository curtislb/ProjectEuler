#!/usr/bin/env python3

"""test_digits.py

Unit test for the 'digits' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.digits as digs


class TestDigits(unittest.TestCase):
    def test_concat_digits(self) -> None:
        self.assertEqual(digs.concat_digits([0]), 0)
        self.assertEqual(digs.concat_digits([1]), 1)
        self.assertEqual(digs.concat_digits([0, 1]), 1)
        self.assertEqual(digs.concat_digits([1, 2]), 12)
        self.assertEqual(digs.concat_digits((3, 2, 1)), 321)
        self.assertEqual(digs.concat_digits(range(0, 7, 2)), 246)
        self.assertEqual(digs.concat_digits([1, 0, 0, 1], 2), 9)
        self.assertEqual(digs.concat_digits([1, 7, 3, 4], 8), 988)
        self.assertEqual(digs.concat_digits([3, 'D', 'c', 0], 16), 15808)

    def test_concat_numbers(self) -> None:
        self.assertEqual(digs.concat_numbers(0, 1), 1)
        self.assertEqual(digs.concat_numbers(1, 0), 10)
        self.assertEqual(digs.concat_numbers(2, 3), 23)
        self.assertEqual(digs.concat_numbers(-2, 3), -23)
        self.assertEqual(digs.concat_numbers(123, 45), 12345)
        self.assertEqual(digs.concat_numbers(1, 2345), 12345)
        with self.assertRaises(ValueError):
            digs.concat_numbers(2, -3)

    def test_count_digits(self) -> None:
        self.assertEqual(digs.count_digits(0), 1)
        self.assertEqual(digs.count_digits(1), 1)
        self.assertEqual(digs.count_digits(9), 1)
        self.assertEqual(digs.count_digits(10), 2)
        self.assertEqual(digs.count_digits(1337), 4)
        self.assertEqual(digs.count_digits(63184285379), 11)

    def test_decimal_digits(self) -> None:
        self.assertEqual(digs.decimal_digits(0, 0), 0)
        self.assertEqual(digs.decimal_digits(1, 0), 1)
        self.assertEqual(digs.decimal_digits(1, 1), 10)
        self.assertEqual(digs.decimal_digits(-1, 1), -10)
        self.assertEqual(digs.decimal_digits(1, 2), 100)
        self.assertEqual(digs.decimal_digits(0.2, 2), 20)
        self.assertEqual(digs.decimal_digits(-0.2, 2), -20)
        self.assertEqual(digs.decimal_digits(0.1337, 3), 134)
        self.assertEqual(digs.decimal_digits(0.1334, 3), 133)
        self.assertEqual(digs.decimal_digits(0.6271361253, 6), 627136)
        self.assertEqual(digs.decimal_digits(49.95804784, 5), 4995805)

    def test_digit_counts(self) -> None:
        self.assertEqual(digs.digit_counts(1), [0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(digs.digit_counts(9), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(digs.digit_counts(10), [1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(digs.digit_counts(99), [0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
        self.assertEqual(digs.digit_counts(1234567890), [1] * 10)
        self.assertEqual(
            digs.digit_counts(490473284389948786968728452),
            [1, 0, 3, 2, 5, 1, 2, 3, 6, 4])

    def test_digit_function_sum(self) -> None:
        self.assertEqual(digs.digit_function_sum(0, lambda x: x), 0)
        self.assertEqual(digs.digit_function_sum(1, lambda x: x), 1)
        self.assertEqual(digs.digit_function_sum(123, lambda x: x), 6)
        self.assertEqual(digs.digit_function_sum(123, lambda x: x + 1), 9)
        self.assertEqual(digs.digit_function_sum(123, lambda x: x**2), 14)
        self.assertEqual(
            digs.digit_function_sum(
                7948531,
                lambda x: -x if x % 2 == 1 else x),
            -13)

    def test_digit_permutations(self) -> None:
        self.assertCountEqual(digs.digit_permutations(1), [1])
        self.assertCountEqual(digs.digit_permutations(2), [2])
        self.assertCountEqual(digs.digit_permutations(10), [10])
        self.assertCountEqual(digs.digit_permutations(11), [11])
        self.assertCountEqual(digs.digit_permutations(12), [12, 21])
        self.assertCountEqual(
            digs.digit_permutations(123),
            [123, 132, 213, 231, 312, 321])
        self.assertCountEqual(
            digs.digit_permutations(1337),
            [1337, 1373, 1733, 3137, 3173, 3317, 3371, 3713, 3731, 7133, 7313,
             7331])

    def test_digit_rotations(self) -> None:
        self.assertCountEqual(digs.digit_rotations(1), [1])
        self.assertCountEqual(digs.digit_rotations(2), [2])
        self.assertCountEqual(digs.digit_rotations(10), [1, 10])
        self.assertCountEqual(digs.digit_rotations(11), [11])
        self.assertCountEqual(digs.digit_rotations(12), [12, 21])
        self.assertCountEqual(digs.digit_rotations(123), [123, 231, 312])
        self.assertCountEqual(
            digs.digit_rotations(600316),
            [600316, 3166, 31660, 316600, 166003, 660031])

    def test_digit_truncations_left(self) -> None:
        self.assertCountEqual(digs.digit_truncations_left(1), [1])
        self.assertCountEqual(digs.digit_truncations_left(2), [2])
        self.assertCountEqual(digs.digit_truncations_left(10), [10, 0])
        self.assertCountEqual(digs.digit_truncations_left(12), [12, 2])
        self.assertCountEqual(digs.digit_truncations_left(1002), [1002, 2])
        self.assertCountEqual(digs.digit_truncations_left(123), [123, 23, 3])
        self.assertCountEqual(
            digs.digit_truncations_left(600316),
            [600316, 316, 16, 6])

    def test_digit_truncations_right(self) -> None:
        self.assertCountEqual(digs.digit_truncations_right(1), [1])
        self.assertCountEqual(digs.digit_truncations_right(2), [2])
        self.assertCountEqual(digs.digit_truncations_right(10), [10, 1])
        self.assertCountEqual(digs.digit_truncations_right(12), [12, 1])
        self.assertCountEqual(digs.digit_truncations_right(123), [123, 12, 1])
        self.assertCountEqual(
            digs.digit_truncations_right(1002),
            [1002, 100, 10, 1])
        self.assertCountEqual(
            digs.digit_truncations_right(600316),
            [600316, 60031, 6003, 600, 60, 6])

    def test_digits(self) -> None:
        self.assertEqual(digs.digits(1), [1])
        self.assertEqual(digs.digits(2), [2])
        self.assertEqual(digs.digits(123), [1, 2, 3])
        self.assertEqual(digs.digits(1337), [1, 3, 3, 7])
        self.assertEqual(
            digs.digits(698873214754301820),
            [6, 9, 8, 8, 7, 3, 2, 1, 4, 7, 5, 4, 3, 0, 1, 8, 2, 0])
        
    def test_get_digit(self) -> None:
        self.assertEqual(digs.get_digit(1, 1), 1)
        self.assertEqual(digs.get_digit(2, 1), 2)
        self.assertEqual(digs.get_digit(123, 2), 2)
        self.assertEqual(digs.get_digit(4567, 4), 7)
        self.assertEqual(digs.get_digit(89, 0), 9)
        self.assertEqual(digs.get_digit(201709364, 7), 3)
        
    def test_int_to_base(self) -> None:
        self.assertEqual(digs.int_to_base(1, 2), '1')
        self.assertEqual(digs.int_to_base(1, 10), '1')
        self.assertEqual(digs.int_to_base(2, 2), '10')
        self.assertEqual(digs.int_to_base(2, 10), '2')
        self.assertEqual(digs.int_to_base(25, 2), '11001')
        self.assertEqual(digs.int_to_base(25, 3), '221')
        self.assertEqual(digs.int_to_base(25, 5), '100')
        self.assertEqual(digs.int_to_base(25, 8), '31')
        self.assertEqual(digs.int_to_base(25, 10), '25')
        self.assertEqual(digs.int_to_base(25, 16), '19')
        self.assertEqual(digs.int_to_base(595129651, 36), '9uboz7')
        self.assertEqual(digs.int_to_base(42, 3, '?!#'), '!!#?')
        
    def test_is_bouncy(self) -> None:
        self.assertFalse(digs.is_bouncy(1))
        self.assertFalse(digs.is_bouncy(9))
        self.assertFalse(digs.is_bouncy(11))
        self.assertFalse(digs.is_bouncy(12))
        self.assertFalse(digs.is_bouncy(21))
        self.assertFalse(digs.is_bouncy(111))
        self.assertFalse(digs.is_bouncy(119))
        self.assertFalse(digs.is_bouncy(199))
        self.assertFalse(digs.is_bouncy(100))
        self.assertFalse(digs.is_bouncy(110))
        self.assertFalse(digs.is_bouncy(66420))
        self.assertFalse(digs.is_bouncy(134468))
        self.assertFalse(digs.is_bouncy(99964332))
        self.assertTrue(digs.is_bouncy(120))
        self.assertTrue(digs.is_bouncy(412))
        self.assertTrue(digs.is_bouncy(525))
        self.assertTrue(digs.is_bouncy(738))
        self.assertTrue(digs.is_bouncy(12951))
        self.assertTrue(digs.is_bouncy(21780))
        self.assertTrue(digs.is_bouncy(155349))
        self.assertTrue(digs.is_bouncy(277032))
        self.assertTrue(digs.is_bouncy(47894411))
        
    def test_is_palindrome(self) -> None:
        self.assertTrue(digs.is_palindrome(1))
        self.assertTrue(digs.is_palindrome(11))
        self.assertTrue(digs.is_palindrome(22))
        self.assertFalse(digs.is_palindrome(10))
        self.assertTrue(digs.is_palindrome(101))
        self.assertFalse(digs.is_palindrome(1212))
        self.assertTrue(digs.is_palindrome(2332))
        self.assertTrue(digs.is_palindrome(72427))
        self.assertTrue(digs.is_palindrome(724427))
        self.assertTrue(digs.is_palindrome(722444227))
        self.assertFalse(digs.is_palindrome(513513))
        self.assertFalse(digs.is_palindrome(551133))
        self.assertFalse(digs.is_palindrome(5133150))
        
    def test_make_palindrome(self) -> None:
        self.assertEqual(digs.make_palindrome(1), 11)
        self.assertEqual(digs.make_palindrome(1, base=2), 0b11)
        self.assertEqual(digs.make_palindrome(1, odd_length=True), 1)
        self.assertEqual(digs.make_palindrome(1, base=2, odd_length=True), 1)
        self.assertEqual(digs.make_palindrome(25), 2552)
        self.assertEqual(digs.make_palindrome(0o31, base=8), 0o3113)
        self.assertEqual(digs.make_palindrome(25, odd_length=True), 252)
        self.assertEqual(
            digs.make_palindrome(0o31, base=8, odd_length=True),
            0o313)
        self.assertEqual(digs.make_palindrome(1347), 13477431)
        self.assertEqual(digs.make_palindrome(0x543, base=16), 0x543345)
        self.assertEqual(digs.make_palindrome(1347, odd_length=True), 1347431)
        self.assertEqual(
            digs.make_palindrome(0x543, base=16, odd_length=True),
            0x54345)
        
    def test_pandigital_string(self) -> None:
        self.assertEqual(digs.pandigital_string(), '0123456789')
        self.assertEqual(digs.pandigital_string(first=0), '0123456789')
        self.assertEqual(digs.pandigital_string(first=3), '3456789')
        self.assertEqual(digs.pandigital_string(first=9), '9')
        self.assertEqual(digs.pandigital_string(last=0), '0')
        self.assertEqual(digs.pandigital_string(last=4), '01234')
        self.assertEqual(digs.pandigital_string(last=9), '0123456789')
        self.assertEqual(digs.pandigital_string(first=0, last=9), '0123456789')
        self.assertEqual(digs.pandigital_string(first=5, last=9), '56789')
        self.assertEqual(digs.pandigital_string(first=0, last=8), '012345678')
        self.assertEqual(digs.pandigital_string(first=2, last=6), '23456')
        
    def test_sum_digits(self) -> None:
        self.assertEqual(digs.sum_digits(1), 1)
        self.assertEqual(digs.sum_digits(2), 2)
        self.assertEqual(digs.sum_digits(10), 1)
        self.assertEqual(digs.sum_digits(13), 4)
        self.assertEqual(digs.sum_digits(209), 11)
        self.assertEqual(digs.sum_digits(1337), 14)
        self.assertEqual(digs.sum_digits(609278806205509), 67)
        self.assertEqual(
            digs.sum_digits(9987223242228759440094102307791387034898),
            182)

    def test_sum_keep_digits(self) -> None:
        self.assertEqual(digs.sum_keep_digits(1, 2), 3)
        self.assertEqual(digs.sum_keep_digits(1, 2, d=1), 3)
        self.assertEqual(digs.sum_keep_digits(1, 2, d=2), 3)
        self.assertEqual(digs.sum_keep_digits(1, 2, d=100), 3)
        self.assertEqual(digs.sum_keep_digits(7, 3), 10)
        self.assertEqual(digs.sum_keep_digits(7, 3, d=1), 0)
        self.assertEqual(digs.sum_keep_digits(7, 3, d=2), 10)
        self.assertEqual(digs.sum_keep_digits(7, 3, d=3), 10)
        self.assertEqual(digs.sum_keep_digits(80, 175), 255)
        self.assertEqual(digs.sum_keep_digits(80, 175, d=1), 5)
        self.assertEqual(digs.sum_keep_digits(80, 175, d=2), 55)
        self.assertEqual(digs.sum_keep_digits(80, 175, d=3), 255)
        self.assertEqual(digs.sum_keep_digits(80, 175, d=4), 255)
        self.assertEqual(digs.sum_keep_digits(9008577767, 2942448238, d=1), 5)
        self.assertEqual(digs.sum_keep_digits(9008577767, 2942448238, d=3), 5)
        self.assertEqual(
            digs.sum_keep_digits(9008577767, 2942448238, d=6),
            26005)
        self.assertEqual(
            digs.sum_keep_digits(9008577767, 2942448238, d=7),
            1026005)
        self.assertEqual(
            digs.sum_keep_digits(9008577767, 2942448238, d=10),
            1951026005)
        self.assertEqual(
            digs.sum_keep_digits(9008577767, 2942448238, d=11),
            11951026005)
        self.assertEqual(
            digs.sum_keep_digits(9008577767, 2942448238, d=552),
            11951026005)
        self.assertEqual(
            digs.sum_keep_digits(9008577767, 2942448238),
            11951026005)


if __name__ == '__main__':
    unittest.main()
