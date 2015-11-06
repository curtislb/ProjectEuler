"""problem_063.py

Problem 63: Powerful digit counts

The 5-digit number, 16807 = 7**5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

@author: Curtis Belmonte
"""

import common as com

# SOLUTION ####################################################################

N_MAX = 21 # default: 21

# PARAMETERS ##################################################################

def solve():
    ans_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for n in range(2, N_MAX + 1):
        b = 2
        bn = b**n
        bn_digits = com.count_digits(bn)
        while bn_digits <= n:
            if bn_digits == n:
                ans_set.add(bn)
            b += 1
            bn = b**n
            bn_digits = com.count_digits(bn)
    return len(ans_set)


if __name__ == '__main__':
    print(solve())
