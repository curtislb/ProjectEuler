#!/usr/bin/env python3

"""problem_060.py

Problem 60: Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of NUM_PRIMES primes for which any two primes
concatenate to produce another prime.

Author: Curtis Belmonte
"""

import common.digits as digs
import common.primes as prime
import common.utility as util


# PARAMETERS ##################################################################


NUM_PRIMES = 5 # default: 5


# SOLUTION ####################################################################


@util.memoized
def concats_prime(n, m):
    """Determines if n and m can concatenate in either order to form primes."""
    return (prime.is_prime(digs.concat_numbers(n, m)) and
            prime.is_prime(digs.concat_numbers(m, n)))


def find_prime_sets(primes, prev_prime_sets=None):
    """Incrementally builds prime sets from prev_prime_sets, using primes."""

    # first iteration, return each prime in individual set
    if prev_prime_sets is None:
        return set((p,) for p in primes)

    # find prime sets with size one greater than previous
    prime_sets = set()
    for p in primes:
        for prev_set in prev_prime_sets:
            # don't duplicate primes in a set
            if p in prev_set:
                continue

            # don't duplicate sets of the same primes
            prime_set = tuple(sorted(prev_set + (p,)))
            if prime_set in prime_sets:
                continue

            # check if new prime concatenates with all prev primes
            all_prime = True
            for prev_p in prev_set:
                # ensure that p1 <= p2 for memoization
                p1, p2 = prev_p, p
                if p1 > p2:
                    p1, p2 = p2, p1

                if not concats_prime(p1, p2):
                    all_prime = False
                    break

            # if valid, add this prime pair set to running list
            if all_prime:
                prime_sets.add(prime_set)

    return prime_sets


def solve():
    # divide primes into those with remainders 1 and 2 mod 3
    one_primes = [3]
    two_primes = [3]
    for p in prime.primes_up_to(10000)[2:]:
        if p % 3 == 1:
            one_primes.append(p)
        else:
            two_primes.append(p)

    # look for prime pair sets within 1-primes and 2-primes
    one_prime_sets = None
    two_prime_sets = None
    for _ in range(NUM_PRIMES):
        one_prime_sets = find_prime_sets(one_primes, one_prime_sets)
        two_prime_sets = find_prime_sets(two_primes, two_prime_sets)

    # find minimum sum of prime sets
    prime_sets = list(one_prime_sets) + list(two_prime_sets)
    return min(map(sum, prime_sets))


if __name__ == '__main__':
    print(solve())
