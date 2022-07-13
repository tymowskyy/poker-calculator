from enum import Enum
from functools import total_ordering

def raise_if_not_same_type(o1, o2):
    if o1.__class__ != o2.__class__:
        raise TypeError('must be {} not {}'.format(o1.__class__.__name__, o2.__class__.__name__))


class CardSuit(Enum):

    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'

    @classmethod
    def from_str(cls, symbol):
        if not isinstance(symbol, str):
            raise TypeError('symbol must be a str')
        symbol = symbol.lower()
        for card_suit in CardSuit:   
            firs_letter = card_suit.name[0].lower()
            if firs_letter == symbol:
                return card_suit 
        raise ValueError('symbol not defined')

    def __str__(self):
        return self.value


@total_ordering
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

    @classmethod
    def from_str(cls, symbol):
        if not isinstance(symbol, str):
            raise TypeError('symbol must be a str')
        symbol = symbol.lower()
        for rank in cls:
            if str(rank).lower() == symbol:
                return rank
        raise ValueError('symbol not defined')
            
    @property
    def index(self):
        return self.value[0]

    def __str__(self):
        return self.value[1]

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.index < other.index



@total_ordering
class Card:

    def __init__(self, suit: CardSuit, rank: CardRank):
        if not isinstance(suit, CardSuit):
            raise TypeError('suit must be CardSuit type')
        if not isinstance(rank, CardRank):
            raise TypeError('rank must be CardRank type')

        self.__suit = suit
        self.__rank = rank

    @classmethod
    def from_str(cls, s):
        if not isinstance(s, str):
           raise TypeError('must be a str') 
        if len(s) < 2:
            raise ValueError('must be at least 2 chars long')
        return cls(
            CardSuit.from_str(s[-1]),
            CardRank.from_str(s[:-1])
        )

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

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.__rank < other.rank