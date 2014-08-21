'''
Problem 47.

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first N consecutive integers to have N distinct primes factors. What
is the first of these numbers?

@author: Curtis Belmonte
'''

N = 4 # default: 4

###############################################################################

from collections import deque

from common import prime_factorization

if N < 4:
    n = (2, 14, 644)[N - 1]
else:
    n = 647

has_N_pfs = deque(len(prime_factorization(k).keys()) == N for k in range(n, n + N))

while sum(has_N_pfs) != N:
    n += 1
    has_N_pfs.popleft()
    has_N_pfs.append(len(prime_factorization(n + (N - 1)).keys()) == N)
print(n)
