"""common.py

Common utility functions and classes for various Project Euler problems.

@author: Curtis Belmonte
"""

import collections
import functools
import math

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


def _compute_primes(n):
    """Precomputes and stores at least the first n prime numbers."""
    
    prime_count = len(_prime_sequence)

    # have the first n primes already been computed?
    if n < prime_count:
        return

    # TODO: implement incremental sieve?

    # based on analysis of OEIS data set A006880 and empirical time tests
    estimate = 100 if n <= 25 else int(n * math.log(n) * 1.05 + n * 0.87)
    increment = n / math.log(n)

    # compute primes up to estimate, then step forward until n are found
    i = estimate
    while len(_prime_sequence) < n:
        _compute_primes_up_to(i)
        i += increment


def _compute_primes_up_to(n):
    """Precomputes and stores the prime numbers up to n."""

    # have the numbers up to n already been computed?
    prime_max = _prime_sequence[-1]
    if prime_max >= n:
        return

    # prepare sieve of Eratosthenes for numbers prime_max + 1 to n
    sieve_size = n - prime_max
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

# PUBLIC DECORATORS ###########################################################

class memoized(object):
    """Decorator that caches the result of calling function with a particular
    set of arguments and returns this result for subsequent calls to function
    with the same arguments.
    
    Adapted from: https://wiki.python.org/moin/PythonDecoratorLibrary"""
    
    def __init__(self, function):
        self.function = function
        self.results = {}
    
    def __call__(self, *args):
        # if given arguments are not hashable, don't attempt any caching
        if not isinstance(args, collections.Hashable):
            return self.function(*args)
        
        # if result of running func on args has been cached, return it
        if args in self.results:
            return self.results[args]
        
        # evaluate function with args and store the result
        result = self.function(*args)
        self.results[args] = result
        return result
    
    def __get__(self, obj, objtype):
        # support decorating instance methods
        return functools.partial(self.__call__, obj)
    
    def __repr__(self):
        # return the docstring of the memoized function
        return self.function.__doc__

# PUBLIC FUNCTIONS ############################################################

def arith_series(a, n, d):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def count_divisors(n):
    """Returns the number of divisors of the natural number n."""
    
    # compute product of one more than the powers of its prime factors
    divisor_count = 1
    factorization = prime_factorization(n)
    for factor in factorization:
        divisor_count *= factor[1] + 1

    return divisor_count


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


def lcm_all(nums):
    """Returns the least common multiple of all natural numbers in nums."""
    
    max_powers = {}
    for num in nums:
        # compute powers of unique prime factors of the current number
        factorization = prime_factorization(num)
        for factor in factorization:
            if (factor[0] in max_powers and factor[1] > max_powers[factor[0]]
                or factor[0] not in max_powers):
                max_powers[factor[0]] = factor[1]
        
    # return the product of prime factors raised to their highest powers
    product = 1
    for factor in max_powers:
        product *= factor**max_powers[factor]
    return product


def numbers_from_file(input_file):
    """Returns a list of rows of integer numbers read from input_file."""
    
    with open(input_file) as file:
        # add each line from the input file as a row to the matrix
        matrix = []
        for line in file:
            # add each token from the current line to the row vector
            row = [int(num) for num in line[:-1].split()]
            matrix.append(row)
    
        return matrix


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


def prime(n):
    """Returns the nth prime number."""
    _compute_primes(n)
    return _prime_sequence[n - 1]


def primes(n):
    """Returns the first n prime numbers in sorted order."""
    _compute_primes(n)
    return _prime_sequence[:n]


def primes_up_to(n):
    """Returns the prime numbers up to p in sorted order."""
    
    _compute_primes_up_to(n)

    # find the index of the last prime <= n
    i = 0
    prime_count = len(_prime_sequence)
    while i < prime_count and _prime_sequence[i] <= n:
        i += 1

    return _prime_sequence[:i]


def sum_of_squares(n):
    """Returns the sum of the squares of the first n natural numbers."""
    return (2 * n**3 + 3 * n*n + n) // 6


def triangle(n):
    """Returns the nth triangle number, or the sum of the natural numbers up to
    and including n."""
    return n * (n + 1) // 2
