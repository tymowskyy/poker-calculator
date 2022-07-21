from itertools import combinations
from card import Card
from hand import Hand, HandCategory


class Game:

    def __init__(self, pocket_cards, community_cards):
        if len(pocket_cards) != 2:
            raise ValueError('lenght of pocket_cards must be 2')
        if len(community_cards) < 0 or len(community_cards) > 5:
            raise ValueError('lenght of community_cards must be between 0 and 5')

        self.__n_cards_left = 5 - len(community_cards)
        self.__pocket_cards = sorted(pocket_cards, reverse=True)
        self.__community_cards = sorted(community_cards, reverse=True)
        self.__other_cards = self.__get_other_cards()
        if len(self.__other_cards) != len(Card.get_all_cards()) - len(pocket_cards) - len(community_cards):
            raise ValueError('cards in pocket_cards and community_cards must be uniqe')


    def __get_other_cards(self):
        all_cards = Card.get_all_cards()
        return list(set(all_cards) - set(self.__pocket_cards) - set(self.__community_cards))

    @property
    def pocket_cards(self):
        return self.__pocket_cards

    @property
    def community_cards(self):
        return self.__community_cards

    def get_combinations(self):
        combos = []
        for cards_left in combinations(self.__other_cards, self.__n_cards_left):
            combos.append(cards_left)
        return combos   