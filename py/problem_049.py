"""problem_049.py

Problem 49: Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

@author: Curtis Belmonte
"""

import sys

import common

# PARAMETERS ##################################################################

# N/A

# SOLUTION ####################################################################

if __name__ == '__main__':
    # generate all four-digit primes
    primes = set(filter((lambda x: x > 999), common.primes_up_to(9999)))
    
    # remove sequence from problem description
    primes.remove(1487)
    primes.remove(4817)
    primes.remove(8147)
    
    # test all permutation groups in primes
    while len(primes) > 2:
        first = None
        perms = []
        
        # find all permutations of first prime in primes
        for prime in primes:
            if first is None:
                first = str(prime)
                perms.append(prime)
            elif common.is_permutation(first, str(prime)):
                perms.append(prime)
        
        # check if any three prime permutations form arithmetic sequence
        if len(perms) > 2:
            perms.sort()
            for i in range(len(perms)):
                for j in range(i + 1, len(perms)):
                    for k in range(j + 1, len(perms)):
                        if perms[j] - perms[i] == perms[k] - perms[j]:
                            print('%d%d%d' % (perms[i], perms[j], perms[k]))
                            sys.exit()
        
        # remove permutation group from primes
        for n in perms:
            primes.remove(n)

                