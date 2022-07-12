from card import Card, CardSuit, CardRank, raise_if_not_same_type
from functools import reduce

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

    @classmethod
    def from_strings(cls, list_of_strings):
        return cls(list(map(lambda s: Card.from_str(s), list_of_strings))) 

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