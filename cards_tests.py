import unittest
from cards import CardSuit, CardValue, Card, Hand


class TestCards(unittest.TestCase):
    def test_card_suits_strings(self):
        self.assertEqual(str(CardSuit.HEARTS), '♥')
        self.assertEqual(str(CardSuit.DIAMONDS), '♦')
        self.assertEqual(str(CardSuit.CLUBS), '♣')
        self.assertEqual(str(CardSuit.SPADES), '♠')

    def test_card_values_strings(self):
        self.assertEqual(str(CardValue.QUEEN), 'Q')

    def test_card_values_comparison(self):
        self.assertTrue(CardValue.THREE > CardValue.TWO)
        self.assertFalse(CardValue.THREE > CardValue.THREE)
        self.assertTrue(CardValue.THREE >= CardValue.THREE)
        self.assertFalse(CardValue.THREE >= CardValue.KING)
        self.assertTrue(CardValue.JACK < CardValue.ACE)
        self.assertFalse(CardValue.KING < CardValue.THREE)
        self.assertTrue(CardValue.KING <= CardValue.KING)
        self.assertFalse(CardValue.ACE <= CardValue.KING)

    def test_card_values_comparison_typeerror(self):
        with self.assertRaises(TypeError):
            CardValue.KING > 2

    def test_card_suit_type(self):
        self.assertRaises(TypeError, Card, 0, CardValue.KING)

    def test_card_value_type(self):
        self.assertRaises(TypeError, Card, CardSuit.CLUBS, 0)

    def test_card_equal(self):
        self.assertEqual(Card(CardSuit.HEARTS, CardValue.TEN), Card(CardSuit.CLUBS, CardValue.TEN))
        self.assertNotEqual(Card(CardSuit.HEARTS, CardValue.TEN), Card(CardSuit.HEARTS, CardValue.ACE))

    def test_card_comparison(self):
        ace = Card(CardSuit.HEARTS, CardValue.ACE)
        king = Card(CardSuit.HEARTS, CardValue.KING)
        queen = Card(CardSuit.HEARTS, CardValue.QUEEN)

        self.assertTrue(king > queen)
        self.assertFalse(queen > ace)
        self.assertTrue(ace >= ace)
        self.assertFalse(king >= ace)
        self.assertTrue(queen < king)
        self.assertFalse(ace < king)
        self.assertTrue(queen <= queen)
        self.assertFalse(king <= queen)

    def test_hand_to_string(self):
        h = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.DIAMONDS, CardValue.FOUR)
        ])
        self.assertEqual(str(h), '[A♥, K♠, J♥, 4♦, 2♥]')


if __name__ == '__main__':
    unittest.main()