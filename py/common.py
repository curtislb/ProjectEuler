"""common.py

Common utility functions and classes for various Project Euler problems.

@author: Curtis Belmonte
"""

import collections
import math
import sys
import threading

# PRIVATE VARIABLES ###########################################################

# Currently computed factorial terms
_factorial_sequence = [1, 1]

# Currently computed terms of the Fibonacci sequence (in sorted order)
_fibonacci_sequence = [1, 1]

# Currently computed prime number terms (in sorted order)
_prime_sequence = [2]

# PRIVATE FUNCTIONS ###########################################################

def _compute_factorial(n):
    """Precomputes and stores the factorial terms up to n!."""
    
    FACT_COUNT = len(_factorial_sequence)
    
    # have the terms up to n! already been computed?
    if n < FACT_COUNT:
        return
    
    # compute numbers iteratively from existing sequence
    product = _factorial_sequence[-1]
    for i in range(FACT_COUNT, n + 1):
        product *= i
        _factorial_sequence.append(product)
    

def _compute_fibonacci(n):
    """Precomputes and stores the Fibonacci numbers up to F(n)."""
    
    FIB_COUNT = len(_fibonacci_sequence)

    # have the numbers up to F(n) already been computed?
    if n < FIB_COUNT:
        return

    # compute numbers iteratively from existing sequence
    f0 = _fibonacci_sequence[-2]
    f1 = _fibonacci_sequence[-1]
    for i in range(FIB_COUNT, n + 1):
        temp = f1
        f1 += f0
        f0 = temp
        _fibonacci_sequence.append(f1)


def _compute_primes(n):
    """Precomputes and stores at least the first n prime numbers."""
    
    PRIME_COUNT = len(_prime_sequence)

    # have the first n primes already been computed?
    if n < PRIME_COUNT:
        return

    # TODO: implement incremental sieve?

    # based on analysis of OEIS data set A006880 and empirical time tests
    ESTIMATE = 100 if n <= 25 else int(n * math.log(n) * 1.05 + n * 0.87)
    INCREMENT = n / math.log(n)

    # compute primes up to ESTIMATE, then step forward until n are found
    i = ESTIMATE
    while len(_prime_sequence) < n:
        _compute_primes_up_to(i)
        i += INCREMENT


def _compute_primes_up_to(n):
    """Precomputes and stores the prime numbers up to n."""

    # have the numbers up to n already been computed?
    PRIME_MAX = _prime_sequence[-1]
    if PRIME_MAX >= n:
        return

    # prepare sieve of Eratosthenes for numbers PRIME_MAX + 1 to n
    SIEVE_SIZE = n - PRIME_MAX
    sieve = [True] * SIEVE_SIZE

    # sift out composite numbers using previously computed primes
    PRIME_COUNT = len(_prime_sequence)
    for i in range(PRIME_COUNT):
        rho = _prime_sequence[i]
        for j in range(rho*rho, SIEVE_SIZE + PRIME_MAX + 1, rho):
            if j < PRIME_MAX + 1:
                continue
            sieve[j - PRIME_MAX - 1] = False

    # sift out remaining composite numbers with newly found primes
    for i in range(SIEVE_SIZE):
        if sieve[i]:
            rho = i + PRIME_MAX + 1
            _prime_sequence.append(rho)
            for j in range(rho*rho - PRIME_MAX - 1, SIEVE_SIZE, rho):
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
        
        # if result of running function on args has been cached, return it
        if args in self.results:
            return self.results[args]
        
        # evaluate function with args and store the result
        result = self.function(*args)
        self.results[args] = result
        return result

# PUBLIC ENUMS ################################################################

class Day:
    """Enum representing days of the week."""
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class Month:
    """Enum representing months of the year."""
    JANUARY = 0
    FEBRUARY = 1
    MARCH = 2
    APRIL = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUGUST = 7
    SEPTEMBER = 8
    OCTOBER = 9
    NOVEMBER = 10
    DECEMBER = 11

# PUBLIC FUNCTIONS ############################################################

def alphabet_index_upper(letter):
    """Returns the alphabetic index of the uppercase character letter."""
    return ord(letter) - ord('A') + 1


def arithmetic_product(a, n, d = 1):
    """Returns the product of the arithmetic sequence with first term a, number
    of terms n, and difference between terms d."""
    product = 1
    for i in range(a, a + n * d, d):
        product *= i
    return product


