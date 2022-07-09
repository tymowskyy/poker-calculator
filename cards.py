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
    TWO = (1, '2')
    THREE = (2, '3')
    FOUR = (3, '4')
    FIVE = (4, '5')
    SIX = (5, '6')
    SEVEN = (6, '7')
    EIGHT = (7, '8')
    NINE = (8, '9')
    TEN = (9, '10')
    JACK = (10, 'J')
    QUEEN = (11, 'Q')
    KING = (12, 'K')
    ACE = (13, 'A')

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
            ('Royal Flush', self.is_royal_flush),
            ('Straight Flush', self.is_straight_flush),
            ('Four of a Kind', self.is_four_of_a_kind),
            ('Full House', self.is_full_house),
            ('Flush', self.is_flush),
            ('Straight', self.is_straight),
            ('Three of Kind', self.is_three_of_kind),
            ('Two Pair', self.is_two_pair),
            ('One Pair', self.is_one_pair),
            ('High Card', self.is_high_card)
        ]

    def __str__(self):
        return '[' + reduce(lambda x, y: str(x) + ', ' + str(y), self.cards_sorted) + ']'

    def is_royal_flush(self):
        return self.is_straight_flush() and self.cards_sorted[0].value == CardValue.ACE
    
    def is_straight_flush(self):
        return self.is_straight() and self.is_flush()

    def is_four_of_a_kind(self):
        for value, amount in self.amounts_of_card_values.items():
            if amount == 4:
                return True
        return False

    def is_full_house(self):
        return self.is_three_of_kind() and self.is_one_pair()

    def is_flush(self):
        suit = self.cards[0].suit
        for card in self.cards[1:]:
            if card.suit != suit:
                return False
        return True

    def is_straight(self):
        previous_card = self.cards_sorted[0]
        for card in self.cards_sorted[1:]:
            if previous_card.value.value[0] != card.value.value[0] + 1:
                return False
            previous_card = card
        return True

    def is_three_of_kind(self):
        for value, amount in self.amounts_of_card_values.items():
            if amount == 3:
                return True
        return False

    def is_two_pair(self):
        was_pair = False
        for value, amount in self.amounts_of_card_values.items():
            if amount == 2:
                if was_pair:
                    return True
                else:
                    was_pair = True
        return False

    def is_one_pair(self):
        for value, amount in self.amounts_of_card_values.items():
            if amount == 2:
                return True
        return False

    def is_high_card(self):
        return True

    def get_hand_name(self):
        for hand in self.HAND_RANKING:
            if hand[1]():
                return hand[0]

h = Hand([
    Card(CardSuit.HEARTS, CardValue.JACK),
    Card(CardSuit.SPADES, CardValue.KING),
    Card(CardSuit.HEARTS, CardValue.TWO),
    Card(CardSuit.HEARTS, CardValue.ACE),
    Card(CardSuit.DIAMONDS, CardValue.ACE)
])
print(h.amounts_of_card_values)
print(h.get_hand_name())