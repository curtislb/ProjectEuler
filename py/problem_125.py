'''
Problem 125.

The palindromic number 595 is interesting because it can be written as the sum
of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as
consecutive square sums, and the sum of these palindromes is 4164.

@note: 1 = 0^2 + 1^2 has not been included as this problem is concerned with
the squares of positive integers.

Find the sum of all the numbers less than N that are both palindromic and can
be written as the sum of consecutive squares.

@author: Curtis Belmonte
'''

N = 10**8 # default: 10**8

###############################################################################

from common import arith_series, is_palindrome, sum_squares_to

k_max = 2
while sum_squares_to(k_max) < N:
    k_max += 1

palin_set = set()
for k in range(2, k_max):
    n = k
    while True:
        sqr_sum = k*n**2 - 2*n*arith_series(1, k - 1) + sum_squares_to(k - 1)
        if sqr_sum >= N:
            break
        if is_palindrome(sqr_sum):
            palin_set.add(sqr_sum)
        n += 1
print(sum(palin_set))