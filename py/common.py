#!/usr/bin/env python3

"""common.py

Common utility vars, functions, and classes for various Project Euler problems.

Author: Curtis Belmonte
"""

import copy
import heapq
import itertools
import operator
import math
import random
from collections import defaultdict, deque
from fractions import Fraction
from functools import reduce, total_ordering


# PRIVATE VARIABLES ###########################################################


# Currently computed factorial terms (in sorted order)
_factorial_sequence = [1, 1]

# Currently computed terms of the Fibonacci sequence (in sorted order)
_fibonacci_sequence = [1, 1]

# Currently computed prime number terms (in sorted order)
_prime_sequence = [2]


# PRIVATE FUNCTIONS ###########################################################


def _compute_chain_length(lengths, n, incr, is_valid, invalid_set, terms=None):
    """Recursive helper function for compute_chain_lengths that updates lengths
    with appropriate chain lengths starting from n."""

    if terms is None:
        terms = {}
    
    # if chain is invalid, mark all terms accordingly
    if not is_valid(n) or n in invalid_set or n in lengths:
        for term in terms:
            invalid_set.add(term)

    # if completed chain, set length for all terms in it and invalidate others
    elif n in terms:
        index = terms[n]
        length = len(terms) - index
        for term, i in terms.items():
            if i < index:
                invalid_set.add(term)
            else:
                lengths[term] = length

    # otherwise, continue building the current chain
    else:
        terms[n] = len(terms)
        _compute_chain_length(
            lengths,
            incr(n),
            incr,
            is_valid,
            invalid_set,
            terms)


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
            for j in range(rho**2 - prime_max - 1, sieve_size, rho):
                sieve[j] = False


def _try_assign_zeros(matrix):
    """Returns a list of all unambiguous (row, col) assignments for zero values
    in matrix, such that no row or column is repeated."""

    # convert matrix to bipartite graph, with zeros indicating edges
    edge_matrix = copy.deepcopy(matrix)
    for i, row in enumerate(edge_matrix):
        for j, value in enumerate(row):
            edge_matrix[i][j] = (value == 0)

    return max_bipartite_matching(edge_matrix)


def _try_bipartite_match(edge_matrix, i, col_marked, col_assignments):
    """Attempts to match the given row i to a column in edge_matrix.

    edge_matrix      A boolean matrix indicating edges between rows and columns
    i                The given row to attempt to match with a free column
    col_marked       List of marked, or visited, columns for this row
    col_assignments  Array of current row assignments for each column, if any

    Returns True if row was successfully matched, or False otherwise.
    """

    # try to match row to each column
    for j in range(len(edge_matrix[0])):

        # check if row can be matched with unmarked column
        if edge_matrix[i][j] and not col_marked[j]:
            col_marked[j] = True

            # check if column is unmatched or can be re-matched with new row
            if col_assignments[j] is None or _try_bipartite_match(
                    edge_matrix,
                    col_assignments[j],
                    col_marked,
                    col_assignments):
                col_assignments[j] = i
                return True

    # couldn't match row with any column
    return False


# PUBLIC CONSTANTS ############################################################

# Number of days in a week
DAYS_IN_WEEK = 7

# Number of days in a calendar year
DAYS_IN_YEAR = 365

# Number of days in each month
MONTH_DAY_COUNTS = [
  31, # January
  28, # February (non-leap year)
  31, # March
  30, # April
  31, # May
  30, # June
  31, # July
  31, # August
  30, # September
  31, # October
  30, # November
  31, # December
]

# Number of months in a calendar year
MONTHS_IN_YEAR = 12

# Float representation of positive infinity
INFINITY = float('inf')

# Mapping from natural numbers to their English word equivalents
NUMBER_WORDS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


# PUBLIC DECORATORS ###########################################################


def memoized(func):
    """Decorator that caches the result of calling func with a particular set
    of arguments and returns this result for subsequent calls to function with
    the same arguments.
    """

    memo = {}

    def memo_func(*args):
        if args not in memo:
            memo[args] = func(*args)
        return memo[args]

    return memo_func


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


@total_ordering
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

    # dict mapping strings to suits
    _suit_map = {
        'D': Suit.DIAMONDS,
        'H': Suit.HEARTS,
        'C': Suit.CLUBS,
        'S': Suit.SPADES,
    }

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
        return (isinstance(other, type(self)) and
                self.face == other.face and
                self.suit == other.suit)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.face < other.face:
            return True
        elif self.face > other.face:
            return False
        else:
            return self.suit < other.suit


