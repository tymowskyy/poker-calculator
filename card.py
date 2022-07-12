from enum import Enum

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


class CardRank(Enum):

    TWO = 0, '2'
    THREE = 1, '3'
    FOUR = 2, '4'
    FIVE = 3, '5'
    SIX = 4, '6'
    SEVEN = 5, '7'
    EIGHT = 6, '8'
    NINE = 7, '9'
    TEN = 8, '10'
    JACK = 9, 'J'
    QUEEN = 10, 'Q'
    KING = 11, 'K'
    ACE = 12, 'A'

    @property
    def index(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.index < other.index

    def __le__(self, other):
        raise_if_not_same_type(self, other)
        return self.index <= other.index

    def __gt__(self, other):
        raise_if_not_same_type(self, other)
        return self.index > other.index

    def __ge__(self, other):
        raise_if_not_same_type(self, other)
        return self.index >= other.index


class Card:

    def __init__(self, suit: CardSuit, rank: CardRank):
        if not isinstance(suit, CardSuit):
            raise TypeError('suit must be CardSuit type')
        if not isinstance(rank, CardRank):
            raise TypeError('rank must be CardRank type')

        self.__suit = suit
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank

    def __str__(self):
        return str(self.__rank) + str(self.__suit)

    def __eq__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank == other.rank

    def __ne__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank != other.rank

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank < other.rank

    def __le__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank <= other.rank

    def __gt__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank > other.rank
 
    def __ge__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank >= other.rank