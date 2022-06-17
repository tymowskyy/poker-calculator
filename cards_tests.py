import unittest
from cards import CardSuit, CardValue


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


if __name__ == '__main__':
    unittest.main()