def arithmetic_series(a, n, d = 1):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def binary_search(sorted_list, item, lo = 0, hi = None):
    """Returns the index position of item in the sorted list sorted_list or
    None if item is not found in sorted_list."""
    
    # if hi has not been initialized, set it to end of sorted_list
    if hi is None:
        hi = len(sorted_list)
    
    # base case: no elements left to search
    if lo >= hi:
        return None
    
    # check the middle element in list, then recurse if necessary
    mid = (lo + hi) // 2
    if item < sorted_list[mid]:
        # item must be in first half of list or not at all
        return binary_search(sorted_list, item, lo, mid)
    elif item > sorted_list[mid]:
        # item must be in second half of list or not at all
        return binary_search(sorted_list, item, mid + 1, hi)
    else:
        # item found at middle position in list
        return mid


def collatz_step(n):
    """Returns the next number in the Collatz sequence following n."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def combination_sums(total, addends):
    """Returns the number of unique combinations of terms in addends that sum
    to total."""
    
    # initialize the combination array
    combos = [0] * (total + 1)
    combos[0] = 1
    
    # dynamically compute combinations by summing combination dependencies
    for i in range(len(addends)):
        for j in range(addends[i], total + 1):
            combos[j] += combos[j - addends[i]]
    
    return combos[total]


def count_digits(n):
    """Returns the number of digits of the natural number n."""
    
    # divide out and count each digit of n
    digit_count = 0
    while n != 0:
        digit_count += 1
        n //= 10
    
    # return 1 for 0, which has one "digit"
    return 1 if digit_count == 0 else digit_count


def count_divisors(n):
    """Returns the number of divisors of the natural number n."""
    
    # compute product of one more than the powers of its prime factors
    divisor_count = 1
    FACTORIZATION = prime_factorization(n)
    for factor in FACTORIZATION:
        divisor_count *= factor[1] + 1

    return divisor_count


def digit_power_sum(n, exponent):
    """Returns the sum of each digit of n raised to the exponent power."""
    power_sum = 0
    while n != 0:
        n, digit = divmod(n, 10)
        power_sum += digit**exponent
    return power_sum


def factorial(n):
    """Returns the value of n! = n * (n - 1) * ... * 1."""
    _compute_factorial(n)
    return _factorial_sequence[n]


def fibonacci(n):
    """Returns the nth Fibonacci number, with F(0) = F(1) = 1."""
    _compute_fibonacci(n)
    return _fibonacci_sequence[n]


def gcd(m, n):
    """Returns the greatest common divisor of the natural numbers m and n."""
    while n != 0:
        temp = n
        n = m % n
        m = temp
    return m


def is_leap_year(year):
    """Determines if year (given in years A.D.) is a leap year."""
    if year % 100 != 0:
        # year is not a century; it is a leap year if divisible by 4
        return year % 4 == 0
    else:
        # year is a century; it is a leap year only if divisible by 400
        return year % 400 == 0


def is_palindrome(n):
    """Determines if the natural number n is a palindrome."""
    
    N_STR = str(n)
    
    # compare chars iteratively from beginning and end of string
    i = 0
    j = len(N_STR) - 1
    while (i < j):
        if N_STR[i] != N_STR[j]:
            return False
        i += 1
        j -= 1
    return True


def is_permutation(iter_a, iter_b):
    """Determines if the two iterables iter_a and iter_b are permutations of
    each other.
    
    Adapted from: http://stackoverflow.com/questions/396421/"""
    
    # convert iterables to lists if necessary
    if not hasattr(iter_a, 'count'):
        iter_a = list(iter_a)
    if not hasattr(iter_b, 'count'):
        iter_b = list(iter_b)
    
    # if lengths of a and b are different, they cannot be permutations
    len_a = len(iter_a)
    if len_a != len(iter_b):
        return False
    
    # Threshold length at which Namin's method will be used
    NAMIN_THRESHOLD = 1000000
    
    if len_a < NAMIN_THRESHOLD:
        # check if a and b are equal when sorted
        return sorted(iter_a) == sorted(iter_b)
    else:
        # check if a and b contain the same numbers of the same items
        return all(iter_a.count(item) == iter_b.count(item) for item in iter_a)


