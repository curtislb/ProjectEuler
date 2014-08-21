'''
Problem 3.

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the natural number N?

@author: Curtis Belmonte
'''

N = 600851475143 # default: 600851475143

###############################################################################

from common import prime_factorization

print(max(prime_factorization(N)))
