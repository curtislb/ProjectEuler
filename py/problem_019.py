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

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

DAY_OF_WEEK = common.Day.SUNDAY # default: common.Day.SUNDAY
# TODO: parameterize date range

# SOLUTION ####################################################################

# Number of days in each month
MONTH_DAY_COUNTS = [
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
DAYS_IN_WEEK = 7
DAYS_IN_YEAR = 365
MONTHS_IN_YEAR = 12

if __name__ == '__main__':
    # advance day from Monday, 1 Jan 1900 to 1 Jan 1901
    START_YEAR = 1900
    day = common.Day.MONDAY
    day = (day + DAYS_IN_YEAR + common.is_leap_year(START_YEAR)) % DAYS_IN_WEEK

    # count occurrences of DAY_OF_WEEK on the first of each month
    END_YEAR = 2001
    first_day_count = 0
    for year in range(START_YEAR + 1, END_YEAR):
        for month in range(common.Month.JANUARY, MONTHS_IN_YEAR):
            # count the number of days in the current month
            days_in_month = MONTH_DAY_COUNTS[month]
            if month == common.Month.FEBRUARY:
                days_in_month += common.is_leap_year(year)

            # check if the first day of the month is Sunday
            if day == common.Day.SUNDAY:
                first_day_count += 1

            # advance day by one month
            day = (day + days_in_month) % DAYS_IN_WEEK

    print(first_day_count)
