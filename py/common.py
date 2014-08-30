"""common.py

Common utility functions and classes for various Project Euler problems.

@author: Curtis Belmonte
"""

# PRIVATE VARIABLES ###########################################################

# Currently computed terms of the Fibonacci sequence (in sorted order)
_fibonacci_sequence = [1, 1]

# Currently computed prime number terms (in sorted order)
_prime_sequence = [2]

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


def _compute_primes_up_to(n):
    """Precomputes and stores the prime numbers up to n."""

    # have the numbers up to n already been computed?
    prime_max = _prime_sequence[-1]
    if prime_max >= n:
        return

    # prepare sieve of Eratosthenes for numbers prime_max + 1 to n
    sieve_size = n - prime_max
    print(sieve_size)
    sieve = [True] * sieve_size

    # sift out composite numbers using previously computed primes
    prime_count = len(_prime_sequence)
    for i in range(prime_count):
        rho = _prime_sequence[i]
        for j in range(rho*rho, sieve_size + prime_max + 1, rho):
            if j < prime_max + 1:
                continue
            sieve[j - prime_max - 1] = False

    # sift out remaining composite numbers with newly found primes
    for i in range(sieve_size):
        if sieve[i]:
            rho = i + prime_max + 1
            _prime_sequence.append(rho)
            for j in range(rho*rho - prime_max - 1, sieve_size, rho):
                sieve[j] = False

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


def is_palindrome(n):
    """Determines if the natural number n is a palindrome."""
    
    n_str = str(n)
    
    # compare chars iteratively from beginning and end of string
    i = 0
    j = len(n_str) - 1
    while (i < j):
        if n_str[i] != n_str[j]:
            return False
        i += 1
        j -= 1
    return True


def lcm(m, n):
    """Returns the least common multiple of natural numbers m and n."""
    return m * n // gcd(m, n)


def prime_factorization(n):
    """Computes the prime factorization of the natural number n.
    
    Returns a list of base-exponent pairs containing each prime factor and
    its power in the prime factorization of n."""
    
    factorization = []

    i = 2
    while i <= n:
        # compute power of i in factorization
        factor = [i, 0]
        while n % i == 0:
            n //= i
            factor[1] += 1

        # add factor to factorization if necessary
        if factor[1] > 0:
            factorization.append(factor)
            
        i += 1

    return factorization


def primes_up_to(n):
    """Returns the prime numbers up to p in sorted order."""
    # find the index of the last prime <= n
    i = 0
    prime_count = len(_prime_sequence)
    while i < prime_count and _prime_sequence[i] <= n:
        i += 1

    return _prime_sequence[:i]