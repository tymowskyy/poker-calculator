from enum import Enum


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
        self.raise_if_not_cardvalue(other)
        return self.value[0] < other.value[0]

    def __le__(self, other):
        self.raise_if_not_cardvalue(other)
        return self.value[0] <= other.value[0]

    def __gt__(self, other):
        self.raise_if_not_cardvalue(other)
        return self.value[0] > other.value[0]

    def __ge__(self, other):
        self.raise_if_not_cardvalue(other)
        return self.value[0] >= other.value[0]

    def raise_if_not_cardvalue(self, o):
        if not isinstance(o, CardValue):
            raise TypeError('CardValue can only be compared with another CardValue')