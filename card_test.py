import unittest
from card import CardSuit, CardRank, Card


class TestCards(unittest.TestCase):
    def test_card_suits_strings(self):
        self.assertEqual(str(CardSuit.HEARTS), '♥')
        self.assertEqual(str(CardSuit.DIAMONDS), '♦')
        self.assertEqual(str(CardSuit.CLUBS), '♣')
        self.assertEqual(str(CardSuit.SPADES), '♠')

    def test_card_ranks_strings(self):
        self.assertEqual(str(CardRank.QUEEN), 'Q')

    def test_card_ranks_comparison(self):
        self.assertTrue(CardRank.THREE > CardRank.TWO)
        self.assertFalse(CardRank.THREE > CardRank.THREE)
        self.assertTrue(CardRank.THREE >= CardRank.THREE)
        self.assertFalse(CardRank.THREE >= CardRank.KING)
        self.assertTrue(CardRank.JACK < CardRank.ACE)
        self.assertFalse(CardRank.KING < CardRank.THREE)
        self.assertTrue(CardRank.KING <= CardRank.KING)
        self.assertFalse(CardRank.ACE <= CardRank.KING)

    def test_card_ranks_comparison_typeerror(self):
        with self.assertRaises(TypeError):
            CardRank.KING > 2

    def test_card_suit_type(self):
        self.assertRaises(TypeError, Card, 0, CardRank.KING)

    def test_card_rank_type(self):
        self.assertRaises(TypeError, Card, CardSuit.CLUBS, 0)

    def test_card_equal(self):
        self.assertEqual(Card(CardSuit.HEARTS, CardRank.TEN), Card(CardSuit.CLUBS, CardRank.TEN))
        self.assertNotEqual(Card(CardSuit.HEARTS, CardRank.TEN), Card(CardSuit.HEARTS, CardRank.ACE))

    def test_card_comparison(self):
        ace = Card(CardSuit.HEARTS, CardRank.ACE)
        king = Card(CardSuit.HEARTS, CardRank.KING)
        queen = Card(CardSuit.HEARTS, CardRank.QUEEN)

        self.assertTrue(king > queen)
        self.assertFalse(queen > ace)
        self.assertTrue(ace >= ace)
        self.assertFalse(king >= ace)
        self.assertTrue(queen < king)
        self.assertFalse(ace < king)
        self.assertTrue(queen <= queen)
        self.assertFalse(king <= queen)

    def test_card_suit_from_string(self):
        self.assertEqual(CardSuit.HEARTS, CardSuit.from_str('H'))
        self.assertEqual(CardSuit.DIAMONDS, CardSuit.from_str('D'))
        self.assertEqual(CardSuit.CLUBS, CardSuit.from_str('c'))
        self.assertEqual(CardSuit.SPADES, CardSuit.from_str('s'))

    def test_card_suit_from_string_errors(self):
        with self.assertRaises(TypeError):
            CardSuit.from_str(1)
        with self.assertRaises(ValueError):
            CardSuit.from_str('a')

    def test_card_rank_from_string(self):
        self.assertEqual(CardRank.TWO, CardRank.from_str('2'))
        self.assertEqual(CardRank.ACE, CardRank.from_str('A'))
        self.assertEqual(CardRank.TEN, CardRank.from_str('10'))

    def test_card_rank_from_string_errors(self):
        with self.assertRaises(TypeError):
            CardRank.from_str(1)
        with self.assertRaises(ValueError):
            CardRank.from_str('Z')

    def test_card_from_str(self):
        self.assertEqual(
            Card(CardSuit.DIAMONDS, CardRank.KING),
            Card.from_str('KD')
        )
        self.assertEqual(
            Card(CardSuit.CLUBS, CardRank.TEN),
            Card.from_str('10c')
        )
        self.assertEqual(
            Card(CardSuit.SPADES, CardRank.QUEEN),
            Card.from_str('qs')
        )
    
    def test_card_from_str_errors(self):
        with self.assertRaises(TypeError):
            Card.from_str(1)
        with self.assertRaises(ValueError):
            Card.from_str('')
        

if __name__ == '__main__':
    unittest.main()