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

import common as com

# PARAMETERS ##################################################################

NUM_PRIMES = 4 # default: 5

# SOLUTION ####################################################################

def concats_prime(n, m):
    return (com.is_prime(com.concat_numbers(n, m)) and
            com.is_prime(com.concat_numbers(m, n)))


def find_prime_sets(primes, prev_prime_sets=None):
    if prev_prime_sets is None:
        return [[prime] for prime in primes]

    prime_sets = []
    for prime in primes:
        for prime_set in prev_prime_sets:
            if prime in prime_set:
                continue
            all_prime = True
            for prev_prime in prime_set:
                if not concats_prime(prev_prime, prime):
                    all_prime = False
                    break
            if all_prime:
                prime_sets.append(prime_set + [prime])
    return prime_sets


def solve():
    primes = com.primes_up_to(750)[1:]
    prime_sets = None
    for __ in range(NUM_PRIMES):
        prime_sets = find_prime_sets(primes, prime_sets)
    sorted_sets = com.sort_by(prime_sets, [sum(ps) for ps in prime_sets])
    return sorted_sets[0]


if __name__ == '__main__':
    print(solve())
