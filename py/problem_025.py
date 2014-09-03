"""problem_025.py

Problem 25: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

    F(n) = F(n−1) + F(n−2), where F(1) = 1 and F(2) = 1.

Hence the first 12 terms will be:

    F(1) = 1
    F(2) = 1
    F(3) = 2
    F(4) = 3
    F(5) = 5
    F(6) = 8
    F(7) = 13
    F(8) = 21
    F(9) = 34
    F(10) = 55
    F(11) = 89
    F(12) = 144

The 12th term, F(12), is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain D digits?

@author: Curtis Belmonte
"""

import common

# PARAMETERS ##################################################################

D = 1000 # default: 1000

# SOLUTION ####################################################################

if __name__ == '__main__':
    # search for Fibonacci number containing D digits
    n = 0
    fib_num = common.fibonacci(n)
    while common.count_digits(fib_num) < D:
        n += 1
        fib_num = common.fibonacci(n)
    
    # shift Fibonacci index so F(0) = 1, F(1) = 1 -> F(1) = 1, F(2) = 1
    print(n + 1)
