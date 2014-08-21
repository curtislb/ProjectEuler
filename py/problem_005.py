'''
Problem 5.

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to MAX?

@author: Curtis Belmonte
'''

MAX = 20 # default: 20

###############################################################################

from common import lcm

all_nums = range(2, MAX + 1)
print(lcm(*all_nums))
