#!/usr/bin/env python3

"""calendar.py



Author: Curtis Belmonte
"""


# Number of days in a week
DAYS_IN_WEEK = 7

# Number of days in a calendar year
DAYS_IN_YEAR = 365

# Number of days in each month
MONTH_DAY_COUNTS = [
  31, # January
  28, # February (non-leap year)
  31, # March
  30, # April
  31, # May
  30, # June
  31, # July
  31, # August
  30, # September
  31, # October
  30, # November
  31, # December
]

# Number of months in a calendar year
MONTHS_IN_YEAR = 12


class Day:
    """Enum representing days of the week."""
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Month:
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


def is_leap_year(year):
    """Determines if year (given in years A.D.) is a leap year."""
    if year % 100 != 0:
        # year is not a century; it is a leap year if divisible by 4
        return year % 4 == 0
    else:
        # year is a century; it is a leap year only if divisible by 400
        return year % 400 == 0
