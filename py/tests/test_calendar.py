#!/usr/bin/env python3

"""test_calendar.py

Unit test for the 'calendar' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

import common.calendar as cal


class TestCalendar(unittest.TestCase):
    def test_is_leap_year(self) -> None:
        self.assertFalse(cal.is_leap_year(1))
        self.assertTrue(cal.is_leap_year(4))
        self.assertTrue(cal.is_leap_year(40))
        self.assertFalse(cal.is_leap_year(100))
        self.assertTrue(cal.is_leap_year(104))
        self.assertTrue(cal.is_leap_year(400))
        self.assertTrue(cal.is_leap_year(1248))
        self.assertFalse(cal.is_leap_year(1337))
        self.assertFalse(cal.is_leap_year(1800))
        self.assertTrue(cal.is_leap_year(1804))
        self.assertTrue(cal.is_leap_year(1804))
        self.assertTrue(cal.is_leap_year(2016))
        self.assertFalse(cal.is_leap_year(2017))
        self.assertFalse(cal.is_leap_year(2300))
        self.assertTrue(cal.is_leap_year(2400))
        self.assertTrue(cal.is_leap_year(4936))
        self.assertFalse(cal.is_leap_year(4937))
        self.assertFalse(cal.is_leap_year(4938))


if __name__ == '__main__':
    unittest.main()
