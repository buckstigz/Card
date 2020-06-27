from card import Card
from deck import Deck
import random

class Player:
    def __init__(self, name, hand):
        self._name = name
        self._hand = []

    def draw(self, Deck):
        self._hand.append(Deck.drawCard())
        return self

    def showHand(self):
        for card in self._hand:
            card.show()

new_deck = Deck()
bob = Player("Bob", [])
bob.draw(new_deck)
bob.showHand()
