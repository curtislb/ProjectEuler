'''
Problem 77.

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over N
different ways?
'''

N = 5000 # default: 5000

###############################################################################

from common import primes_up_to, sum_combos

primes = list(primes_up_to(2 * N))
n = 2
while sum_combos(n, primes) <= N:
    n += 1
print(n)