/*
 * problem019.cpp
 * 
 * Problem 19: Counting Sundays
 *
 * You are given the following information, but you may prefer to do some
 * research for yourself.
 *
 * - 1 Jan 1900 was a Monday.
 * - Thirty days has September,
 *   April, June and November.
 *   All the rest have thirty-one,
 *   Saving February alone,
 *   Which has twenty-eight, rain or shine.
 *   And on leap years, twenty-nine.
 * - A leap year occurs on any year evenly divisible by 4, but not on a century
 *   unless it is divisible by 400.
 *
 * How many Sundays fell on the first of the month during the twentieth century
 * (1 Jan 1901 to 31 Dec 2000)?
 * 
 * Author: Curtis Belmonte
 * Created: Aug 29, 2014
 */

#include <iostream>

#include "common.h"

using namespace std;

/* PARAMETERS ****************************************************************/

// TODO: parameterize date range

/* SOLUTION ******************************************************************/

int main() {
    // number of days in each month
    const unsigned short kMonthDayCounts[] = {
            31 // January
          , 28 // February (non-leap year)
          , 31 // March
          , 30 // April
          , 31 // May
          , 30 // June
          , 31 // July
          , 31 // August
          , 30 // September
          , 31 // October
          , 30 // November
          , 31 // December
    };

    // months of the year
    enum {
        JANUARY = 0,
        FEBRUARY = 1
    };

    // days of the week
    enum {
        SUNDAY = 0,
        MONDAY = 1
    };

    // advance day from Monday, 1 Jan 1900 to 1 Jan 1901
    const unsigned short kDaysInWeek = 7;
    const unsigned short kDaysInYear = 365;
    const unsigned short kStartYear = 1900;
    unsigned short day = MONDAY;
    day = (day + kDaysInYear + common::isLeapYear(kStartYear)) % kDaysInWeek;

    // count occurrences of Sunday on the first of each month
    unsigned short days_in_month;
    unsigned int first_sunday_count = 0;
    const unsigned short kEndYear = 2001;
    const unsigned short kMonthsInYear = 12;
    for (unsigned short year = kStartYear + 1; year < kEndYear; year++) {
        for (unsigned short month = JANUARY; month < kMonthsInYear; month++) {
            // count the number of days in the current month
            days_in_month = kMonthDayCounts[month];
            if (month == FEBRUARY)
                days_in_month += common::isLeapYear(year);

            // check if the first day of the month is Sunday
            if (day == SUNDAY)
                first_sunday_count++;

            // advance day by one month
            day = (day + days_in_month) % kDaysInWeek;
        }
    }

    cout << first_sunday_count << endl;
    return 0;
}
