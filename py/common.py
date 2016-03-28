"""common.py

Common utility functions and classes for various Project Euler problems.

Author: Curtis Belmonte
"""

import collections
import functools
import heapq
import itertools
import math
import sys
import threading

# PRIVATE VARIABLES ###########################################################

# Currently computed factorial terms (in sorted order)
_factorial_sequence = [1, 1]

# Currently computed terms of the Fibonacci sequence (in sorted order)
_fibonacci_sequence = [1, 1]

# Currently computed prime number terms (in sorted order)
_prime_sequence = [2]

# PRIVATE FUNCTIONS ###########################################################

def _compute_factorial(n):
    """Precomputes and stores the factorial terms up to n!."""
    
    fact_count = len(_factorial_sequence)
    
    # have the terms up to n! already been computed?
    if n < fact_count:
        return
    
    # compute numbers iteratively from existing sequence
    product = _factorial_sequence[-1]
    for i in range(fact_count, n + 1):
        product *= i
        _factorial_sequence.append(product)
    

def _compute_fibonacci(n):
    """Precomputes and stores the Fibonacci numbers up to F(n)."""
    
    fib_count = len(_fibonacci_sequence)

    # have the numbers up to F(n) already been computed?
    if n < fib_count:
        return

    # compute numbers iteratively from existing sequence
    f0 = _fibonacci_sequence[-2]
    f1 = _fibonacci_sequence[-1]
    for i in range(fib_count, n + 1):
        f0, f1 = f1, f0 + f1
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
    increment = int(round(n / math.log(n)))

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
        rho_start = next_multiple(rho, prime_max + 1)
        for j in range(rho_start, n + 1, rho):
            sieve[j - prime_max - 1] = False

    # sift out remaining composite numbers with newly found primes
    for i in range(sieve_size):
        if sieve[i]:
            rho = i + prime_max + 1
            _prime_sequence.append(rho)
            for j in range(rho*rho - prime_max - 1, sieve_size, rho):
                sieve[j] = False

# PUBLIC CONSTANTS ############################################################

# Float representation of positive infinity
INFINITY = float('inf')

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
    
# PUBLIC CLASSES ##############################################################

@functools.total_ordering
class Card(object):
    """Class representing a standard playing card."""
    
    class Face:
        """Enum representing playing card face values."""
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10
        JACK = 11
        QUEEN = 12
        KING = 13
        ACE = 14
    
    class Suit:
        """Enum representing playing card suits."""
        DIAMONDS = 0
        HEARTS = 1
        CLUBS = 2
        SPADES = 3
    
    # dict mapping strings to face values
    _face_map = {
        '2': Face.TWO,
        '3': Face.THREE,
        '4': Face.FOUR,
        '5': Face.FIVE,
        '6': Face.SIX,
        '7': Face.SEVEN,
        '8': Face.EIGHT,
        '9': Face.NINE,
        '10': Face.TEN,
        'T': Face.TEN,
        'J': Face.JACK,
        'Q': Face.QUEEN,
        'K': Face.KING,
        'A': Face.ACE,
    }
    
    # dict mapping strings to suits
    _suit_map = {
        'D': Suit.DIAMONDS,
        'H': Suit.HEARTS,
        'C': Suit.CLUBS,
        'S': Suit.SPADES,
    }
    
    @staticmethod
    def _str_to_face(s):
        """Converts a string to a face value."""
        if s in Card._face_map:
            return Card._face_map[s]
        else:
            raise ValueError('cannot convert %s to face' % s)
    
    @staticmethod
    def _str_to_suit(s):
        """Converts a string to a suit."""
        if s in Card._suit_map:
            return Card._suit_map[s]
        else:
            raise ValueError('cannot convert %s to suit' % s)
    
    def __init__(self, str_rep):
        self._str_rep = ''.join(str_rep.split()).upper()
        self.face = Card._str_to_face(self._str_rep[:-1])
        self.suit = Card._str_to_suit(self._str_rep[-1])
        
    def __str__(self):
        return self._str_rep
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.face == other.face and self.suit == other.suit

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if self.face < other.face:
            return True
        elif self.face > other.face:
            return False
        else:
            return self.suit < other.suit


