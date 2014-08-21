'''
Problem 41.

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

@author: Curtis Belmonte
'''

# [problem-defined constants]

###############################################################################

from common import digits, primes_up_to, run_thread

digit_sets = [{d for d in range(1, n)} for n in range(2, 11)]

n = -1
primes = list(primes_up_to(7654321))
p_digits = digits(primes[n])
num_digits = len(p_digits)
while not num_digits == sum(digit in p_digits
                            for digit in digit_sets[num_digits - 1]):
    n -= 1
    p_digits = digits(primes[n])
    num_digits = len(p_digits)
print(primes[n])
