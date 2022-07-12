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

class Hand:

    def __init__(self, cards):
        self.__cards = sorted(cards)[::-1]
        self.__amounts_of_card_ranks = dict.fromkeys(CardRank, 0)
        for card in cards:
            self.__amounts_of_card_ranks[card.rank] += 1

        self.__HAND_RANKING = [
            ('Royal Flush', self.__get_royal_flush_rank),
            ('Straight Flush', self.__get_straight_flush_rank),
            ('Four of a Kind', self.__get_four_of_a_kind_rank),
            ('Full House', self.__get_full_house_rank),
            ('Flush', self.__get_flush_rank),
            ('Straight', self.__get_straight_rank),
            ('Three of a Kind', self.__get_three_of_kind_rank),
            ('Two Pair', self.__get_two_pair_rank),
            ('One Pair', self.__get_one_pair_rank),
            ('High Card', self.__get_high_card_rank)
        ]

        self.__name, self.__rank = self.__generate_name_and_rank()

    def __str__(self):
        return '[' + reduce(lambda x, y: str(x) + ', ' + str(y), self.__cards) + ']'

    @property
    def name(self):
        return self.__name

    @property
    def rank(self):
        return self.__rank

    @property
    def cards(self):
        return self.__cards

    def __get_royal_flush_rank(self):
        if self.__get_straight_flush_rank() is None or self.__cards[0].rank != CardRank.ACE:
            return None
        return []
    
    def __get_straight_flush_rank(self):
        if self.__get_straight_rank() is None or self.__get_flush_rank() is None:
            return None
        return [self.__cards[0].rank]

    def __get_four_of_a_kind_rank(self):
        rank = []
        for card_rank, amount in self.__amounts_of_card_ranks.items():
            if amount == 4:
                rank.append(card_rank)
                break
        if not rank: 
            return None
        for card in self.__cards:
            if card.rank != rank[0]:
                rank.append(card.rank)
        return rank

    def __get_full_house_rank(self):
        three_of_a_kind_rank = self.__get_three_of_kind_rank()
        one_pair_rank = self.__get_one_pair_rank()
        if three_of_a_kind_rank is None or one_pair_rank is None:
            return None
        return [three_of_a_kind_rank[0], one_pair_rank[0]]

    def __get_flush_rank(self):
        suit = self.__cards[0].suit
        for card in self.__cards[1:]:
            if card.suit != suit:
                return None
        return self.__get_high_card_rank()

    def __get_straight_rank(self):
        previous_card = self.__cards[0]
        for card in self.__cards[1:]:
            if previous_card.rank.index != card.rank.index + 1:
                return None
            previous_card = card
        return [self.__cards[0].rank]

    def __get_three_of_kind_rank(self):
        rank = []
        for card_rank, amount in self.__amounts_of_card_ranks.items():
            if amount == 3:
                rank.append(card_rank)
                break
        if not rank:
            return None
        for card in self.__cards:
            if card.rank != rank[0]:
                rank.append(card.rank)
        return rank

    def __get_two_pair_rank(self):
        rank = []
        for card_rank, amount in self.__amounts_of_card_ranks.items():
            if amount == 2:
                rank.append(card_rank)
        if len(rank) != 2:
            return None
        rank = sorted(rank)[::-1]
        for card in self.__cards:
            if not card.rank in rank[:2]:
                rank.append(card.rank)
        return rank

    def __get_one_pair_rank(self):
        rank = []
        for card_rank, amount in self.__amounts_of_card_ranks.items():
            if amount == 2:
                rank.append(card_rank)
        if len(rank) != 1:
            return None
        for card in self.__cards:
            if card.rank != rank[0]:
                rank.append(card.rank)
        return rank

    def __get_high_card_rank(self):
        rank = []
        for card in self.__cards:
            rank.append(card.rank)
        return rank

    def __generate_name_and_rank(self):        
        for i, hand in enumerate(self.__HAND_RANKING):
            rank = hand[1]()
            if not rank is None:
                return (
                    self.__HAND_RANKING[i][0],
                    [len(self.__HAND_RANKING) - i - 1] + [card_rank.index for card_rank in rank]
                )

    def __eq__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank == other.rank

    def __ne__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank != other.rank

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank < other.rank

    def __le__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank <= other.rank

    def __gt__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank > other.rank

    def __ge__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank >= other.rank
