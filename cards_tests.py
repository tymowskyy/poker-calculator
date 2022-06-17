import unittest
from cards import CardSuit, CardValues


class TestCards(unittest.TestCase):

    def test_card_suits_strings(self):
        self.assertEqual(str(CardSuit.HEARTS), '♥')
        self.assertEqual(str(CardSuit.DIAMONDS), '♦')
        self.assertEqual(str(CardSuit.CLUBS), '♣')
        self.assertEqual(str(CardSuit.SPADES), '♠')

    def test_card_values_strings(self):
        self.assertEqual(str(CardValues.QUEEN), 'Q')

    def test_card_values_comparsion(self):
        self.assertTrue(CardValues.THREE > CardValues.TWO)
        self.assertFalse(CardValues.THREE > CardValues.THREE)
        self.assertTrue(CardValues.THREE >= CardValues.THREE)
        self.assertFalse(CardValues.THREE >= CardValues.KING)
        self.assertTrue(CardValues.JACK < CardValues.ACE)
        self.assertFalse(CardValues.KING < CardValues.THREE)
        self.assertTrue(CardValues.KING <= CardValues.KING)
        self.assertFalse(CardValues.ACE <= CardValues.KING)

if __name__ == '__main__':
    unittest.main()