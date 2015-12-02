"""problem_063.py

Problem 63: Powerful digit counts

The 5-digit number, 16807 = 7**5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

# N/A

# SOLUTION ####################################################################

def solve():
    n_max = 21
    ans_set = set(range(1, 10))
    for n in range(2, n_max + 1):
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
