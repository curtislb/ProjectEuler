#!/usr/bin/env python3

"""problem_087.py

Problem 87: Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and
prime fourth power is 28. In fact, there are exactly four numbers below fifty
that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below LIMIT can be expressed as the sum of a prime square,
prime cube, and prime fourth power?

Author: Curtis Belmonte
"""

import math

import common.primes as prime


# PARAMETERS ##################################################################


LIMIT = 5 * 10**7 # default: 5 * 10**7


# SOLUTION ####################################################################


def solve() -> int:
    # precompute all primes up to the square root of LIMIT
    primes = prime.primes_up_to(int(math.sqrt(LIMIT)) + 1)
    
    # store all squares, cubes, and fourth powers of primes
    prime_squares = []
    prime_cubes = []
    prime_fourths = []
    for p in primes:
        power = p**2
        prime_squares.append(power)

        power *= p
        prime_cubes.append(power)

        power *= p
        prime_fourths.append(power)

    # add all distinct power sums below LIMIT to answers
    answers = set()
    for square in prime_squares:
        if square >= LIMIT:
            break
        for cube in prime_cubes:
            sc_sum = square + cube
            if sc_sum >= LIMIT:
                break
            for fourth in prime_fourths:
                scf_sum = sc_sum + fourth
                if scf_sum >= LIMIT:
                    break
                answers.add(scf_sum)

    return len(answers)


if __name__ == '__main__':
    print(solve())