def is_prime(n):
    """Determines if the natural number n is prime."""
    
    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3:
        return n > 1

    # check if multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    MAX_FACTOR = int(math.sqrt(n))
    for i in range(5, MAX_FACTOR + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def lcm(m, n):
    """Returns the least common multiple of the natural numbers m and n."""
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


def make_spiral(layers, matrix = None, depth = 0):
    """Returns a spiral with the given number of layers formed by starting with
    1 in the center and moving to the right in a clockwise direction."""
    
    # compute the dimension of one side of the spiral
    SIDE = layers * 2 - 1
    
    # initialize the matrix that will hold the spiral
    if matrix is None:
        matrix = [[1 for i in range(SIDE)] for j in range(SIDE)]
    
    # base case: a spiral with one layer will contain the number 1
    if layers < 2:
        return matrix
    
    SIDE_MIN_1 = SIDE - 1
    value = SIDE * SIDE
    
    # fill the top row of the spiral
    for i in range(SIDE_MIN_1):
        matrix[depth][-1 - depth - i] = value
        value -= 1
    
    # fill the left column of the spiral
    for i in range(SIDE_MIN_1):
        matrix[depth + i][depth] = value
        value -= 1
    
    # fill the bottom row of the spiral
    for i in range(SIDE_MIN_1):
        matrix[-1 - depth][depth + i] = value
        value -= 1
    
    # fill the right column of the spiral
    for i in range(SIDE_MIN_1):
        matrix[-1 - depth - i][-1 - depth] = value
        value -= 1
    
    # recurse to fill the inside of the spiral
    return make_spiral(layers - 1, matrix, depth + 1)


def max_triangle_path(triangle):
    """Returns the maximal sum of numbers from top to bottom in triangle."""
    
    NUM_ROWS = len(triangle)

    # add maximum adjacent values from row above to each row
    for i in range(1, NUM_ROWS):
        for j in range(i + 1):
            if j != 0 and j != i:
                # two adjacent elements above; add maximal
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            elif j == 0:
                # no adjacent element to left above; add right
                triangle[i][j] += triangle[i - 1][j]
            else:
                # no adjacent element to right above; add left
                triangle[i][j] += triangle[i - 1][j - 1]

    # return maximal sum accumulated in last row of triangle
    return max(triangle[-1])


def numbers_from_file(input_file):
    """Returns a list of rows of integer numbers read from input_file."""
    
    with open(input_file) as file:
        # add each line from the input file as a row to the MATRIX
        matrix = []
        for line in file:
            # add each token from the current line to the row vector
            row = [int(num) for num in line[:-1].split()]
            matrix.append(row)
    
        return matrix


def pandigital_string(n):
    """Returns a string with each of the digits from 1 to n in order."""
    return ''.join('%d' % digit for digit in range(1, n + 1))


def permutate(n, k):
    """Returns the number of permutations of k objects from a group of n."""
    
    # if faster, compute n! and (n - k)! and return their quotient
    FACT_COUNT = len(_factorial_sequence)
    if n - FACT_COUNT <= k:
        return factorial(n) // factorial(n - k)
    
    # compute the product (n - k + 1) * (n - k + 2) * ... * n
    return arithmetic_product(n - k + 1, k)


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
    PRIME_COUNT = len(_prime_sequence)
    while i < PRIME_COUNT and _prime_sequence[i] <= n:
        i += 1

    return _prime_sequence[:i]


def run_thread(function, stack_size = 128 * 10**6, recursion_limit = 2**20):
    """Runs function in a new thread with stack size stack_size and maximum
    recursion depth recursion_limit."""
    
    # set stack size and maximum recursion depth of the thread
    threading.stack_size(stack_size)
    sys.setrecursionlimit(recursion_limit)
    
    # run the thread
    thread = threading.Thread(target = function)
    thread.start()


def sum_digits(n):
    """Returns the sum of the decimal digits of the natural number n."""
    digit_sum = 0
    while n != 0:
        n, digit = divmod(n, 10)
        digit_sum += digit
    return digit_sum


def sum_divisors(n):
    """Returns the sum of the divisors of the natural number n."""
    
    FACTORIZATION = prime_factorization(n)
    
    # compute sum of divisors of n as the product of (p^(a+1) - 1)/(p - 1) for
    # each prime factor p^a of n
    # Source: http://mathschallenge.net/?section=faq&ref=number/sum_of_divisors
    product = 1
    for factor in FACTORIZATION:
        product *= (factor[0]**(factor[1] + 1) - 1) // (factor[0] - 1)
    return product


def sum_of_squares(n):
    """Returns the sum of the squares of the first n natural numbers."""
    return (2 * n**3 + 3 * n*n + n) // 6


def sum_proper_divisors(n):
    """Returns the sum of the proper divisors of the natural number n."""
    return sum_divisors(n) - n


def triangle(n):
    """Returns the nth triangle number, or the sum of the natural numbers up to
    and including n."""
    return n * (n + 1) // 2