class Graph(object):
    """Class representing a directed graph with weighted edges."""

    def __init__(self):
        self._adj = {}
        self._node_count = 0
        self._edge_count = 0

    def num_nodes(self):
        """Returns the number of vertices in the graph."""
        return self._node_count

    def num_edges(self):
        """Returns the number of edges in the graph."""
        return self._edge_count

    def nodes(self):
        """Returns an iterable of the unique vertices in the graph."""
        return self._adj.keys()

    def add_node(self, label):
        """Adds a node with a given label to the graph."""

        if label in self._adj:
            raise ValueError('Node ' + str(label) + ' already in graph')

        self._adj[label] = {}
        self._node_count += 1

    def has_node(self, label):
        """Determines if the graph contains a vertex with the given label."""
        return label in self._adj

    def _assert_node(self, label):
        if label not in self._adj:
            raise ValueError('No node ' + str(label) + ' in graph')

    def add_edge(self, source, dest, weight=1):
        """Adds edge (source, dest) with specified weight to the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest in self._adj[source]:
            raise ValueError(
                'Edge ({}, {}) already in graph'.format(source, dest)
            )

        self._adj[source][dest] = weight
        self._edge_count += 1

    def has_edge(self, source, dest):
        """Determines if the graph contains an edge from source to dest."""

        self._assert_node(source)
        self._assert_node(dest)

        return dest in self._adj[source]

    def neighbors(self, label):
        """Returns an iterable of the vertices adjacent to the vertex with
        specified label in the graph."""

        self._assert_node(label)
        
        return self._adj[label].keys()

    def edge_weight(self, source, dest):
        """Returns the weight of edge (source, dest) in the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest not in self._adj[source]:
            raise ValueError('No such edge ({}, {})'.format(source, dest))

        return self._adj[source][dest]


class MinPQ(object):
    """Class representing a minimum priority queue that supports update-key.

    Adapted from: https://docs.python.org/3/library/heapq.html#priority-queue-
    implementation-notes"""

    def __init__(self):
        self._heap = []
        self._entry_map = {}
        self._counter = itertools.count()

    def __len__(self):
        return len(self._entry_map)

    def is_empty(self):
        """Determines if the priority queue is empty."""
        return len(self._entry_map) == 0

    def put(self, value, priority=0):
        """Inserts a value with priority into the queue, or updates the value's
        priority if it is already contained in the priority queue."""

        if value in self._entry_map:
            self.delete(value)
        
        entry = [priority, next(self._counter), value]
        self._entry_map[value] = entry
        heapq.heappush(self._heap, entry)

    def delete(self, value):
        """Removes the given value from the priority queue."""
        entry = self._entry_map.pop(value)
        entry[-1] = None

    def pop_min(self):
        """Deletes and returns the minimum element in the priority queue."""
        while self._heap:
            value = heapq.heappop(self._heap)[-1]
            if value is not None:
                del self._entry_map[value]
                return value

# PUBLIC FUNCTIONS ############################################################

def alpha_char_lower(index):
    """Returns the letter of the alphabet corresponding to index."""
    return chr(index + ord('a') - 1)


def alpha_index_upper(letter):
    """Returns the alphabetic index of the uppercase character letter."""
    return ord(letter) - ord('A') + 1


def argmax(values):
    """Returns the first index of the maximum value in values."""
    max_index = 0
    max_value = values[0]
    for i, value in enumerate(values):
        if value > min_value:
            max_index = i
            max_value = value
    return min_index


def argmin(values):
    """Returns the first index of the minimum value in values."""
    min_index = 0
    min_value = values[0]
    for i, value in enumerate(values):
        if value < min_value:
            min_index = i
            min_value = value
    return min_index


def arithmetic_product(a, n, d=1):
    """Returns the product of the arithmetic sequence with first term a, number
    of terms n, and difference between terms d."""
    product = 1
    for i in range(a, a + n * d, d):
        product *= i
    return product


def arithmetic_series(a, n, d=1):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def binary_search(sorted_list, item, lo=0, hi=None):
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


