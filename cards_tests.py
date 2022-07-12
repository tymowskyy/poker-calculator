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

        self.assertEqual(royal_flush.name, 'Royal Flush')
        self.assertEqual(straight_flush.name, 'Straight Flush')
        self.assertEqual(four_of_a_kind.name, 'Four of a Kind')
        self.assertEqual(full_house.name, 'Full House')
        self.assertEqual(flush.name, 'Flush')
        self.assertEqual(straight.name, 'Straight')
        self.assertEqual(three_of_a_kind.name, 'Three of a Kind')
        self.assertEqual(two_pair.name, 'Two Pair')
        self.assertEqual(one_pair.name, 'One Pair')
        self.assertEqual(high_card.name, 'High Card')

    def test_hand_ranks(self):
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

        self.assertEqual(royal_flush.rank, [
            9
        ])
        self.assertEqual(straight_flush.rank, [
            8,
            CardValue.KING.value[0]
        ])
        self.assertEqual(four_of_a_kind.rank, [
            7,
            CardValue.JACK.value[0],
            CardValue.FOUR.value[0]
        ])
        self.assertEqual(full_house.rank, [
            6,
            CardValue.JACK.value[0],
            CardValue.ACE.value[0]
        ])
        self.assertEqual(flush.rank, [
            5,
            CardValue.ACE.value[0],
            CardValue.KING.value[0],
            CardValue.JACK.value[0],
            CardValue.FOUR.value[0],
            CardValue.TWO.value[0]
        ])
        self.assertEqual(straight.rank, [
            4,
            CardValue.ACE.value[0]
        ])
        self.assertEqual(three_of_a_kind.rank, [
            3,
            CardValue.TWO.value[0],
            CardValue.JACK.value[0],
            CardValue.FOUR.value[0]
        ])
        self.assertEqual(two_pair.rank, [
            2,
            CardValue.JACK.value[0],
            CardValue.EIGHT.value[0],
            CardValue.FOUR.value[0]
        ])
        self.assertEqual(one_pair.rank, [
            1,
            CardValue.KING.value[0],
            CardValue.JACK.value[0],
            CardValue.FOUR.value[0],
            CardValue.TWO.value[0]

        ])
        self.assertEqual(high_card.rank, [
            0,
            CardValue.ACE.value[0],
            CardValue.KING.value[0],
            CardValue.JACK.value[0],
            CardValue.FOUR.value[0],
            CardValue.TWO.value[0]
        ])

if __name__ == '__main__':
    unittest.main()