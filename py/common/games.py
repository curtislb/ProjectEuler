#!/usr/bin/env python3

"""games.py

Classes and functions for simulating games such as cards and board games.
"""

__author__ = 'Curtis Belmonte'

from collections import defaultdict
from enum import Enum
from functools import total_ordering
from typing import *

import common.arrays as arrs
import common.probability as prob
from common.types import Real
from common.utility import simple_equality


@simple_equality
@total_ordering
class Card(object):
    """Class representing a standard playing card."""

    class Face(Enum):
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

    class Suit(Enum):
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

    @classmethod
    def _str_to_face(cls, s: str) -> Face:
        """Converts a string to a face value."""
        if s in cls._face_map:
            return cls._face_map[s]
        else:
            raise ValueError('cannot convert {0} to face'.format(s))

    @classmethod
    def _str_to_suit(cls, s: str) -> Suit:
        """Converts a string to a suit."""
        if s in cls._suit_map:
            return cls._suit_map[s]
        else:
            raise ValueError('cannot convert {0} to suit'.format(s))

    def __init__(self, str_rep: str) -> None:
        self._str_rep = ''.join(str_rep.split()).upper()
        self.face = self._str_to_face(self._str_rep[:-1])
        self.suit = self._str_to_suit(self._str_rep[-1])

    def __str__(self) -> str:
        return self._str_rep

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Any) -> bool:
        return (type(self) is type(other) and
                self.face == other.face and
                self.suit == other.suit)

    def __lt__(self, other: Any) -> bool:
        if self.face.value < other.face.value:
            return True
        elif self.face.value > other.face.value:
            return False
        else:
            return self.suit.value < other.suit.value

    def __hash__(self) -> int:
        return hash((self.face, self.suit))


class GameBoard(object):
    """Class representing a game board with a cyclical sequence of spaces.

    This class supports defining a set of types that are assigned to the spaces
    in the board. It also allows rules to be specified for each space type that
    give some probability of ending a turn on a different space than the one
    which was landed on."""

    @simple_equality
    class Space(object):
        """Class representing a space on the board, with a type and number."""

        def __init__(self, space_type: str, number: int) -> None:
            self.type = space_type
            self.number = number

        def __str__(self) -> str:
            return '{0}{1}'.format(self.type, self.number)

        def __repr__(self) -> str:
            return str(self)

        def __eq__(self, other: Any) -> bool:
            return (type(self) is type(other) and
                    self.type == other.type and
                    self.number == other.number)

        def __hash__(self) -> int:
            return hash((self.type, self.number))

    # Custom type for a rule specifying where a player should move when landing
    # on a space of a given type. Can be any of:
    # - (str, int): player should move to the specified space
    # - str: player should move to the next space of this type
    # - int: player should move forward this many spaces
    MoveRule = Union[Tuple[str, int], str, int]

    # Other custom type aliases
    SpaceList = Sequence[Optional[Space]]
    SpaceMap = Mapping[Optional[Space], int]
    SpaceTypeMap = Mapping[str, Sequence[int]]
    MoveProbs = Sequence[Mapping[int, Real]]
    MoveRules = Mapping[str, Mapping[MoveRule, Real]]

    def __init__(
            self,
            space_type_map: SpaceTypeMap,
            move_rules: MoveRules) -> None:
        self._space_list = self._make_space_list(space_type_map)
        self._move_probs = self._make_move_probs(move_rules, self._space_list)

    @classmethod
    def _make_space_list(cls, space_type_map: SpaceTypeMap) -> SpaceList:
        """Contructs an ordered sequence of board spaces from a map of space
        types to their positions on the board."""

        # allocate the list of spaces
        num_spaces = sum(map(len, space_type_map.values()))
        space_list = [None] * num_spaces # type: List

        # create spaces and assign them to their board positions
        for space_type, indices in space_type_map.items():
            for i, index in enumerate(indices):
                space_list[index] = cls.Space(space_type, i + 1)

        return space_list

    @classmethod
    def _make_move_probs(
            cls,
            move_rules: MoveRules,
            space_list: SpaceList) -> MoveProbs:

        """Constructs an ordered list of move probabilities from each space.

        move_rules  Maps space types to the probability of ending up on a
                    different space after landing on them. Each space type maps
                    to another dict, mapping rules to probabilities.

        space_list  An ordered list of all spaces on the board.
        """

        move_probs = []
        space_map = arrs.inverse_index_map(space_list)

        for position, space in enumerate(space_list):
            # if no rules specified, player always ends on this space
            if space is not None and space.type not in move_rules:
                move_probs.append({position: 1})
                continue

            # convert rules to positions and assign probabilities to them
            space_probs = defaultdict(int) # type: Dict
            rule_probs = move_rules[space.type]
            total_prob = 0
            for rule, p in rule_probs.items():
                rule_dest = cls._get_rule_dest(
                    rule, position, space_list, space_map)
                space_probs[rule_dest] += p
                total_prob += p # type: ignore

            # player ends on this space with remaining probability
            if total_prob < 1:
                space_probs[position] += 1 - total_prob

            move_probs.append(space_probs)

        return move_probs

    @classmethod
    def _get_rule_dest(
            cls,
            rule: MoveRule,
            position: int,
            space_list: SpaceList,
            space_map: SpaceMap) -> int:

        """Returns the position that corresponds to a given rule.

        rule        The rule specifying a space that a player could move to
        position    The player's current position on the board
        space_list  An ordered list of all spaces on the board
        space_map   A dict mapping each space to its position on the board
        """

        # check if rule is tuple, indicating a particular space
        if isinstance(rule, tuple):
            return space_map[cls.Space(*rule)]

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
        raise ValueError(
            'rule {0} of type {1} is invalid'.format(rule, type(rule)))

    def move(self, start: int, spaces: int) -> int:
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
