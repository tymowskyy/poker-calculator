import unittest
from card import Card, CardSuit, CardRank
from hand import Hand, HandCategory


class TestHands(unittest.TestCase):

    def test_hand_to_string(self):
        hand = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        self.assertEqual(str(hand), '[A♥, K♠, J♥, 4♦, 2♥]')

    def test_hand_category_names(self):
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

        self.assertEqual(str(royal_flush.category), 'Royal Flush')
        self.assertEqual(str(straight_flush.category), 'Straight Flush')
        self.assertEqual(str(four_of_a_kind.category), 'Four of a Kind')
        self.assertEqual(str(full_house.category), 'Full House')
        self.assertEqual(str(flush.category), 'Flush')
        self.assertEqual(str(straight.category), 'Straight')
        self.assertEqual(str(three_of_a_kind.category), 'Three of a Kind')
        self.assertEqual(str(two_pair.category), 'Two Pair')
        self.assertEqual(str(one_pair.category), 'One Pair')
        self.assertEqual(str(high_card.category), 'High Card')

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
            HandCategory.ROYAL_FLUSH
        ])
        self.assertEqual(straight_flush.rank, [
            HandCategory.STRAIGHT_FLUSH,
            CardRank.KING
        ])
        self.assertEqual(four_of_a_kind.rank, [
            HandCategory.FOUR_OF_A_KIND,
            CardRank.JACK,
            CardRank.FOUR
        ])
        self.assertEqual(full_house.rank, [
            HandCategory.FULL_HOUSE,
            CardRank.JACK,
            CardRank.ACE
        ])
        self.assertEqual(flush.rank, [
            HandCategory.FLUSH,
            CardRank.ACE,
            CardRank.KING,
            CardRank.JACK,
            CardRank.FOUR,
            CardRank.TWO
        ])
        self.assertEqual(straight.rank, [
            HandCategory.STRAIGHT,
            CardRank.ACE
        ])
        self.assertEqual(three_of_a_kind.rank, [
            HandCategory.THREE_OF_A_KIND,
            CardRank.TWO,
            CardRank.JACK,
            CardRank.FOUR
        ])
        self.assertEqual(two_pair.rank, [
            HandCategory.TWO_PAIR,
            CardRank.JACK,
            CardRank.EIGHT,
            CardRank.FOUR
        ])
        self.assertEqual(one_pair.rank, [
            HandCategory.ONE_PAIR,
            CardRank.KING,
            CardRank.JACK,
            CardRank.FOUR,
            CardRank.TWO

        ])
        self.assertEqual(high_card.rank, [
            HandCategory.HIGH_CARD,
            CardRank.ACE,
            CardRank.KING,
            CardRank.JACK,
            CardRank.FOUR,
            CardRank.TWO
        ])

    def test_hand_from_strings(self):
        hand1 = Hand([
            Card(CardSuit.HEARTS, CardRank.JACK),
            Card(CardSuit.SPADES, CardRank.KING),
            Card(CardSuit.HEARTS, CardRank.TWO),
            Card(CardSuit.HEARTS, CardRank.ACE),
            Card(CardSuit.DIAMONDS, CardRank.FOUR)
        ])
        hand2 = Hand.from_strings(['Ks', 'Jh', '2h', 'ah', '4d'])
        self.assertEqual(hand1.cards, hand2.cards)
    
    def test_hand_comparison(self):
        royal_flush_hearts = Hand.from_strings([
            'Ah', 'Kh', 'Qh', 'Jh', '10h'
        ])
        royal_flush_clubs = Hand.from_strings([
            'Ac', 'Kc', 'Qc', 'Jc', '10c'
        ])
        pair1 = Hand.from_strings([
            'Jc', 'Js', 'As', 'Ks', 'Qc'
        ])
        pair2 = Hand.from_strings([
            'Ac', 'As', '2s', '3s', '5c'
        ])
        pair3 = Hand.from_strings([
            'Ac', 'As', '2s', '7s', '5c'
        ])

        self.assertTrue(royal_flush_clubs == royal_flush_hearts)
        self.assertTrue(royal_flush_clubs > pair1)
        self.assertTrue(pair1 != pair2)
        self.assertFalse(pair3 <= pair2)
        self.assertFalse(pair2 < pair1)
        self.assertFalse(pair1 >= pair3)

if __name__ == '__main__':
    unittest.main()