def choose(n, k):
    """Returns the number of ways to choose k objects from a group of n."""
    return permute(n, k) // factorial(k)


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


def concat_digits(digits, base=10):
    """Return the integer that results from concatenating digits in order."""
    return int(''.join([str(d) for d in digits]), base)


def concat_numbers(n, m):
    """Returns the number that results from concatenating the natural numbers
    n and m, in that order."""

    return int(str(n) + str(m))


def count_digits(n):
    """Returns the number of digits of the natural number n."""
    return len(str(n))


def count_divisors(n):
    """Returns the number of divisors of the natural number n."""
    
    # compute product of one more than the powers of its prime factors
    divisor_count = 1
    factorization = prime_factorization(n)
    for __, power in factorization:
        divisor_count *= power + 1

    return divisor_count


def count_prime_factors(n, primes=None):
    """Returns the number of distinct prime factors of the natural number n,
    using the given precomputed list of primes."""
    
    # generate list of primes up to n if none given
    if primes is None:
        primes = primes_up_to(n)
    
    # check if n is prime to avoid worst-case performance
    if binary_search(primes, n) is not None:
        factor_count = 1
    else:
        factor_count = 0
        for prime in primes:
            # have all prime factors of n been found?
            if n == 1:
                break
            
            # if prime divides n, increment count and divide it out of n
            if n % prime == 0:
                factor_count += 1
                while n % prime == 0:
                    n /= prime
        
    return factor_count


def digit_counts(n):
    """Returns a list with the count of each decimal digit in the natural
    number n."""

    counts = [0] * 10
    while n != 0:
        n, digit = divmod(n, 10)
        counts[digit] += 1

    return counts


def digit_function_sum(n, function):
    """Returns the sum of the results of applying function to each of the
    digits of the natural number n."""

    total = 0
    while n != 0:
        n, digit = divmod(n, 10)
        total += function(digit)

    return total


def digit_permutations(n):
    """Returns all of the digit permutations of the natural number n,
    excluding permutations with leading zeros."""

    perms = []
    for perm_tuple in itertools.permutations(str(n)):
        if perm_tuple[0] != '0':
            perms.append(int(''.join(perm_tuple)))

    return perms


def digit_rotations(n):
    """Returns all digit rotations of the natural number n."""

    n_str = str(n)
    rotations = []
    for i in range(len(n_str)):
        rotations.append(int(n_str[i:] + n_str[:i]))

    return rotations


def digit_truncations_left(n):
    """Returns the left-to-right digit truncations of the natural number n."""

    truncations = []
    
    # prepend the digits of n from right to left to truncated
    truncated = 0
    factor_10 = 1
    while n != 0:
        n, digit = divmod(n, 10)
        truncated += digit * factor_10
        truncations.append(truncated)
        factor_10 *= 10
    
    return truncations


def digit_truncations_right(n):
    """Returns the right-to-left digit truncations of the natural number n."""
    
    truncations = []
    
    # remove each rightmost digit from n
    while n != 0:
        truncations.append(n)
        n //= 10
    
    return truncations


def dijkstra(graph, source):
    """Returns the result of Djikstra's shortest path algorithm on a directed
    graph from a given source vertex."""

    distance = {source: 0}
    previous = {}

    pq = MinPQ()
    for node in graph.nodes():
        if node != source:
            distance[node] = INFINITY
            previous[node] = None

        pq.put(node, distance[node])

    while not pq.is_empty():
        node = pq.pop_min()
        for neighbor in graph.neighbors(node):
            path_cost = distance[node] + graph.edge_weight(node, neighbor)
            if path_cost < distance[neighbor]:
                distance[neighbor] = path_cost
                previous[neighbor] = node
                pq.put(neighbor, path_cost)

    return distance, previous


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
        m, n = n, m % n
    return m


def get_digit(n, digit):
    """Returns the given decimal digit of the natural number n."""
    return int(str(n)[digit - 1])


def int_log(x, base=math.e):
    """Returns the rounded integer logarithm of x for the given base."""
    return int(round(math.log(x, base)))


def int_sqrt(x):
    """Returns the rounded integer square root of the number x."""
    return int(round(math.sqrt(x)))