class GameBoard(object):
    """Class representing a game board with a cyclical sequence of spaces.

    This class supports defining a set of types that are assigned to the spaces
    in the board. It also allows rules to be specified for each space type that
    give some probability of ending a turn on a different space than the one
    which was landed on."""

    class Space(object):
        """Class representing a space on the board, with a type and number."""

        def __init__(self, space_type, number):
            self.type = space_type
            self.number = number

        def __str__(self):
            return '{0}{1}'.format(self.type, self.number)

        def __repr__(self):
            return self.__str__()

        def __eq__(self, other):
            return (isinstance(other, self.__class__) and
                    self.type == other.type and
                    self.number == other.number)

        def __ne__(self, other):
            return not self.__eq__(other)

        def __hash__(self):
            return hash((self.type, self.number))

    def __init__(self, space_type_map, move_rules):
        self._space_list = GameBoard._make_space_list(space_type_map)
        self._move_probs = GameBoard._make_move_probs(
            move_rules,
            self._space_list)

    @staticmethod
    def _make_space_list(space_type_map):
        """Contructs an ordered list of board spaces, from a map of space types
        to their positions on the board."""

        # allocate the list of spaces
        num_spaces = sum(map(len, space_type_map.values()))
        space_list = [None] * num_spaces

        # create spaces and assign them to their board positions
        for space_type, indices in space_type_map.items():
            for i, index in enumerate(indices):
                space_list[index] = GameBoard.Space(space_type, i + 1)

        return space_list

    @staticmethod
    def _make_move_probs(move_rules, space_list):
        """Constructs an ordered list of move probabilities from each space.

        move_rules  Maps space types to the probability of ending up on a
                    different space after landing on them. Each string space
                    type maps to another dict, mapping rules to probabilities.
                    See GameBoard._get_rule_dest for a description of all valid
                    rule types.

        space_list  An ordered list of all spaces on the board.
        """

        move_probs = []
        space_map = inverse_index_map(space_list)

        for position, space in enumerate(space_list):
            # if no rules specified, player always ends on this space
            if space.type not in move_rules:
                move_probs.append({position: 1})
                continue
            
            # convert rules to positions and assign probabilities to them
            space_probs = defaultdict(int)
            rule_probs = move_rules[space.type]
            total_prob = 0
            for rule, prob in rule_probs.items():
                rule_dest = GameBoard._get_rule_dest(
                    rule,
                    position,
                    space_list,
                    space_map)
                space_probs[rule_dest] += prob
                total_prob += prob

            # player ends on this space with remaining probability
            if total_prob < 1:
                space_probs[position] += 1 - total_prob

            move_probs.append(space_probs)

        return move_probs

    @staticmethod
    def _get_rule_dest(rule, position, space_list, space_map):
        """Returns the position that corresponds to a given rule.

        rule        The rule specifying a space that a player could move to.
                    Its type should be one of:
                    1. (str, int): player should move to the specified space
                    2. str: player should move to the next space of this type
                    3. int: player should move forward this many spaces

        position    The player's current position on the board
        
        space_list  An ordered list of all spaces on the board

        space_map   A dict mapping each space to its position on the board
        """

        # check if rule is tuple, indicating a particular space
        if isinstance(rule, tuple):
            return space_map[GameBoard.Space(*rule)]

        num_spaces = len(space_list)

        # check if rule is str, indicating next space of given type
        if isinstance(rule, str):
            position = (position + 1) % num_spaces
            while space_list[position].type != rule:
                position = (position + 1) % num_spaces
            return position

        # check if rule is int, indicating relative movement
        if isinstance(rule, int):
            return (position + rule) % num_spaces

        # received invalid rule type
        raise ValueError('Rule {0} of type {1} is invalid'.format(
            rule,
            type(rule)))

    def move(self, start, spaces):
        """Simulates moving the given number of spaces forward from position
        start and returns the position that the player lands on, after
        probabilistically applying any applicable move rules."""

        # find where player would end before applying move rules
        target = (start + spaces) % len(self._space_list)

        # create lists for each possible end position and its probability
        dests = []
        probs = []
        for dest, prob in self._move_probs[target].items():
            dests.append(dest)
            probs.append(prob)

        # choose end position probabilistically
        return choose_weighted_random(dests, probs)


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
                'Edge ({}, {}) already in graph'.format(source, dest))

        self._adj[source][dest] = weight
        self._edge_count += 1

    def has_edge(self, source, dest):
        """Determines if the graph contains an edge from source to dest."""

        self._assert_node(source)
        self._assert_node(dest)

        return dest in self._adj[source]

    def update_edge(self, source, dest, weight):
        """Updates the weight of edge (source, dest) in the graph."""

        self._assert_node(source)
        self._assert_node(dest)

        if dest not in self._adj[source]:
            raise ValueError(
                'Edge ({}, {}) not in graph'.format(source, dest))

        self._adj[source][dest] = weight

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

    def reverse(self):
        """Returns a copy of the graph with all edge directions reversed."""

        # add all nodes to reverse graph
        rev_graph = Graph()
        for node in self._adj:
            rev_graph.add_node(node)

        # add reverse of all edges
        for node, edges in self._adj.items():
            for neighbor, weight in edges.items():
                rev_graph._adj[neighbor][node] = weight
                rev_graph._edge_count += 1

        return rev_graph

    def postorder(self):
        """Returns a postorder traversal of all nodes in the graph."""

        post = []

        # run DFS from each unvisited node in the graph
        visited = set()
        for node in self._adj:
            if node not in visited:
                self._postorder_dfs(node, set(), visited, post)

        return post

    def _postorder_dfs(self, node, path, visited, post):
        """Helper function for postorder that runs DFS from a given node."""

        path.add(node)
        visited.add(node)

        for neighbor in self._adj[node]:
            # has a cycle if neighbor is an earlier node on path
            if neighbor in path:
                raise RuntimeError('Graph contains a cycle')

            # continue searching from neighbors of node
            if neighbor not in visited:
                self._postorder_dfs(neighbor, path.copy(), visited, post)

        post.append(node)

    def bfs(self, source):
        """Runs breadth-first search from a source node in the graph.

        Returns two dicts that map each node to its distance from source and
        to the previous node along the search path from source to that node."""

        self._assert_node(source)

        distance = {source: 0}
        previous = {}
        visited = {source}

        # queue of nodes to be visited in order
        frontier = deque()
        frontier.append(source)

        # visit each node in FIFO order, adding its neighbors
        while frontier:
            node = frontier.popleft()
            for neighbor in self._adj[node]:
                if neighbor not in visited:
                    distance[neighbor] = distance[node] + 1
                    previous[neighbor] = node
                    visited.add(neighbor)
                    frontier.append(neighbor)

        return distance, previous

    def dijkstra(self, source):
        """Runs Djikstra's shortest path algorithm from a source node.

        Returns two dicts that map each node to its distance from source and
        to the previous node along a shortest path from source to that node."""

        self._assert_node(source)

        distance = {source: 0}
        previous = {}

        # initialize node distances to positive inifnity
        pq = MinPQ()
        for node in self._adj:
            if node != source:
                distance[node] = INFINITY
                previous[node] = None

            pq.put(node, distance[node])

        # visit nodes in priority order along explored paths
        while not pq.is_empty():
            node = pq.pop_min()
            for neighbor in self._adj[node]:
                path_cost = distance[node] + self._adj[node][neighbor]

                # update distance to node when shorter path found
                if path_cost < distance[neighbor]:
                    distance[neighbor] = path_cost
                    previous[neighbor] = node
                    pq.put(neighbor, path_cost)

        return distance, previous


