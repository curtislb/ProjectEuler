#!/usr/bin/env python3

"""problem_054.py

Problem 54: Poker hands

In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

    Hand         Player 1            Player 2          Winner
    
    1         5H 5C 6S 7S KD      2C 3S 8S 8D TD      Player 2
              Pair of Fives       Pair of Eights
         
    2         5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
             Highest card Ace   Highest card Queen
         
    3         2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
                Three Aces      Flush with Diamonds
         
    4         4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
              Pair of Queens      Pair of Queens
             Highest card Nine  Highest card Seven
         
    5         2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
                Full House          Full House
             with Three Fours    with Three Threes

The file, INPUT_FILE, contains random hands dealt to two players. Each line of
the file contains ten cards (separated by a single space): the first five are
Player 1's cards and the last five are Player 2's cards. You can assume that
all hands are valid (no invalid characters or repeated cards), each player's
hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

Author: Curtis Belmonte
"""

import common as com

# PARAMETERS ##################################################################

INPUT_FILE = '../input/054.txt' # default: '../input/054.txt

# SOLUTION ####################################################################

def count_faces(cards):
    """Returns a dictionary of occurrences of each face value in cards."""
    counts = {}
    for card in cards:
        if card.face not in counts:
            counts[card.face] = 1
        else:
            counts[card.face] += 1
    return counts


class Rank(object):
    """Class representing the rank and rank value of a poker hand."""
    
    class Type:
        """Enum representing different types of poker hand ranks."""
        HIGH_CARD = 0
        ONE_PAIR = 1
        TWO_PAIRS = 2
        THREE_KIND = 3
        STRAIGHT = 4
        FLUSH = 5
        FULL_HOUSE = 6
        FOUR_KIND = 7
        STRAIGHT_FLUSH = 8
        ROYAL_FLUSH = 9
        
    def _update(self, type_, value):
        """Updates type and value of this rank if the new type is superior."""
        if type_ > self.type:
            self.type = type_
            self.value = value
    
    def __init__(self, hand):
        # initialize type and value with dummy values
        self.type = -1
        self.value = -1
        
        # check for flush or straight hand
        if (hand[0].suit == hand[1].suit and
            hand[1].suit == hand[2].suit and
            hand[2].suit == hand[3].suit and
            hand[3].suit == hand[4].suit):
            if (hand[0].face == com.Card.Face.TEN and
                hand[1].face == com.Card.Face.JACK and
                hand[2].face == com.Card.Face.QUEEN and
                hand[3].face == com.Card.Face.KING and
                hand[4].face == com.Card.Face.ACE):
                self.type = Rank.Type.ROYAL_FLUSH
                self.value = com.Card.Face.ACE
            elif (hand[0].face + 1 == hand[1].face and
                  hand[1].face + 1 == hand[2].face and
                  hand[2].face + 1 == hand[3].face and
                  hand[3].face + 1 == hand[4].face):
                self.type = Rank.Type.STRAIGHT_FLUSH
                self.value = hand[4].face
            else:
                self.type = Rank.Type.FLUSH
                self.value = hand[4].face
        elif (hand[0].face + 1 == hand[1].face and
              hand[1].face + 1 == hand[2].face and
              hand[2].face + 1 == hand[3].face and
              hand[3].face + 1 == hand[4].face):
            self._update(Rank.Type.STRAIGHT, hand[4].face)
            
        counts = count_faces(hand)
        two_of = None
        three_of = None
        
        # check for pairs, three-of-a-kind, and four-of-a-kind card groups
        for face in counts:
            if counts[face] == 4:
                self._update(Rank.Type.FOUR_KIND, face)
                break
            elif counts[face] == 3:
                if two_of is not None:
                    self._update(Rank.Type.FULL_HOUSE, face * 16 + two_of)
                    break
                else:
                    three_of = face
            elif counts[face] == 2:
                if three_of is not None:
                    self._update(Rank.Type.FULL_HOUSE, three_of * 16 + face)
                    break
                elif two_of is not None:
                    self._update(Rank.Type.TWO_PAIRS,
                                 max(face, two_of) * 16 + min(face, two_of))
                    break
                else:
                    two_of = face
        
        # check for three of a kind and one pair, otherwise use highest card
        if three_of is not None:
            self._update(Rank.Type.THREE_KIND, three_of)
        elif two_of is not None:
            self._update(Rank.Type.ONE_PAIR, two_of)
        else:
            self._update(Rank.Type.HIGH_CARD, hand[4].face)


def solve():
    # read (and sort) all hands from input file
    hands = []
    with open(INPUT_FILE) as f:
        for line in f:
            cards = [com.Card(s) for s in line.split()]
            hands.append((sorted(cards[:5]), sorted(cards[5:])))
    
    # count total number of wins for player 1
    wins = 0
    for hand in hands:
        rank_1 = Rank(hand[0])
        rank_2 = Rank(hand[1])
        if rank_1.type > rank_2.type:
            # player 1 has a higher ranked hand than player 2
            wins += 1
        elif rank_1.type == rank_2.type:
            # ranks are tied
            if rank_1.value > rank_2.value:
                # player 1 has a higher rank value than player 2
                wins += 1
            elif rank_1.value == rank_2.value:
                # rank values are tied
                for i in range(4, -1, -1):
                    if hand[0][i].face > hand[1][i].face:
                        # player 1 has a higher card at position i
                        wins += 1
                        break
                    elif hand[0][i].face < hand[1][i].face:
                        # player 2 has a higher card at position i
                        break
    
    return wins


if __name__ == '__main__':
    print(solve())
