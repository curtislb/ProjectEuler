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
  
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

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
days_in_year = 365

# Months of the year
class Month:
    JANUARY = 0
    FEBRUARY = 1
months_in_year = 12

# Days of the week
class Day:
    SUNDAY = 0
    MONDAY = 1
days_in_week = 7

if __name__ == '__main__':
    # advance day from Monday, 1 Jan 1900 to 1 Jan 1901
    start_year = 1900
    day = Day.MONDAY
    day = (day + days_in_year + common.is_leap_year(start_year)) % days_in_week

    # count occurrences of Sunday on the first of each month
    first_sunday_count = 0
    end_year = 2001
    for year in range(start_year + 1, end_year):
        for month in range(Month.JANUARY, months_in_year):
            # count the number of days in the current month
            days_in_month = month_day_counts[month]
            if month == Month.FEBRUARY:
                days_in_month += common.is_leap_year(year)

            # check if the first day of the month is Sunday
            if day == Day.SUNDAY:
                first_sunday_count += 1

            # advance day by one month
            day = (day + days_in_month) % days_in_week

    print(first_sunday_count)
