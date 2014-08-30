"""common.py

Common utility functions and classes for various Project Euler problems.

@author: Curtis Belmonte
"""

# PRIVATE VARIABLES ###########################################################

# Currently computed terms of the Fibonacci sequence (in sorted order).
_fibonacci_sequence = [1, 1]

# PRIVATE FUNCTIONS ###########################################################

def _compute_fibonacci(n):
    """Precomputes and stores the Fibonacci numbers up to F(n)."""
    fib_count = len(_fibonacci_sequence)

    # have the numbers up to F(n) already been computed?
    if n < fib_count:
        return

    # compute numbers iteratively from existing sequence
    f0 = _fibonacci_sequence[fib_count - 2]
    f1 = _fibonacci_sequence[fib_count - 1]
    for i in range(fib_count, n + 1):
        temp = f1
        f1 += f0
        f0 = temp
        _fibonacci_sequence.append(f1)

# PUBLIC FUNCTIONS ############################################################

def arith_series(a, n, d):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def fibonacci(n):
    """Returns the nth Fibonacci number, with F(0) = F(1) = 1."""
    _compute_fibonacci(n)
    return _fibonacci_sequence[n]


def gcd(m, n):
    """Returns the greatest common divisor of natural numbers m and n."""
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m


def lcm(m, n):
    """Returns the least common multiple of natural numbers m and n."""
    return m * n // gcd(m, n)
