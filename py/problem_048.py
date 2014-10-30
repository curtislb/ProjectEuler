"""problem_048.py

Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last D digits of the series, 1^1 + 2^2 + 3^3 + ... + MAX^MAX.

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

D = 10 # default: 10
MAX = 1000 # default: 1000

# SOLUTION ####################################################################

if __name__ == '__main__':
    total = 0
    for n in range(1, MAX + 1):
        total = common.sum_keep_digits(total, n**n, D)
    print(total)
