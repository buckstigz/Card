from card import Card
import random


class Deck:
    # create an empty list, each index will be a Card object
    def __init__(self):
        self._cards = []
        self.populate()
        random.shuffle(self._cards)

##    def __repr__(self):
##        return repr(self._cards)
##    
    def __iter__(self):
        return CardIterator(self)

    def populate(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        numbers = [str(n) for n in list(range(2, 11)) + ["Ace", "King", "Queen", "Jack"]]
        self._cards = [ Card(s, n) for n in numbers for s in suits ]

##    def __len__(self):
##        len(self._cards)

    def show(self):
        for c in self._cards:
            c.show()

    def drawCard(self):
        return self._cards.pop()

    def remove(self, card):
        if card in self._cards:
            self._cards.remove(card)
            return True
        else:
            return False

    def isEmpty(self):
        return (len(self._cards) == 0)
        
class CardIterator:
    def __init__(self, my_deck):
        self._my_deck = my_deck
        self._index = 0

    def __next__(self):
        #returns the next value from my_deck object's list
        if self._index < (len(self._my_deck._cards)):
            if self._index < (len(self._my_deck._cards)):
                result = (self._my_deck._cards[self._index])
                self._index += 1
            return result
        raise StopIteration




## Above is list comprehension. This means that self._cards is set to [ a list ] of Card
## objects containing every combination of s, n looping through 'for s in suits' and
## 'for n in numbers'.
##
##cards = []                                      #Create an emtpty list of cards
##for suit in suits:                              # For each suit...
##    for number in numbers:                      # For each number...
##        # Create a new Card object and add it to the list
##        cards.append( Card(suit, number) )
##self._cards = cards                             # Then point self._cards at this list
##
## Above is a nested loop - in order for populate to generate a list of cards you have
## combine the two lists in populat so that each suit for each number creates a card
## object
