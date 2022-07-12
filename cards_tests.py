import unittest
from cards import CardSuit, CardRank, Card, Hand


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

    def test_hand_to_string(self):
        hand = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        self.assertEqual(str(hand), '[A♥, K♠, J♥, 4♦, 2♥]')

    def test_hand_names(self):
        royal_flush = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.QUEEN),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.TEN)
        ])
        straight_flush = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TEN),
            Card(CardSuit.HEARTS, CardRank.QUEEN),
            Card(CardSuit.HEARTS, CardRank.NINE)
        ])
        four_of_a_kind = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.CLUBS, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        full_house = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.JACK)
        ])
        flush = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.FOUR)
        ])
        straight = Hand([
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.QUEEN),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.TEN)
        ])
        three_of_a_kind = Hand([
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.TWO),
            Card(CardSuit.CLUBS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.FOUR)
        ])
        two_pair = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.EIGHT),
            Card(CardSuit.SPADES, CardRank.EIGHT),
            Card(CardSuit.HEARTS, CardRank.FOUR)
        ])
        one_pair = Hand([
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.KING),
            Card(CardSuit.CLUBS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        high_card = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
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
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.QUEEN),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.TEN)
        ])
        straight_flush = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TEN),
            Card(CardSuit.HEARTS, CardRank.QUEEN),
            Card(CardSuit.HEARTS, CardRank.NINE)
        ])
        four_of_a_kind = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.CLUBS, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        full_house = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.JACK)
        ])
        flush = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.FOUR)
        ])
        straight = Hand([
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.QUEEN),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.HEARTS, CardRank.TEN)
        ])
        three_of_a_kind = Hand([
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.TWO),
            Card(CardSuit.CLUBS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.FOUR)
        ])
        two_pair = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.HEARTS, CardRank.EIGHT),
            Card(CardSuit.SPADES, CardRank.EIGHT),
            Card(CardSuit.HEARTS, CardRank.FOUR)
        ])
        one_pair = Hand([
            Card(CardSuit.SPADES, CardRank.JACK),
            Card(CardSuit.DIAMONDS, CardRank.KING),
            Card(CardSuit.CLUBS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.KING),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        high_card = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])

        self.assertEqual(royal_flush.rank, [
            9
        ])
        self.assertEqual(straight_flush.rank, [
            8,
            CardRank.KING.index
        ])
        self.assertEqual(four_of_a_kind.rank, [
            7,
            CardRank.JACK.index,
            CardRank.FOUR.index
        ])
        self.assertEqual(full_house.rank, [
            6,
            CardRank.JACK.index,
            CardRank.ACE.index
        ])
        self.assertEqual(flush.rank, [
            5,
            CardRank.ACE.index,
            CardRank.KING.index,
            CardRank.JACK.index,
            CardRank.FOUR.index,
            CardRank.TWO.index
        ])
        self.assertEqual(straight.rank, [
            4,
            CardRank.ACE.index
        ])
        self.assertEqual(three_of_a_kind.rank, [
            3,
            CardRank.TWO.index,
            CardRank.JACK.index,
            CardRank.FOUR.index
        ])
        self.assertEqual(two_pair.rank, [
            2,
            CardRank.JACK.index,
            CardRank.EIGHT.index,
            CardRank.FOUR.index
        ])
        self.assertEqual(one_pair.rank, [
            1,
            CardRank.KING.index,
            CardRank.JACK.index,
            CardRank.FOUR.index,
            CardRank.TWO.index

        ])
        self.assertEqual(high_card.rank, [
            0,
            CardRank.ACE.index,
            CardRank.KING.index,
            CardRank.JACK.index,
            CardRank.FOUR.index,
            CardRank.TWO.index
        ])

if __name__ == '__main__':
    unittest.main()