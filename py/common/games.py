#!/usr/bin/env python3

"""games.py



Author: Curtis Belmonte
"""

import collections
import functools

import common.arrays as arrs
import common.probability as prob


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
        return (type(self) is type(other) and
                self.face == other.face and
                self.suit == other.suit)

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
        space_map = arrs.inverse_index_map(space_list)

        for position, space in enumerate(space_list):
            # if no rules specified, player always ends on this space
            if space.type not in move_rules:
                move_probs.append({position: 1})
                continue

            # convert rules to positions and assign probabilities to them
            space_probs = collections.defaultdict(int)
            rule_probs = move_rules[space.type]
            total_prob = 0
            for rule, p in rule_probs.items():
                rule_dest = GameBoard._get_rule_dest(
                    rule,
                    position,
                    space_list,
                    space_map)
                space_probs[rule_dest] += p
                total_prob += p

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
        for dest, p in self._move_probs[target].items():
            dests.append(dest)
            probs.append(p)

        # choose end position probabilistically
        return prob.choose_weighted_random(dests, probs)
