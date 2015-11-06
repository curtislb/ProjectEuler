"""problem_050.py

Problem 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below 100.

The longest sum of consecutive primes below 1000 that adds to a prime, contains
21 terms, and is equal to 953.

Which prime, below LIMIT, can be written as the sum of the most consecutive
primes?

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 1000000 # default: 1000000

# SOLUTION ####################################################################

def solve():
    # TODO: find (provably) better lower bound on prime addend size
    primes = com.primes_up_to(max(1000, LIMIT // 10))
    num_primes = len(primes)
    
    # create matrix with primes along diagonal
    dyna_sums = [None] * num_primes
    for i in range(num_primes):
        dyna_sums[i] = [0] * num_primes
        dyna_sums[i][i] = primes[i]
    
    # compute dynamic sums, up to LIMIT - 1
    for j in range(1, num_primes):
        for i in range(j - 1, -1, -1):
            dyna_sum = dyna_sums[i][j - 1] + dyna_sums[j][j]
            if dyna_sum >= LIMIT:
                break
            else:
                dyna_sums[i][j] = dyna_sum
    
    # search for prime sum of max consecutive terms
    max_consec = -1
    best_prime = -1
    for i in range(num_primes):
        for j in range(i, num_primes):
            # stop searching if no more sums < LIMIT in current row
            if dyna_sums[i][j] == 0:
                break
            
            # check if sum meets criteria and is better than best so far
            if com.is_prime(dyna_sums[i][j]):
                consec = j - i + 1
                if consec > max_consec:
                    max_consec = consec
                    best_prime = dyna_sums[i][j]
    
    return best_prime


if __name__ == '__main__':
    print(solve())
