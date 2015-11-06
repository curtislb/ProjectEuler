"""problem_023.py

Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers below LIMIT which cannot be written
as the sum of two abundant numbers.

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 28123 # default: 28123

# SOLUTION ####################################################################

def solve():
    total = 0
    abundant_nums = set()
    for n in range(1, min(LIMIT, 28123)):
        # check if n is the sum of any abundant number pairs seen so far
        sum_of_abundant = False
        for abundant_num in abundant_nums:
            diff = n - abundant_num
            if diff in abundant_nums:
                sum_of_abundant = True
                break
        
        # if n is not the sum of two abundant numbers, add it to total
        if not sum_of_abundant:
            total += n
        
        # check if n is an abundant number
        if com.sum_proper_divisors(n) > n:
            abundant_nums.add(n)
    
    return total


if __name__ == '__main__':
    print(solve())
