import unittest
from card import Card, CardSuit, CardRank
from hand import Hand


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