def int_to_base(n, base, numerals='0123456789abcdefghijklmnopqrstuvwxyz'):
    """Returns the string representation of the natural number n in the given
    base using the given set of numerals.
    
    Adapted from: http://stackoverflow.com/questions/2267362/"""
    
    # base case: 0 is represented as numerals[0] in any base
    if n == 0:
        return numerals[0]
    
    # compute the low-order digit and recurse to compute higher order digits
    div, mod = divmod(n, base)
    return int_to_base(div, base, numerals).lstrip(numerals[0]) + numerals[mod]


def is_hexagon_number(n):
    """Determines if the natural number n is a hexagonal number."""
    radical_sum = 1 + (8 * n)
    return is_square(radical_sum) and int_sqrt(radical_sum) % 4 == 3


def is_int(x):
    """Determines if the floating point number x has an integer value."""
    return x - int(x) == 0


def is_leap_year(year):
    """Determines if year (given in years A.D.) is a leap year."""
    if year % 100 != 0:
        # year is not a century; it is a leap year if divisible by 4
        return year % 4 == 0
    else:
        # year is a century; it is a leap year only if divisible by 400
        return year % 400 == 0


def is_palindrome(n, base=10):
    """Determines if the natural number n is a palindrome in the given base."""
    
    # create a copy of n and number to hold its reversed value
    n_copy = n
    reverse_n = 0
    
    # append each of the digits of n to reverse_n in reverse order
    while n_copy != 0:
        n_copy, digit = divmod(n_copy, base)
        reverse_n = (reverse_n * base) + digit
    
    # compare the original n to its reversed version
    return n == reverse_n


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
        for item in iter_a:
            if iter_a.count(item) != iter_b.count(item):
                return False
        return True


def is_pentagon_number(n):
    """Determines if the natural number n is a pentagonal number."""
    radical_sum = 1 + (24 * n)
    return is_square(radical_sum) and int_sqrt(radical_sum) % 6 == 5


def is_power(n, p):
    """Determines if the natural number n is a perfect power with exponent p.
    
    Specifically, returns True iff n = m**p for some natural number m."""

    root_n = n**(1 / p)
    root_pow = (int(round(root_n)))**p
    return root_pow == n


