from card import Card
from deck import Deck
from player import Player
import random

class Dealer(Player):
    def __init__(self, name):
        self._name = name
        self._hand = []
        self._isBust = False

    def showHand(self):
        for card in self._hand:
            print(card),
        print

    def hit(self, Deck):
        print("Hitting...")
        self._hand.append(Deck.drawCard())
        return self._hand

    def stand(self):
        print(self.getValue())

    def checkBust(self):
        if self.getValue() > 21:
            self.isBust = True
            print("%s is bust!") % self._name
        else:
            self.stand()
##
d = Deck()
deal = Dealer("Dealer")
sabina = Player("Sabina")
for i in range(2):
    deal.hit(d)
deal.showHand()
deal.stand()
