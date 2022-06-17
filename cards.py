from enum import Enum


class CardSuit(Enum):
    HEARTS = '\u2665'
    DIAMONDS = '\u2666'
    CLUBS = '\u2663'
    SPADES = '\u2660'

    def __str__(self):
        return self.value