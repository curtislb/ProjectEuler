#!/usr/bin/env python3

"""Common library for simulating played games.

This module provides classes that can be used to simulate games. Examples
include card games like Poker and board games like Monopoly.
"""

from collections import defaultdict
from enum import Enum
from functools import total_ordering
from typing import Any, Dict, List, Mapping, Sequence, Tuple, Union

import common.arrays as arrs
import common.probability as prob
from common.typex import Real
from common.utility import simple_equality


@simple_equality
@total_ordering
class Card(object):
    """A single card from a standard deck of playing cards.

    Attributes:
        face (Card.Face): The face value of the card (e.g., ``Face.ACE``).
        suit (Card.Suit): The suit of the card (e.g., ``Suit.SPADES``).
    """

    class Face(Enum):
        """Enum of playing card face values."""
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
        """Enum of playing card suits."""
        DIAMONDS = 0
        HEARTS = 1
        CLUBS = 2
        SPADES = 3

    # Dict mapping strings to suits
    _suit_map = {
        'D': Suit.DIAMONDS,
        'H': Suit.HEARTS,
        'C': Suit.CLUBS,
        'S': Suit.SPADES,
    }

    # Dict mapping strings to face values
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

    def __init__(self, str_rep: str) -> None:
        """Initializes a playing card from its string representation.

        Args:
            str_rep: A human-readable string representation of a playing card.
                Should be of the format ``${face}${suit}`` where ``face`` and
                ``suit`` are abbreviations for the face and suit of the card,
                respectively. For convenience, ``face`` and ``suit`` may be
                upper- or lower-case and separated by whitespace.
        """
        self._str_rep = ''.join(str_rep.split()).upper()
        self.face = self._str_to_face(self._str_rep[:-1])
        self.suit = self._str_to_suit(self._str_rep[-1])

    def __str__(self) -> str:
        return self._str_rep

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Any) -> bool:
        return (
            type(self) is type(other) and
            self.face == other.face and
            self.suit == other.suit
        )

    def __lt__(self, other: Any) -> bool:
        if self.face.value < other.face.value:
            return True
        elif self.face.value > other.face.value:
            return False
        else:
            return self.suit.value < other.suit.value

    def __hash__(self) -> int:
        return hash((self.face, self.suit))

    @classmethod
    def _str_to_face(cls, s: str) -> 'Card.Face':
        """Converts a string to a playing card face value.

        Args:
            s: A string representing a face value (e.g., 'A' for ``Face.ACE``).

        Returns:
            The face value corresponding to the given string representation.

        Raises:
            ValueError: If ``s`` does not correspond to any face value.
        """
        if s in cls._face_map:
            return cls._face_map[s]
        else:
            raise ValueError('cannot convert {0} to face'.format(s))

    @classmethod
    def _str_to_suit(cls, s: str) -> 'Card.Suit':
        """Converts a string to a playing card suit.

        Args:
            s: A string representing a suit (e.g., 'S' for ``Suit.SPADES``).

        Returns:
            The face value corresponding to the given string representation.

        Raises:
            ValueError: If ``s`` does not correspond to any face value.
        """
        if s in cls._suit_map:
            return cls._suit_map[s]
        else:
            raise ValueError('cannot convert {0} to suit'.format(s))