def is_prime(n):
    """Determines if the natural number n is prime."""
    
    # simple test for small n: 2 and 3 are prime, but 1 is not
    if n <= 3:
        return n > 1

    # check if multiple of 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # search for subsequent prime factors around multiples of 6
    max_factor = int(math.sqrt(n))
    for i in range(5, max_factor + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_square(n):
    """Determines if the natural number n is a perfect square."""
    return is_power(n, 2)


def lcm(m, n):
    """Returns the least common multiple of the natural numbers m and n."""
    return m * n // gcd(m, n)


def lcm_all(nums):
    """Returns the least common multiple of all natural numbers in nums."""
    
    max_powers = {}
    for num in nums:
        # compute powers of unique prime factors of the current number
        factorization = prime_factorization(num)
        for factor, power in factorization:
            if (factor in max_powers and power > max_powers[factor]
                or factor not in max_powers):
                max_powers[factor] = power
        
    # return the product of prime factors raised to their highest powers
    product = 1
    for factor in max_powers:
        product *= factor**max_powers[factor]
    return product


def loop_indices(depth, function, start, stop=None, disjoint=False):
    """Simulates a nested index loop with a specified number of levels.

    The step size is 1 for each index, and the range is [start, stop).

    depth      the number of loop levels to simulate
    function   a function to perform some operation given a list of indices
    start      the min value (inclusive) for each index
    stop       the max value (exclusive) for each index, or [0, start) if None
    disjoint   if True, loop indices will be disjoint (in sorted order)
    """

    # set range to 0:start if stop not specified
    if stop is None:
        start, stop = 0, start

    # don't run function if loops would not execute
    if start >= stop or disjoint and start + depth - 1 >= stop:
        return

    # set initial index values
    indices = []
    for i in range(depth):
        init_index = start + i if disjoint else start
        indices.append(init_index)

    while indices[0] < stop:
        # execute the function for the given set of indices
        function(indices)

        # update all index values
        indices[-1] += 1
        while indices[-1] >= stop:
            # search for deepest index that can be incremented
            i = depth - 1
            while i > 0 and indices[i] >= stop - 1:
                i -= 1

            # if outermost index reaches stop, then return
            if indices[0] >= stop:
                return

            # set new start values for deeper indices
            indices[i] += 1
            for j in range(i + 1, depth):
                indices[j] = indices[j - 1] + 1 if disjoint else start


def make_palindrome(n, base, odd_length=False):
    """Returns a palindrome in the given base formed from the natural number n.
    
    If the odd_length flag is set to True, the generated palindrome will have
    an odd number of digits when written in the given base; otherwise, it will
    have an even number of digits.
    
    Adapted from: https://projecteuler.net/overview=036"""
    
    # set beginning of palindrome to be the digits of n
    palindrome = n
    
    # remove final digit of n if palindrome should be odd in length
    if odd_length:
        n //= base
    
    # append each digit of n to palindrome in reverse order
    while n != 0:
        n, digit = divmod(n, base)
        palindrome = (palindrome * base) + digit
    
    return palindrome


def make_spiral(layers, matrix=None, depth=0):
    """Returns a spiral with the given number of layers formed by starting with
    1 in the center and moving to the right in a clockwise direction."""
    
    # compute the dimension of one side of the spiral
    side = layers * 2 - 1
    
    # initialize the matrix that will hold the spiral
    if matrix is None:
        matrix = [[1 for i in range(side)] for j in range(side)]
    
    # base case: a spiral with one layer will contain the number 1
    if layers < 2:
        return matrix
    
    side_min_1 = side - 1
    value = side * side
    
    # fill the top row of the spiral
    for i in range(side_min_1):
        matrix[depth][-1 - depth - i] = value
        value -= 1
    
    # fill the left column of the spiral
    for i in range(side_min_1):
        matrix[depth + i][depth] = value
        value -= 1
    
    # fill the bottom row of the spiral
    for i in range(side_min_1):
        matrix[-1 - depth][depth + i] = value
        value -= 1
    
    # fill the right column of the spiral
    for i in range(side_min_1):
        matrix[-1 - depth - i][-1 - depth] = value
        value -= 1
    
    # recurse to fill the inside of the spiral
    return make_spiral(layers - 1, matrix, depth + 1)


def max_triangle_path(triangle):
    """Returns the maximal sum of numbers from top to bottom in triangle."""
    
    num_rows = len(triangle)

    # add maximum adjacent values from row above to each row
    for i in range(1, num_rows):
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


def mod_multiply(n, m, mod):
    """Returns the the product of natural numbers n and m modulo mod."""
    return ((n % mod) * (m % mod)) % mod


def next_multiple(n, min_val):
    """Returns the next multiple of the natural number n >= min_val."""
    return min_val + ((n - (min_val % n)) % n)


def numbers_from_file(input_file, sep=' '):
    """Returns a list of rows of integer numbers read from input_file."""
    
    with open(input_file) as f:
        # add each line from the input file as a row to the MATRIX
        matrix = []
        for line in f:
            # add each token from the current line to the row vector
            row = [int(num) for num in line.rstrip().split(sep)]
            matrix.append(row)
    
        return matrix


def pandigital_string(first=0, last=9):
    """Returns a string with each of the digits from first to last in order."""
    return ''.join('%d' % digit for digit in range(first, last + 1))


def pentagon_number(n):
    """Returns the nth pentagonal number."""
    return n * (3 * n - 1) // 2


def permute(n, k):
    """Returns the number of permutations of k objects from a group of n."""
    
    # if faster, compute n! and (n - k)! and return their quotient
    fact_count = len(_factorial_sequence)
    if n - fact_count <= k:
        return factorial(n) // factorial(n - k)
    
    # compute the product (n - k + 1) * (n - k + 2) * ... * n
    return arithmetic_product(n - k + 1, k)


def prime_factorization(n):
    """Computes the prime factorization of the natural number n.
    
    Returns a list of base-exponent pairs containing each prime factor and
    its power in the prime factorization of n."""

    i = 2
    factorization = []
    while i <= int(math.sqrt(n)):
        # compute power of i in factorization
        factor = [i, 0]
        div, mod = divmod(n, i)
        while mod == 0:
            n = div
            factor[1] += 1
            div, mod = divmod(n, i)

        # add factor to factorization if necessary
        if factor[1] > 0:
            factorization.append(factor)
            
        i += 1

    # no more prime factors above sqrt(n)
    if n > 1:
        factorization.append([n, 1])

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

    # return whole sequence if all primes <= n
    if _prime_sequence[-1] <= n:
        return _prime_sequence[:]
    
    # find the index of the last prime <= n
    i = 0
    while _prime_sequence[i] <= n:
        i += 1

    return _prime_sequence[:i]


def run_thread(function, stack_size=128*(10**6), recursion_limit=2**20):
    """Runs function in a new thread with stack size stack_size and maximum
    recursion depth recursion_limit."""
    
    # set stack size and maximum recursion depth of the thread
    threading.stack_size(stack_size)
    sys.setrecursionlimit(recursion_limit)
    
    # run the thread
    thread = threading.Thread(target=function)
    thread.start()
    thread.join()


def sort_by(values, keys):
    """Returns a copy of values sorted by their corresponding keys.

    Adapted from: http://stackoverflow.com/a/6618543"""

    first = lambda vals: vals[0]
    return [value for (key, value) in sorted(zip(keys, values), key=first)]


def sqrt_expansion(n, precision):
    """Returns the square root of the natural number n to arbitrary precision.

    Result is a string with precision digits following the decimal point."""

    # break n into two-digit chunks
    n_digits = []
    while n > 0:
        n, mod = divmod(n, 100)
        n_digits.append(mod)

    expansion = []
    remainder = 0
    root_part = 0
    f = lambda x: x*(20*root_part + x)

    # compute digits before decimal point
    for carry in n_digits:
        c = remainder*100 + carry

        x = 1
        y = f(x)
        while y <= c:
            x += 1
            y = f(x)

        x -= 1
        y = f(x)

        remainder = c - y
        root_part = root_part*10 + x
        expansion.append(str(x))

    expansion.append('.')

    # compute digits after decimal point
    for __ in range(precision):
        c = remainder*100

        x = 1
        y = f(x)
        while y <= c:
            x += 1
            y = f(x)

        x -= 1
        y = f(x)

        remainder = c - y
        root_part = root_part*10 + x
        expansion.append(str(x))

    return ''.join(expansion)


def strings_from_file(input_file, sep=','):
    """Returns a list of sep-separated strings read from input_file."""
    with open(input_file) as f:
        return [string.strip('"\'') for string in f.read().split(sep)]


def sum_digits(n):
    """Returns the sum of the decimal digits of the natural number n."""
    digit_sum = 0
    while n != 0:
        n, digit = divmod(n, 10)
        digit_sum += digit
    return digit_sum


def sum_keep_digits(m, n, d=None):
    """Returns the last d digits of the sum of m and n. If d is None, returns
    the entire sum."""
    result = m + n
    if d is None:
        return result
    else:
        return result % 10**d


def sum_divisors(n):
    """Returns the sum of the divisors of the natural number n."""
    
    factorization = prime_factorization(n)
    
    # compute sum of divisors of n as the product of (p^(a+1) - 1)/(p - 1) for
    # each prime factor p^a of n
    # Source: http://mathschallenge.net/?section=faq&ref=number/sum_of_divisors
    product = 1
    for factor, power in factorization:
        product *= (factor**(power + 1) - 1) // (factor - 1)
    return product


def sum_of_squares(n):
    """Returns the sum of the squares of the first n natural numbers."""
    return (2 * n**3 + 3 * n*n + n) // 6


def sum_proper_divisors(n):
    """Returns the sum of the proper divisors of the natural number n."""
    return sum_divisors(n) - n


def triangle_number(n):
    """Returns the nth triangle number, or the sum of the natural numbers up to
    and including n."""
    return n * (n + 1) // 2
