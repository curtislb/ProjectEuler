"""problem_002.py

Problem 2: Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
LIMIT, find the sum of the even-valued terms.

@author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

LIMIT = 4000000 # default: 4000000

# SOLUTION ####################################################################

def solve():
    # sum every third (even) Fibonacci number
    i = -1
    fib_num = 0
    total = 0
    while fib_num <= LIMIT:
        total += fib_num
        i += 3
        fib_num = com.fibonacci(i)

    return total


if __name__ == '__main__':
    print(solve())
