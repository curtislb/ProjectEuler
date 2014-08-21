'''
Problem 10.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below LIMIT.

@author: Curtis Belmonte
'''

LIMIT = 2000000 # default: 2000000

###############################################################################

from common import primes_up_to

print(sum(primes_up_to(LIMIT - 1)))