class MinPQ(object):
    """Class representing a minimum priority queue that supports update-key.

    Adapted from: https://docs.python.org/3/library/heapq.html"""

    def __init__(self):
        self._heap = []
        self._entry_map = {}
        self._counter = itertools.count()

    def __len__(self):
        return len(self._entry_map)

    def is_empty(self):
        """Determines if the priority queue is empty."""
        return not self._entry_map

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

        if value not in self._entry_map:
            raise KeyError('Value {0} not present in MinPQ'.format(value))

        entry = self._entry_map.pop(value)
        entry[-1] = None

    def pop_min(self):
        """Deletes and returns the minimum element in the priority queue."""

        if self.is_empty():
            raise KeyError('Cannot pop from an empty MinPQ')

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
        if value > max_value:
            max_index = i
            max_value = value
    return max_index


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
    return reduce(operator.mul, range(a, a + n * d, d), 1)


def arithmetic_series(a, n, d=1):
    """Returns the sum of the arithmetic sequence with first term a, number of
    terms n, and difference between terms d."""
    return n * (2 * a + (n - 1) * d) // 2


def binary_search(sorted_list, item, _lo=0, _hi=None):
    """Returns the index position of item in the sorted list sorted_list or
    None if item is not found in sorted_list."""
    
    # if hi has not been initialized, set it to end of sorted_list
    if _hi is None:
        _hi = len(sorted_list)
    
    # base case: no elements left to search
    if _lo >= _hi:
        return None
    
    # check the middle element in list, then recurse if necessary
    mid = (_lo + _hi) // 2
    if item < sorted_list[mid]:
        # item must be in first half of list or not at all
        return binary_search(sorted_list, item, _lo, mid)
    elif item > sorted_list[mid]:
        # item must be in second half of list or not at all
        return binary_search(sorted_list, item, mid + 1, _hi)
    else:
        # item found at middle position in list
        return mid


