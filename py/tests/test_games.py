#!/usr/bin/env python3

"""test_games.py

Unit test for the 'games' common module.
"""

__author__ = 'Curtis Belmonte'

import unittest

from common.games import Card, GameBoard


class TestCard(unittest.TestCase):
    all_faces = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q',
                 'K', 'A')

    all_suits = ('D', 'H', 'C', 'S')

    def test_str(self) -> None:
        for face in TestCard.all_faces:
            for suit in TestCard.all_suits:
                self.assertEqual(str(Card(face + suit)), face + suit)

    def test_repr(self) -> None:
        for face in TestCard.all_faces:
            for suit in TestCard.all_suits:
                self.assertEqual(repr(Card(face + suit)), face + suit)

    def test_eq(self) -> None:
        card_3h = Card('3H')
        self.assertTrue(card_3h == card_3h)
        self.assertTrue(card_3h == Card('3H'))
        self.assertFalse(card_3h == Card('7C'))
        self.assertFalse(card_3h == Card('3D'))
        self.assertFalse(card_3h == Card('2H'))
        self.assertTrue(Card('TS') == Card('10S'))

    def test_lt(self) -> None:
        self.assertFalse(Card('8H') < Card('6H'))
        self.assertFalse(Card('8H') < Card('7H'))
        self.assertFalse(Card('8H') < Card('8H'))
        self.assertTrue(Card('8H') < Card('9H'))
        self.assertTrue(Card('8H') < Card('10H'))
        self.assertTrue(Card('8H') < Card('JH'))
        self.assertFalse(Card('8H') < Card('8D'))
        self.assertTrue(Card('8H') < Card('8C'))
        self.assertTrue(Card('8H') < Card('8S'))
        self.assertFalse(Card('TH') < Card('TD'))
        self.assertFalse(Card('TH') < Card('TH'))
        self.assertTrue(Card('TH') < Card('TC'))
        self.assertTrue(Card('TH') < Card('TS'))

    def test_hash(self) -> None:
        card_2c = Card('2C')
        self.assertTrue(hash(card_2c) == hash(card_2c))
        self.assertTrue(hash(card_2c) == hash(Card('2C')))
        self.assertFalse(hash(card_2c) == hash(Card('7H')))
        self.assertFalse(hash(card_2c) == hash(Card('2S')))
        self.assertFalse(hash(card_2c) == hash(Card('3C')))
        self.assertTrue(hash(Card('10D')) == hash(Card('TD')))


class TestGameBoard(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
