from card import Card
from deck import Deck
import random

class Player:

    def __init__(self, name):
        self._name = name
        self._hand = []
        self.value = 0

    def draw(self, Deck):
        self._hand.append(Deck.drawCard())
##        self.value += value[card._number]
        return self

    def showHand(self):
        for c in self._hand:
            c.show()

    def discard(self):
        return self._hand.pop()
##    
##    def cardValue(self):
##        if self._hand in ("J", "Q", "K"):
##            print(int(10))
##        elif self._hand in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
##            print(int(self._hand))
##        elif "A" in self._hand:
##            print("\n" + str(self._hand))
##            num = input("Do you want this Ace to be High or Low?")
##            while num !="High" or num !="Low":
##                if num == "High":
##                    return int(11)
##                elif num == "Low":
##                    return int(1)
# above does work to an extent....




        
##        if self._hand in [str(n) for n in range(2, 11)]:
##            self._value = int(self._hand[:1])
##        elif self._hand in ["King", "Queen", "Jack", "Ace"]:
##            self._value = int(10)
##        else:
##            print("No points avaliable!")

deck1 = Deck()
sabina = Player("Sabina")
card1 = sabina.draw(deck1)
sabina.showHand()






##deck1 = Deck()
##sabina = Player("Sabina")
##for i in range(2):
##    sabina.draw(deck1)
##
##print(f'\nThe {len(sabina._hand)} cards in {sabina._name}\'s hand: ')
##sabina.showHand()
##
##print('\nDiscarded: ')
##sabina.discard().show()
##
##print(f'\nThe {len(sabina._hand)} cards in {sabina._name}\'s hand: ')
##sabina.showHand()






    



