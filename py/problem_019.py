#!/usr/bin/env python3

"""problem_019.py

Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research
for yourself.

- 1 Jan 1900 was a Monday.
- Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.
  
How many DAY_OF_WEEKs fell on the first of the month from 1 Jan 1901 up until
(but excluding) the start of END_YEAR?
"""

__author__ = 'Curtis Belmonte'

import common.calendar as cal
from common.calendar import Day, Month

# PARAMETERS ##################################################################

DAY_OF_WEEK = Day.SUNDAY # default: Day.SUNDAY

END_YEAR = 2001 # default: 2001

# SOLUTION ####################################################################


def solve() -> int:
    # advance day from Monday, 1 Jan 1900 to 1 Jan 1901
    start_year = 1900
    leap_days = 1 if cal.is_leap_year(start_year) else 0
    num_days = Day.MONDAY.value + cal.DAYS_IN_YEAR + leap_days
    day = Day(num_days % cal.DAYS_IN_WEEK)

    # count occurrences of DAY_OF_WEEK on the first of each month
    first_day_count = 0
    for year in range(start_year + 1, END_YEAR):
        for month_value in range(Month.JANUARY.value, cal.MONTHS_IN_YEAR):
            month = Month(month_value)

            # count the number of days in the current month
            days_in_month = cal.MONTH_DAY_COUNTS[month]
            if month == Month.FEBRUARY:
                days_in_month += cal.is_leap_year(year)

            # check if the first day of the month is Sunday
            if day == Day.SUNDAY:
                first_day_count += 1

            # advance day by one month
            day = Day((day.value + days_in_month) % cal.DAYS_IN_WEEK)

    return first_day_count


if __name__ == '__main__':
    print(solve())
