from enum import Enum
from functools import reduce

def raise_if_not_same_type(o1, o2):
    if o1.__class__ != o2.__class__:
        raise TypeError('must be {} not {}'.format(o1.__class__.__name__, o2.__class__.__name__))


class CardSuit(Enum):
    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'

    def __str__(self):
        return self.value


class CardValue(Enum):
    TWO = (0, '2')
    THREE = (1, '3')
    FOUR = (2, '4')
    FIVE = (3, '5')
    SIX = (4, '6')
    SEVEN = (5, '7')
    EIGHT = (6, '8')
    NINE = (7, '9')
    TEN = (8, '10')
    JACK = (9, 'J')
    QUEEN = (10, 'Q')
    KING = (11, 'K')
    ACE = (12, 'A')

    def __str__(self):
        return self.value[1]

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.value[0] < other.value[0]

    def __le__(self, other):
        raise_if_not_same_type(self, other)
        return self.value[0] <= other.value[0]

    def __gt__(self, other):
        raise_if_not_same_type(self, other)
        return self.value[0] > other.value[0]

    def __ge__(self, other):
        raise_if_not_same_type(self, other)
        return self.value[0] >= other.value[0]


class Card:
    suit: CardSuit
    value: CardValue

    def __init__(self, suit: CardSuit, value: CardValue):
        if not isinstance(suit, CardSuit):
            raise TypeError('suit must be CardSuit type')
        if not isinstance(value, CardValue):
            raise TypeError('value must be CardValue type')

        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + str(self.suit)

    def __eq__(self, other):
        raise_if_not_same_type(self, other)
        return self.value == other.value

    def __ne__(self, other):
        raise_if_not_same_type(self, other)
        return self.value != other.value

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.value < other.value

    def __le__(self, other):
        raise_if_not_same_type(self, other)
        return self.value <= other.value


    def __gt__(self, other):
        raise_if_not_same_type(self, other)
        return self.value > other.value
 

    def __ge__(self, other):
        raise_if_not_same_type(self, other)
        return self.value >= other.value

class Hand:
    cards: list
    cards_sorted: list

    def __init__(self, cards):
        self.cards = cards
        self.cards_sorted = sorted(self.cards)[::-1]

        self.amounts_of_card_values = dict.fromkeys(CardValue, 0)
        for card in cards:
            self.amounts_of_card_values[card.value] += 1

        self.HAND_RANKING = [
            ('Royal Flush', self.get_royal_flush_rank),
            ('Straight Flush', self.get_straight_flush_rank),
            ('Four of a Kind', self.get_four_of_a_kind_rank),
            ('Full House', self.get_full_house_rank),
            ('Flush', self.get_flush_rank),
            ('Straight', self.get_straight_rank),
            ('Three of a Kind', self.get_three_of_kind_rank),
            ('Two Pair', self.get_two_pair_rank),
            ('One Pair', self.get_one_pair_rank),
            ('High Card', self.get_high_card_rank)
        ]

    def __str__(self):
        return '[' + reduce(lambda x, y: str(x) + ', ' + str(y), self.cards_sorted) + ']'

    def get_royal_flush_rank(self):
        if self.get_straight_flush_rank() is None or self.cards_sorted[0].value != CardValue.ACE:
            return None
        return []
    
    def get_straight_flush_rank(self):
        if self.get_straight_rank() is None or self.get_flush_rank() is None:
            return None
        return [self.cards_sorted[0].value]

    def get_four_of_a_kind_rank(self):
        rank = []
        for value, amount in self.amounts_of_card_values.items():
            if amount == 4:
                rank.append(value)
                break
        if not rank: 
            return None
        for card in self.cards_sorted:
            if card.value != rank[0]:
                rank.append(card.value)
        return rank

    def get_full_house_rank(self):
        three_of_a_kind_rank = self.get_three_of_kind_rank()
        one_pair_rank = self.get_one_pair_rank()
        if three_of_a_kind_rank is None or one_pair_rank is None:
            return None
        return [three_of_a_kind_rank[0], one_pair_rank[0]]

    def get_flush_rank(self):
        suit = self.cards[0].suit
        for card in self.cards[1:]:
            if card.suit != suit:
                return None
        return self.get_high_card_rank()

    def get_straight_rank(self):
        previous_card = self.cards_sorted[0]
        for card in self.cards_sorted[1:]:
            if previous_card.value.value[0] != card.value.value[0] + 1:
                return None
            previous_card = card
        return [self.cards_sorted[0].value]

    def get_three_of_kind_rank(self):
        rank = []
        for value, amount in self.amounts_of_card_values.items():
            if amount == 3:
                rank.append(value)
                break
        if not rank:
            return None
        for card in self.cards_sorted:
            if card.value != rank[0]:
                rank.append(card.value)
        return rank

    def get_two_pair_rank(self):
        rank = []
        for value, amount in self.amounts_of_card_values.items():
            if amount == 2:
                rank.append(value)
        if len(rank) != 2:
            return None
        rank = sorted(rank)[::-1]
        for card in self.cards_sorted:
            if not card.value in rank[:2]:
                rank.append(card.value)
        return rank

    def get_one_pair_rank(self):
        rank = []
        for value, amount in self.amounts_of_card_values.items():
            if amount == 2:
                rank.append(value)
        if len(rank) != 1:
            return None
        for card in self.cards_sorted:
            if card.value != rank[0]:
                rank.append(card.value)
        return rank

    def get_high_card_rank(self):
        rank = []
        for card in self.cards_sorted:
            rank.append(card.value)
        return rank

    def get_name(self):
        if not hasattr(self, 'name'):
            self.name = self.generate_name()
        return self.name

    def get_rank(self):
        if not hasattr(self, 'rank'):
            self.rank = self.generate_rank()
        return self.rank

    def generate_name(self):
        for hand in self.HAND_RANKING:
            if not hand[1]() is None:
                return hand[0]
    

    def generate_rank(self):        
        for i, hand in enumerate(self.HAND_RANKING):
            rank = hand[1]()
            if not rank is None:
                return [len(self.HAND_RANKING) - i - 1] + [card_value.value[0] for card_value in rank]