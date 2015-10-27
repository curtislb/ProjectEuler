"""problem_051.py

Problem 51: Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an 8 prime value family.

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

# N/A

# SOLUTION ####################################################################

# TODO: refactor to handle prime value families of any size
FAMILY_SIZE = 8


def main():
    families = set()
    
    # test 5-digit numbers
    for i in range(1, 5):
        for digit_i in range(10):
            for digit_one in range(10):
                count = 0
                family = []
                for digit_repl in range(10):
                    if count < FAMILY_SIZE - (10 - digit_repl):
                        break
                    
                    num = digit_one
                    for d in range(1, 5):
                        if d == i:
                            num += digit_i * 10**d
                        else:
                            num += digit_repl * 10**d
                    
                    if com.is_prime(num):
                        count += 1
                        family.append(num)
                        
                        if count == FAMILY_SIZE:
                            families.add(tuple(sorted(family)))
    
    # test 6-digit numbers
    for i in range(1, 6):
        for j in range(1, 6):
            for digit_i in range(10):
                for digit_j in range(10):
                    for digit_one in range(10):
                        count = 0
                        family = []
                        for digit_repl in range(10):
                            if count < FAMILY_SIZE - (10 - digit_repl):
                                break
                            
                            num = digit_one
                            for d in range(1, 6):
                                if d == i:
                                    num += digit_i * 10**d
                                elif d == j:
                                    num += digit_j * 10**d
                                else:
                                    num += digit_repl * 10**d
                            
                            if com.is_prime(num):
                                count += 1
                                family.append(num)
                                
                                if count == FAMILY_SIZE:
                                    families.add(tuple(sorted(family)))
    
    # find min prime that satisfies problem requirements
    min_primes = []                            
    for family in families:
        min_prime = family[0]
        digit_count = com.count_digits(min_prime)
        same_num_digits = True
        for prime in family[1:]:
            if com.count_digits(prime) != digit_count:
                same_num_digits = False
                break
            
            if same_num_digits:
                min_primes.append(min_prime)
    
    return min(min_primes)


if __name__ == '__main__':
    print(main())