class GameBoard(object):
    """A game board with a looping sequence of spaces.

    This class supports defining a set of types that are assigned to the spaces
    in the board. It also allows rules to be specified for each space type that
    give some probability of ending a turn on a different space than the one
    which was landed on.
    """

    @simple_equality
    class Space(object):
        """A single space on the game board.
        
        Attributes:
            space_type: A string representing the type of this space.
            number: A number that is used along with ``space_type`` to
                uniquely identify this space on the board.
        """
        def __init__(self, space_type: str, number: int) -> None:
            """Initializes a board space given its type and number.

            Args:
                space_type: A string representing the type of this space.
                number: A number that is used along with ``space_type`` to
                    uniquely identify this space on the board.
            """
            self.space_type = space_type
            self.number = number

        def __str__(self) -> str:
            return '{0}{1}'.format(self.space_type, self.number)

        def __repr__(self) -> str:
            return str(self)

        def __eq__(self, other: Any) -> bool:
            return (
                type(self) is type(other) and
                self.space_type == other.space_type and
                self.number == other.number
            )

        def __hash__(self) -> int:
            return hash((self.space_type, self.number))

    #: Type of a rule specifying where a player should move when landing on a
    #: space of a given type. Can be any of:
    #:
    #: - ``(space_type: str, number: int)``: Move to the given space.
    #: - ``space_type: str``: Move to the next ``space_type`` space.
    #: - ``distance: int``: Move forward ``distance`` spaces.
    MoveRule = Union[Tuple[str, int], str, int]

    #: Type of a sequence of board spaces.
    SpaceList = Sequence[Space]

    #: Type of a map from each space to its board position.
    SpaceMap = Mapping[Space, int]

    #: Type of a map from each space type to its board positions.
    SpaceTypeMap = Mapping[str, Sequence[int]]

    #: Type of a map from each possible move distance to its probability.
    MoveProbs = Sequence[Mapping[int, Real]]

    #: Type of a map from each space type to its move rules and probabilities.
    MoveRules = Mapping[str, Mapping[MoveRule, Real]]

    def __init__(
        self,
        space_type_map: SpaceTypeMap,
        move_rules: MoveRules,
    ) -> None:
        """Initializes a game board with the given spaces and move rules.

        Args:
            space_type_map: A mapping from each valid space type to a sequence
                of its positions on the board.
            move_rules: A map from space types to the probabilities of ending
                up on different spaces after landing on them. Each space type
                maps to another mapping, from move rules to probabilities.
        """
        self._space_list = self._make_space_list(space_type_map)
        self._move_probs = self._make_move_probs(move_rules, self._space_list)

    def move(self, start: int, spaces: int) -> int:
        """Simulates moving a player a given number of spaces on the board.

        Args:
            start: The board position at which the player starts before moving.
            spaces: The number of spaces forward to move the player. If
                ``spaces`` is negative, the player will move ``abs(spaces)``
                spaces backward.

        Returns:
            The board position at which the player ends their turn, after any
            move rules from the space they initially landed on have been
            applied.
        """

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

    @classmethod
    def _make_space_list(cls, space_type_map: SpaceTypeMap) -> SpaceList:
        """Builds an ordered sequence of board spaces from a space type map.

        Args:
            space_type_map: A mapping from each valid space type to a sequence
                of its positions on the board.

        Returns:
            A sequence of all spaces on the board, ordered by position.
        """

        # allocate the list of spaces
        num_spaces = sum(map(len, space_type_map.values()))
        space_list = [cls.Space('', i) for i in range(num_spaces)]

        # create spaces and assign them to their board positions
        for space_type, indices in space_type_map.items():
            for i, index in enumerate(indices):
                space_list[index] = cls.Space(space_type, i + 1)

        return space_list

    @classmethod
    def _make_move_probs(
        cls,
        move_rules: MoveRules,
        space_list: SpaceList,
    ) -> MoveProbs:
        """Builds an ordered list of move probabilities from each space.

        Args:
            move_rules: A map from space types to the probabilities of ending
                up on different spaces after landing on them. Each space type
                maps to another mapping, from move rules to probabilities.
            space_list: An ordered sequence of all spaces on the board.

        Returns:
            A sequence of length ``len(space_list)``, where the value at each
            index ``m`` is a mapping from move rules to their probability of
            applying when a player lands on the space at position ``m`` on the
            board.
        """

        move_probs: List[Dict[int, Real]] = []
        space_map = arrs.inverse_index_map(space_list)

        for position, space in enumerate(space_list):
            # if no rules specified, player always ends on this space
            if space is not None and space.space_type not in move_rules:
                move_probs.append({position: 1})
                continue

            # convert rules to positions and assign probabilities to them
            space_probs: Dict[int, Real] = defaultdict(int)
            rule_probs = move_rules[space.space_type]
            total_prob: Real = 0
            for rule, p in rule_probs.items():
                rule_dest = cls._get_rule_dest(
                    rule, position, space_list, space_map)
                space_probs[rule_dest] += p
                total_prob += p

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
        space_map: SpaceMap
    ) -> int:
        """Determines where a player should move after applying a move rule.

        Args:
            rule: The rule specifying a space that a player could move to.
            position: The player's current position on the board.
            space_list: An ordered sequence of all spaces on the board.
            space_map: A map from each space to its position on the board.

        Returns:
            The position on the board where the player should end up after
            applying ``rule``. May be equal to ``position`` if the player does
            not move.
        """

        # check if rule is tuple, indicating a particular space
        if isinstance(rule, tuple):
            return space_map[cls.Space(*rule)]

        num_spaces = len(space_list)

        # check if rule is str, indicating next space of given type
        if isinstance(rule, str):
            position = (position + 1) % num_spaces
            while space_list[position].space_type != rule:
                position = (position + 1) % num_spaces
            return position

        # check if rule is int, indicating relative movement
        if isinstance(rule, int):
            return (position + rule) % num_spaces

        # received invalid rule type
        raise ValueError(
            'rule {0} of type {1} is invalid'.format(rule, type(rule)))
