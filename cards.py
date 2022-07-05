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

    def __str__(self):
        return '[' + reduce(lambda x, y: str(x) + ', ' + str(y), self.cards_sorted) + ']'

h = Hand([
    Card(CardSuit.HEARTS, CardValue.JACK),
    Card(CardSuit.SPADES, CardValue.KING),
    Card(CardSuit.HEARTS, CardValue.TWO),
    Card(CardSuit.HEARTS, CardValue.ACE),
    Card(CardSuit.DIAMONDS, CardValue.FOUR)
])

print(h)