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
  
How many DAY_OF_WEEKs fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

DAY_OF_WEEK = com.Day.SUNDAY # default: com.Day.SUNDAY
# TODO: parameterize date range

# SOLUTION ####################################################################

# Number of days in each month
month_day_counts = [
    31 # January
  , 28 # February (non-leap year)
  , 31 # March
  , 30 # April
  , 31 # May
  , 30 # June
  , 31 # July
  , 31 # August
  , 30 # September
  , 31 # October
  , 30 # November
  , 31 # December
]

# Additional useful constants
days_in_week = 7
days_in_year = 365
months_in_year = 12


def solve():
    # advance day from Monday, 1 Jan 1900 to 1 Jan 1901
    start_year = 1900
    day = com.Day.MONDAY
    day = (day + days_in_year + com.is_leap_year(start_year)) % days_in_week

    # count occurrences of DAY_OF_WEEK on the first of each month
    end_year = 2001
    first_day_count = 0
    for year in range(start_year + 1, end_year):
        for month in range(com.Month.JANUARY, months_in_year):
            # count the number of days in the current month
            days_in_month = month_day_counts[month]
            if month == com.Month.FEBRUARY:
                days_in_month += com.is_leap_year(year)

            # check if the first day of the month is Sunday
            if day == com.Day.SUNDAY:
                first_day_count += 1

            # advance day by one month
            day = (day + days_in_month) % days_in_week

    return first_day_count


if __name__ == '__main__':
    print(solve())
