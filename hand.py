from enum import Enum
from functools import reduce, total_ordering
from card import Card, CardSuit, CardRank, raise_if_not_same_type


@total_ordering
class HandCategory(Enum):
    ROYAL_FLUSH = 9
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

    def __str__(self):
        words = self.name.lower().split('_')
        words = list(map(lambda word: word if word in ['of', 'a'] else word.capitalize(), words))
        return reduce(lambda x, y: f'{x} {y}', words)

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.value < other.value

@total_ordering
class Hand:

    def __init__(self, cards):
        self.__cards = sorted(cards, reverse=True)
        self.__amounts_of_card_ranks = dict.fromkeys(CardRank, 0)
        for card in cards:
            self.__amounts_of_card_ranks[card.rank] += 1

        self.__GET_CATEGORIES_RANKS = {
            HandCategory.ROYAL_FLUSH: self.__get_royal_flush_rank,
            HandCategory.STRAIGHT_FLUSH: self.__get_straight_flush_rank,
            HandCategory.FOUR_OF_A_KIND: self.__get_four_of_a_kind_rank,
            HandCategory.FULL_HOUSE: self.__get_full_house_rank,
            HandCategory.FLUSH: self.__get_flush_rank,
            HandCategory.STRAIGHT: self.__get_straight_rank,
            HandCategory.THREE_OF_A_KIND: self.__get_three_of_kind_rank,
            HandCategory.TWO_PAIR: self.__get_two_pair_rank,
            HandCategory.ONE_PAIR: self.__get_one_pair_rank,
            HandCategory.HIGH_CARD: self.__get_high_card_rank
        }

        self.__rank = self.__generate_rank()

    @classmethod
    def from_strings(cls, list_of_strings):
        return cls(list(map(lambda s: Card.from_str(s), list_of_strings))) 

    def __str__(self):
        return '[' + reduce(lambda x, y: str(x) + ', ' + str(y), self.__cards) + ']'

    @property
    def category(self):
        return self.__rank[0]

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
        rank = sorted(rank, reverse=True)
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

    def __generate_rank(self):        
        for category, get_rank in self.__GET_CATEGORIES_RANKS.items():
            rank = get_rank()
            if not rank is None:
                return [category] + rank

    def __eq__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank == other.rank

    def __lt__(self, other):
        raise_if_not_same_type(self, other)
        return self.rank < other.rank