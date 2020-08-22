#!/usr/bin/env python
"""Demo the Python data model."""
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """A standard card deck."""
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "clubs diamonds hearts spades".split()
    suit_values = {}
    for i in range(len(suits)):
        suit_values[suits[i]] = i

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    """Return position in deck, spades high."""
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]


def main():
    """The whole shootin' match."""
    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high):
        print(card)


if __name__ == "__main__":
    main()
