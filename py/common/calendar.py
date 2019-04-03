#!/usr/bin/env python3

"""Common library for working with calendar dates.

This module provides constants and functions related to calendar dates and
associated units of time, such as days, months, and years. Examples include
enums and counts for the days of the week and months of the year, the number of
days in each month, and a test for whether a given year is a leap year.
"""

from enum import Enum
from typing import Mapping


class Day(Enum):
    """Enum representing days of the week, from Sunday to Saturday."""

    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6

    def __repr__(self) -> str:
        return self.name


class Month(Enum):
    """Enum representing months of the year, from January to December."""

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

    def __repr__(self) -> str:
        return self.name


#: Number of days in a week.
DAYS_IN_WEEK = 7

#: Number of days in a calendar year.
DAYS_IN_YEAR = 365

#: Number of days in each month.
MONTH_DAY_COUNTS: Mapping[Month, int] = {
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

#: Number of months in a calendar year.
MONTHS_IN_YEAR = 12


def is_leap_year(year: int) -> bool:
    """Checks if a given year is, was, or will be a leap year.

    Args:
        year: An integer representing a common-era year, e.g. 1984 CE.

    Returns:
        ``True`` if ``year`` is a leap year, meaning it contains one additional
        day in February, for a total of 366 days. Returns ``False`` otherwise.
    """
    if year % 100 != 0:
        # year is not a century; it is a leap year if divisible by 4
        return year % 4 == 0
    else:
        # year is a century; it is a leap year only if divisible by 400
        return year % 400 == 0
