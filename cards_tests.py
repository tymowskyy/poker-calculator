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
        hand = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.DIAMONDS, CardValue.FOUR)
        ])
        self.assertEqual(str(hand), '[A♥, K♠, J♥, 4♦, 2♥]')

    def test_hand_names(self):
        royal_flush = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.HEARTS, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.QUEEN),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.HEARTS, CardValue.TEN)
        ])
        straight_flush = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.HEARTS, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.TEN),
            Card(CardSuit.HEARTS, CardValue.QUEEN),
            Card(CardSuit.HEARTS, CardValue.NINE)
        ])
        four_of_a_kind = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.JACK),
            Card(CardSuit.CLUBS, CardValue.JACK),
            Card(CardSuit.DIAMONDS, CardValue.JACK),
            Card(CardSuit.DIAMONDS, CardValue.FOUR)
        ])
        full_house = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.ACE),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.DIAMONDS, CardValue.JACK)
        ])
        flush = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.HEARTS, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.HEARTS, CardValue.FOUR)
        ])
        straight = Hand([
            Card(CardSuit.SPADES, CardValue.JACK),
            Card(CardSuit.HEARTS, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.QUEEN),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.HEARTS, CardValue.TEN)
        ])
        three_of_a_kind = Hand([
            Card(CardSuit.SPADES, CardValue.JACK),
            Card(CardSuit.DIAMONDS, CardValue.TWO),
            Card(CardSuit.CLUBS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.FOUR)
        ])
        two_pair = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.JACK),
            Card(CardSuit.HEARTS, CardValue.EIGHT),
            Card(CardSuit.SPADES, CardValue.EIGHT),
            Card(CardSuit.HEARTS, CardValue.FOUR)
        ])
        one_pair = Hand([
            Card(CardSuit.SPADES, CardValue.JACK),
            Card(CardSuit.DIAMONDS, CardValue.KING),
            Card(CardSuit.CLUBS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.KING),
            Card(CardSuit.DIAMONDS, CardValue.FOUR)
        ])
        high_card = Hand([
            Card(CardSuit.HEARTS, CardValue.JACK),
            Card(CardSuit.SPADES, CardValue.KING),
            Card(CardSuit.HEARTS, CardValue.TWO),
            Card(CardSuit.HEARTS, CardValue.ACE),
            Card(CardSuit.DIAMONDS, CardValue.FOUR)
        ])

        self.assertEqual(royal_flush.get_name(), 'Royal Flush')
        self.assertEqual(straight_flush.get_name(), 'Straight Flush')
        self.assertEqual(four_of_a_kind.get_name(), 'Four of a Kind')
        self.assertEqual(full_house.get_name(), 'Full House')
        self.assertEqual(flush.get_name(), 'Flush')
        self.assertEqual(straight.get_name(), 'Straight')
        self.assertEqual(three_of_a_kind.get_name(), 'Three of a Kind')
        self.assertEqual(two_pair.get_name(), 'Two Pair')
        self.assertEqual(one_pair.get_name(), 'One Pair')
        self.assertEqual(high_card.get_name(), 'High Card')

if __name__ == '__main__':
    unittest.main()