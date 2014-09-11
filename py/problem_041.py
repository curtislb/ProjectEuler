"""problem_041.py

Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

# N/A

# SOLUTION ####################################################################

# Array of 1 to n pandigital numbers for n from 2 to 7
PANDIGIT_STRINGS = [common.pandigital_string(1, n) for n in range(2, 8)]

if __name__ == '__main__':
    # compute primes up to maximum possible pandigital number
    # note: 1 to 8 or 9 pandigital numbers cannot be prime (divisible by 3)
    primes = common.primes_up_to(7654321)
    
    # check if each prime is 1 to n pandigital in decreasing order
    i = -1
    prime = primes[i]
    digit_count = common.count_digits(prime)
    while not common.is_permutation(str(prime),
                                    PANDIGIT_STRINGS[digit_count - 2]):
        # advance to next largest prime number
        i -= 1
        prime = primes[i]
        digit_count = common.count_digits(prime)
    
    # print largest prime that satisfies the conditions
    print(primes[i])
