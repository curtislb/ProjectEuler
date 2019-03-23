#!/usr/bin/env python3

"""calendar.py

Constants and functions for working with calendar dates.
"""

__author__ = 'Curtis Belmonte'

from enum import Enum


class Day(Enum):
    """Enum representing days of the week."""
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Month(Enum):
    """Enum representing months of the year."""
    JANUARY = 0
    FEBRUARY = 1
    MARCH = 2
    APRIL = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUGUST = 7
    SEPTEMBER = 8
    OCTOBER = 9
    NOVEMBER = 10
    DECEMBER = 11


# Number of days in a week
DAYS_IN_WEEK = 7

# Number of days in a calendar year
DAYS_IN_YEAR = 365

# Number of days in each month
MONTH_DAY_COUNTS = {
  Month.JANUARY: 31,
  Month.FEBRUARY: 28,  # (non-leap year)
  Month.MARCH: 31,
  Month.APRIL: 30,
  Month.MAY: 31,
  Month.JUNE: 30,
  Month.JULY: 31,
  Month.AUGUST: 31,
  Month.SEPTEMBER: 30,
  Month.OCTOBER: 31,
  Month.NOVEMBER: 30,
  Month.DECEMBER: 31,
}

# Number of months in a calendar year
MONTHS_IN_YEAR = 12


def is_leap_year(year: int) -> bool:
    """Determines if year (given in years A.D.) is a leap year."""
    if year % 100 != 0:
        # year is not a century; it is a leap year if divisible by 4
        return year % 4 == 0
    else:
        # year is a century; it is a leap year only if divisible by 400
        return year % 400 == 0