def choose(n, k):
    """Returns the number of ways to choose k objects from a group of n."""
    return permute(n, k) // factorial(k)


def choose_weighted_random(values, probs):
    """Returns a value at random from values, weighted by probs.

    Note: The sum of values in probs must equal 1."""

    # generate a random float in [0, 1)
    x = random.random()

    # search for corresponding index in values
    i = 0
    cum_prob = probs[0]
    while x > cum_prob:
        i += 1
        cum_prob += probs[i]

    return values[i]


def collatz_step(n):
    """Returns the next number in the Collatz sequence following n."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def combination_sums(total, terms):
    """Returns the number of unique combinations of terms that sum to total.

    Both total and each term in terms must be a natural number."""

    if total <= 0:
        raise ValueError("Argument 'total' must be a natural number")
    for term in terms:
        if term <= 0:
            raise ValueError("Each term in 'terms' must be a natural number")
    
    # initialize the combination array
    combos = [0] * (total + 1)
    combos[0] = 1
    
    # dynamically compute combinations by summing combination dependencies
    for i, term in enumerate(terms):
        for j in range(term, total + 1):
            combos[j] += combos[j - terms[i]]
    
    return combos[total]


def compute_chain_lengths(lengths, values, incr, is_valid=lambda x: True):
    """Populates lengths with chain lengths starting from each term in values.

    lengths   the dict to be populated, mapping each term to its chain length
    values    an iterable of all valid starting terms for a chain
    incr      for any term n, incr(n) gives the next term in the chain
    is_valid  is_valid(n) returns True iff n is a valid chain member
    """
    
    invalid_set = set()
    for n in values:
        _compute_chain_length(lengths, n, incr, is_valid, invalid_set)


def concat_digits(digit_list, base=10):
    """Returns the integer that results from concatenating digits in order."""
    return int(''.join(map(str, digit_list)), base)


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
    for _, power in factorization:
        divisor_count *= power + 1

    return divisor_count


def count_divisors_up_to(n):
    """Returns a list of divisor counts for integers 0 to n, inclusive."""

    # set counts for 1..n to 1
    divisor_counts = [1] * (n + 1)
    divisor_counts[0] = 0

    # increment counts for multiples of each number up to n
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            divisor_counts[j] += 1

    return divisor_counts


def count_prime_factors(n, prime_nums=None):
    """Returns the number of distinct prime factors of the natural number n,
    using the given precomputed list of primes."""
    
    # generate list of primes up to n if none given
    if prime_nums is None:
        prime_nums = primes_up_to(n)
    
    # check if n is prime to avoid worst-case performance
    if binary_search(prime_nums, n) is not None:
        factor_count = 1
    else:
        factor_count = 0
        for prime_num in prime_nums:
            # have all prime factors of n been found?
            if n == 1:
                break
            
            # if prime divides n, increment count and divide it out of n
            if n % prime_num == 0:
                factor_count += 1
                while n % prime_num == 0:
                    n /= prime_num
        
    return factor_count


def cross_product_3d(p1, p2):
    """Returns the cross product p1 x p2 of 3-dimensional points p1 and p2."""
    
    # compute determinant of cross product matrix
    prod_i = (p1[1] * p2[2]) - (p1[2] * p2[1])
    prod_j = (p1[2] * p2[0]) - (p1[0] * p2[2])
    prod_k = (p1[0] * p2[1]) - (p1[1] * p2[0])

    return prod_i, prod_j, prod_k


def cumulative_partial_sum(nums, limit=INFINITY):
    """Returns a list of cumulative sums of the numbers in nums, keeping the
    sum of only the previous limit elements."""

    sums = []
    total = 0
    terms = deque()
    for i, num in enumerate(nums):
        total += num
        terms.append(num)

        if len(terms) > limit:
            total -= terms.popleft()
        
        sums.append(total)

    return sums


def dice_probability(x, n, s):
    """Returns the probability of rolling a value of x with n s-sided dice."""
    
    outcomes = 0
    for k in range((x - n) // s + 1):
        outcomes += (-1)**k * choose(n, k) * choose(x - s * k - 1, n - 1)
    
    return Fraction(outcomes, s**n)


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
    """Returns all unique digit permutations of the natural number n,
    excluding permutations with leading zeros."""

    perms = set()
    for perm_tuple in itertools.permutations(str(n)):
        if perm_tuple[0] != '0':
            perms.add(int(''.join(perm_tuple)))

    return perms


def digit_rotations(n):
    """Returns all unique digit rotations of the natural number n."""

    n_str = str(n)
    rotations = set()
    for i in range(len(n_str)):
        rotations.add(int(n_str[i:] + n_str[:i]))

    return rotations


def digit_truncations_left(n):
    """Returns all unique left-to-right digit truncations of the natural number
    n."""

    truncations = set()
    
    # prepend the digits of n from right to left to truncated
    truncated = 0
    factor_10 = 1
    while n != 0:
        n, digit = divmod(n, 10)
        truncated += digit * factor_10
        truncations.add(truncated)
        factor_10 *= 10
    
    return truncations


def digit_truncations_right(n):
    """Returns all right-to-left digit truncations of the natural number n."""
    
    truncations = []
    
    # remove each rightmost digit from n
    while n != 0:
        truncations.append(n)
        n //= 10
    
    return truncations


def digits(n, base=10):
    """Returns a list of the digits of the natural number n."""

    digit_list = []

    while n != 0:
        n, digit = divmod(n, base)
        digit_list.append(digit)

    return digit_list[::-1]


def dot_product(u, v):
    """Returns the dot product of vectors u and v."""
    return sum(i * j for i, j in zip(u, v))


def factorial(n):
    """Returns the value of n! = n * (n - 1) * ... * 1."""
    _compute_factorial(n)
    return _factorial_sequence[n]


def fibonacci(n):
    """Returns the nth Fibonacci number, with F(0) = F(1) = 1."""
    _compute_fibonacci(n)
    return _fibonacci_sequence[n]


def flatten_matrix(matrix, keep_indices=False):
    """Returns a list of the elements in matrix in row-major order. If
    keep_indices is set to True, also returns the indices of each element."""

    flat_matrix = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            flat_val = (value, i, j) if keep_indices else value
            flat_matrix.append(flat_val)

    return flat_matrix


def gcd(m, n):
    """Returns the greatest common divisor of the natural numbers m and n."""
    while n != 0:
        m, n = n, m % n
    return m


def get_digit(n, digit):
    """Returns the given decimal digit of the natural number n."""
    return int(str(n)[digit - 1])


def hexagonal(n):
    """Returns the nth hexagonal number."""
    return n * (2 * n - 1)


def int_log(x, base=math.e):
    """Returns the rounded integer logarithm of x for the given base."""
    return int(round(math.log(x, base)))


def int_pow(x, exponent):
    """Returns the rounded integer power of x to the exponent power."""
    return int(round(x**exponent))


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


def ints_from_file(input_file, sep=' '):
    """Returns a list of rows of integer numbers read from input_file."""
    with open(input_file) as f:
        for line in f:
            yield [int(token) for token in line.rstrip().split(sep)]


def inverse_index_map(values, distinct=True):
    """Returns a map from each item in values to its index.

    If distinct is False, then items in values can be repeated, and each will
    be mapped to a list of its indices."""

    inverse_map = {} if distinct else defaultdict(list)

    if distinct:
        for i, value in enumerate(values):
            inverse_map[value] = i
    else:
        for i, value in enumerate(values):
            inverse_map[value].append(i)

    return inverse_map


def is_bouncy(n):
    """Determines if the natural number n is a bouncy number.

    A number is bouncy iff its digits are in neither non-decreasing or
    non-increasing order. That is, they increase and then decrease, or decrease
    and then increase."""

    n_digits = digits(n)
    max_index = len(n_digits) - 1

    # search for first increasing or decreasing consecutive digit pair
    i = 0
    while i < max_index and n_digits[i] == n_digits[i + 1]:
        i += 1

    # if all digit pairs are equal, number is not bouncy
    if i == max_index:
        return False

    # check whether first non-equal pair is increasing or decreasing
    increasing = n_digits[i] < n_digits[i + 1]

    # determine if subsequent pairs are also increasing/decreasing
    i += 1
    while i < max_index:
        # if order is reversed, the number is bouncy
        if (increasing and n_digits[i] > n_digits[i + 1]
                or not increasing and n_digits[i] < n_digits[i + 1]):
            return True
        i += 1

    # number is increasing or decreasing
    return False


def is_coprime_pair(n, m):
    """Determines if the natural numbers n and m are relatively prime."""
    return gcd(n, m) == 1


def is_hexagonal(n):
    """Determines if the natural number n is a hexagonal number."""
    radical_sum = 1 + (8 * n)
    return is_square(radical_sum) and int_sqrt(radical_sum) % 4 == 3


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


def is_permutation(iter_a, iter_b, compare_counts=False):
    """Determines if iterables iter_a, iter_b are permutations of each other.

    If iter_a and iter_b have the same length, then the compare_counts flag
    determines how the two will be compared. If compare_counts is True, this
    function will compare counts of items in the two iterables. Otherwise, this
    function will compare sorted copies of the iterables.
    """
    
    # convert iterables to lists if necessary
    if not hasattr(iter_a, 'count'):
        iter_a = list(iter_a)
    if not hasattr(iter_b, 'count'):
        iter_b = list(iter_b)
    
    # if lengths of a and b are different, they cannot be permutations
    if len(iter_a) != len(iter_b):
        return False
    
    if compare_counts:
        # check if a and b contain the same numbers of the same items
        for item in set(iter_a):
            if iter_a.count(item) != iter_b.count(item):
                return False
        return True
    else:
        # check if a and b are equal when sorted
        return sorted(iter_a) == sorted(iter_b)


def is_pentagonal(n):
    """Determines if the natural number n is a pentagonal number."""
    radical_sum = 1 + (24 * n)
    return is_square(radical_sum) and int_sqrt(radical_sum) % 6 == 5


def is_power(n, p):
    """Determines if the natural number n is a perfect power with exponent p.
    
    Specifically, returns True iff n = m**p for some natural number m."""

    root_n = n**(1 / p)
    lo_power = (int(root_n))**p
    hi_power = (int(math.ceil(root_n)))**p
    return lo_power == n or hi_power == n


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
    sqrt_n = math.sqrt(n)
    lo_power = (int(sqrt_n))**2
    hi_power = (int(math.ceil(sqrt_n)))**2
    return lo_power == n or hi_power == n


def is_triangular(n):
    """Determines if the natural number n is a triangle number."""
    return is_square(8 * n + 1)


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


def make_palindrome(n, base=10, odd_length=False):
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


def make_spiral(layers, _matrix=None, _depth=0):
    """Returns a spiral with the given number of layers formed by starting with
    1 in the center and moving to the right in a clockwise direction."""
    
    # compute the dimension of one side of the spiral
    side = layers * 2 - 1
    
    # initialize the matrix that will hold the spiral
    if _matrix is None:
        _matrix = [[1 for _ in range(side)] for _ in range(side)]
    
    # base case: a spiral with one layer will contain the number 1
    if layers < 2:
        return _matrix
    
    side_min_1 = side - 1
    value = side * side
    
    # fill the top row of the spiral
    for i in range(side_min_1):
        _matrix[_depth][-1 - _depth - i] = value
        value -= 1
    
    # fill the left column of the spiral
    for i in range(side_min_1):
        _matrix[_depth + i][_depth] = value
        value -= 1
    
    # fill the bottom row of the spiral
    for i in range(side_min_1):
        _matrix[-1 - _depth][_depth + i] = value
        value -= 1
    
    # fill the right column of the spiral
    for i in range(side_min_1):
        _matrix[-1 - _depth - i][-1 - _depth] = value
        value -= 1
    
    # recurse to fill the inside of the spiral
    return make_spiral(layers - 1, _matrix, _depth + 1)


def max_bipartite_matching(edge_matrix):
    """Returns the list of edges in the maximum matching of a bipartite graph.

    The argument edge_matrix is a boolean matrix mapping vertices in partition
    V to those in partition U, such that edge_matrix[u][v] = True iff there
    exists an edge between u and v, where u is the index of a vertex in U and v
    is the index of a vertex in V.

    Edges are returned in the format (u, v), with u and v defined as above.
    """

    n = len(edge_matrix)    # number of rows
    m = len(edge_matrix[0]) # number of columns

    # try to assign each row to a column
    col_assignments = [None] * m
    for i in range(n):
        col_marked = [False] * m
        _try_bipartite_match(edge_matrix, i, col_marked, col_assignments)

    # convert to list of matched pairs and return
    return [(i, j) for j, i in enumerate(col_assignments) if i is not None]


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


def minimum_line_cover(matrix):
    """Returns a list of the fewest lines needed to cover all zeros in matrix.

    Lines are given in the format (is_vertical, i), where is_vertical is a
    boolean indicating whether the line is oriented vertically, and i is the
    index of the row (if is_vertical = False) or column (if is_vertical = True)
    in the matrix that would be covered by this line.
    """

    # assign as many (row, col) pairs with zeros as possible
    assignments = _try_assign_zeros(matrix)

    # if all zeros assigned, n lines are needed
    n = len(matrix)
    if len(assignments) == n:
        return [(False, i) for i in range(n)]

    # convert to row assignment array
    row_assignments = [None] * n
    for i, j in assignments:
        row_assignments[i] = j

    # mark all unassigned rows
    m = len(matrix[0])
    row_marked = [False] * n
    col_marked = [False] * m
    new_marked_rows = []
    for i, assigned_col in enumerate(row_assignments):
        if assigned_col is None:
            row_marked[i] = True
            new_marked_rows.append(i)

    while new_marked_rows:
        # mark all unmarked columns with zeros in newly marked rows
        for i in new_marked_rows:
            for j in range(m):
                if not col_marked[j] and matrix[i][j] == 0:
                    col_marked[j] = True

        # mark all unmarked rows with assigned zeros in marked columns
        new_marked_rows = []
        for i in range(n):
            if not row_marked[i] and col_marked[row_assignments[i]]:
                row_marked[i] = True
                new_marked_rows.append(i)

    # cover all unmarked rows and marked columns
    lines = []
    for i, marked in enumerate(row_marked):
        if not marked:
            lines.append((False, i))
    for j, marked in enumerate(col_marked):
        if marked:
            lines.append((True, j))

    return lines


def mod_multiply(n, m, mod):
    """Returns the the product of natural numbers n and m modulo mod."""
    return ((n % mod) * (m % mod)) % mod


def next_multiple(n, min_val):
    """Returns the next multiple of the natural number n >= min_val."""
    return min_val + ((n - (min_val % n)) % n)


def optimal_assignment(cost_matrix):
    """Assigns each row to a column of the square matrix cost_matrix so that
    the sum of the cost values in the assigned positions is minimized.

    Returns a list of matrix coordinates in the format (row, col).
    """

    # make a deep copy so we don't change the input matrix
    cost_matrix = copy.deepcopy(cost_matrix)

    # Step 1: subtract the minimum element from each row
    n = len(cost_matrix)
    for i, row in enumerate(cost_matrix):
        min_value = min(row)
        for j in range(n):
            cost_matrix[i][j] -= min_value

    # Step 2: subtract the minimum element from each column
    for j in range(n):
        col = [cost_matrix[i][j] for i in range(n)]
        min_value = min(col)
        for i in range(n):
            cost_matrix[i][j] -= min_value

    # Step 3: cover zeros with minimum number of lines
    lines = minimum_line_cover(cost_matrix)

    # Step 4: subtract min uncovered from all uncovered & add to double-covered
    while len(lines) < n:
        # find rows and columns covered by lines
        covered_rows = set()
        covered_cols = set()
        for is_vertical, index in lines:
            if is_vertical:
                covered_cols.add(index)
            else:
                covered_rows.add(index)

        # search for min uncovered value
        min_value = INFINITY
        for i, row in enumerate(cost_matrix):
            if i in covered_rows:
                continue
            for j, value in enumerate(row):
                if j in covered_cols:
                    continue
                if value < min_value:
                    min_value = value

        # subtract and add min value to matrix entries as needed
        for i in range(n):
            for j in range(n):
                if i not in covered_rows and j not in covered_cols:
                    cost_matrix[i][j] -= min_value
                elif i in covered_rows and j in covered_cols:
                    cost_matrix[i][j] += min_value

        # repeat steps 3-4 until n lines are needed to cover zeros
        lines = minimum_line_cover(cost_matrix)

    # now that a total assignment exists, find and return it
    return _try_assign_zeros(cost_matrix)


def pandigital_string(first=0, last=9):
    """Returns a string with each of the digits from first to last in order."""
    return ''.join(map(str, range(first, last + 1)))


def pentagonal(n):
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


def quadratic_roots(a, b, c):
    """Finds all roots of the equation a*x^2 + b*x + c = 0, where a != 0.

    Returns a tuple (x0, x1), where x0 and x1 are solutions for x in the above
    equation and x0 <= x1, assuming a natural ordering. Note that x0 and x1 may
    each contain an imaginary part if no corresponding real solution exists."""
    
    axis = -b
    delta = (b**2 - 4 * a * c)**0.5
    denom = 2 * a
    return (axis - delta) / denom, (axis + delta) / denom


def radical(n):
    """Returns the product of the distinct prime factors of n."""

    # find the distinct prime factors of n
    factors = [factor for (factor, _) in prime_factorization(n)]

    # multiply factors to find their product
    return reduce(operator.mul, factors, 1)


def sqrt_decimal_expansion(n, precision):
    """Returns the square root of the natural number n to arbitrary precision.

    Result is a string with precision digits following the decimal point."""

    # break n into two-digit chunks
    n_digits = []
    while n > 0:
        n, mod = divmod(n, 100)
        n_digits.append(mod)
    n_digits.reverse()

    expansion = []
    remainder = 0
    root_part = 0

    def f(x):
        return x * (20 * root_part + x)

    # compute digits before decimal point
    for carry in n_digits:
        a = 1
        b = f(a)
        c = remainder * 100 + carry
        while b <= c:
            a += 1
            b = f(a)

        a -= 1
        b = f(a)
        remainder = c - b
        root_part = root_part * 10 + a
        expansion.append(str(a))

    expansion.append('.')

    # compute digits after decimal point
    for _ in range(precision):
        a = 1
        b = f(a)
        c = remainder * 100
        while b <= c:
            a += 1
            b = f(a)

        a -= 1
        b = f(a)
        remainder = c - b
        root_part = root_part * 10 + a
        expansion.append(str(a))

    return ''.join(expansion)


def sqrt_fraction_expansion(n):
    """Returns the terms in the continued fraction expansion of the square root
    of the non-square natural number n, in the format (a0, a1..ar)."""

    # perform the first expansion step
    sqrt_n = math.sqrt(n)
    a0 = int(sqrt_n)
    addend = -a0
    denom = 1

    # continue expansion until terms begin to cycle
    block = []
    end_term = 2 * a0
    while True:
        # compute newly expanded denominator
        new_denom = n - addend**2
        new_denom //= gcd(denom, new_denom)

        # extract term and compute new addend
        term = int((sqrt_n - addend) / new_denom)
        new_addend = -addend - (term * new_denom)

        # add term to expansion and update rational value
        block.append(term)
        addend = new_addend
        denom = new_denom

        # check if term completes cycle
        if term == end_term:
            return a0, block


def strings_from_file(input_file, sep=','):
    """Returns a list of sep-separated quoted strings read from input_file."""
    with open(input_file) as f:
        return [string.strip('"') for string in f.read().split(sep)]


def sum_digits(n):
    """Returns the sum of the decimal digits of the natural number n."""
    digit_sum = 0
    while n != 0:
        n, digit = divmod(n, 10)
        digit_sum += digit
    return digit_sum


def sum_keep_digits(m, n, d=None):
    """Returns the last d decimal digits of the sum of m and n. If d is None,
    returns the entire sum."""
    if d is None:
        return m + n
    else:
        mod = 10**d
        return ((m % mod) + (n % mod)) % mod


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
    return (2 * n**3 + 3 * n**2 + n) // 6


def sum_proper_divisors(n):
    """Returns the sum of the proper divisors of the natural number n."""
    return sum_divisors(n) - n


def totient(n, prime_factors=None):
    """Returns the number of integers between 0 and n relatively prime to n."""
    
    # determine prime factors of n if not provided
    if prime_factors is None:
        prime_factors = [factor for (factor, _) in prime_factorization(n)]
    
    # calculate totient using Euler's product formula
    numer = n
    denom = 1
    for p in prime_factors:
        numer *= p - 1
        denom *= p

    return numer // denom


def totients_up_to(n):
    """Returns the values of Euler's totient function for integers 2 to n."""

    # initialize sieve of Eratosthenes up to n
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    prime_factors = [[] for _ in range(n + 1)]

    # run sieve algorithm, keeping track of prime factors
    for curr_num in range(2, n + 1):
        if sieve[curr_num]:
            prime_factors[curr_num].append(curr_num)
            for multiple in range(2 * curr_num, n + 1, curr_num):
                sieve[multiple] = False
                prime_factors[multiple].append(curr_num)

    # calculate each totient using its prime factors
    totients = []
    for i, factors in enumerate(prime_factors[2:]):
        totients.append(totient(i + 2, factors))

    return totients


def triangular(n):
    """Returns the nth triangle number, or the sum of the natural numbers up to
    and including n."""
    return n * (n + 1) // 2


def try_add_matrix_edge(graph, matrix, node, row, col):
    """Adds edge from node to (row, col) in graph if a valid matrix index."""
    n = len(matrix)
    if 0 <= row < n and 0 <= col < n:
        graph.add_edge(node, (row, col), matrix[row][col])
