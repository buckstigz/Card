import random      

class Card:
    """
    The Card class represents a single playing card, contains functions
    to properly print the card object.
    """
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.value = 0
##
##        if number in ["King", "Queen", "Jack"]:
##            self.value = 10
##        elif number == "Ace":
##            self.value = 1
##        else:
##            self.value = number

    def __repr__(self):
        return self.number + " of " + self.suit

    def show(self):
        print("{} of {}".format(self.number, self.suit))

class Deck:
    """
    The Deck Class creates a list of each card object assigning both it's
    suit and it's number value in the populating of the list. Also contains
    functions to show the card (overriding the method in the Card class),
    to remove a select card, to draw a card out, and to see whether the
    deck (list) is empty.
    """
    def __init__(self):
        self.cards = []
        self.populate()
        random.shuffle(self.cards)

    def populate(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10] + ["Ace", "King", "Queen", "Jack"]
        self.cards = [Card(s, n) for n in numbers for s in suits]

    def show(self):
        for card in self.cards:
            card.show()

    def drawCard(self):
        return self.cards.pop()

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def isEmpty(self):
        return (len(self.card == 0))

class Player:
    """
    The Player class could also be known as the 'hand'. Overrides the show
    method to print the card, the points method allows you to assign points
    based on the card number, draw adds a card from the Deck class to the
    Player object, and discard removes a card from the Player object.
    """
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.value = 0

    def show(self):
        for card in self.cards:
            card.show()

    def points(self):
        self.value = 0
        aces = 0

        for card in self.cards:
            if isinstance(card.number, int):
                self.value += card.number
            elif card.number == "Ace":
                self.value += 1
                aces += 1
            elif isinstance(card.number, str):
                self.value += 10
        while self.value <= 11 and aces > 0:
            self.value += 10
            aces -= 1

    def discard(self):
        return self.cards.pop()

    def draw(self, Deck):
        self.cards.append(Deck.drawCard())
        self.points()

class Chips:
    """
    The Chips class controls the betting, a function of the program that
    has not yet been implemented.
    """
    def __init__(self):
        self.total = 100
        self.bet = 0

    def winBet(self):
        self.total += self.bet

    def loseBet(self):
        self.total -= self.bet

    def push(self):
        self.total = self.total

def takeBet(C):
    C.bet = int(input("Place your bets here: "))
    if C.total == 0 and C.bet > C.total:
        raise Exception("No Money, No Bet - You Lose!")
    while C.bet > C.total or C.bet < 0 or not (isinstance(C.bet, int)):
        C.bet = int(input("Place your bets here: "))

def hit(D, Player):
    P.draw(D)

def hitOrStand(Dealer, P):
    while True:
        hit_stand = input("Do you want to hit or stand? ").lower()
        if hit_stand == "hit" or hit_stand == "h":
            hit(D, P)
        else:
            print(P.name + " stands, DEALER is playing")
            return False
        return True

def showAll(P, Dealer):
    print(P.name + " cards: ")
    print(P.show())
    print(Dealer.name + " cards: ")
    print(Dealer.show())

##def bustOrWin(P):
##    if P.value <= 21:
##        return
##    elif P.value > 21:
##        print(P.name + " is Bust!")
    

def playerBust(C, P):
    C.loseBet()
    print(P.name + " Bust!")
    
def playerWin(C, P):
    C.winBet()
    print(P.name + " Wins!")

def dealerBust(C, Dealer):
    C.loseBet()
    print(Dealer.name + " Bust!")
    
def dealerWin(C, Dealer):
    C.winBet()
    print(Dealer.name + " Wins!")

def push(C, P, Dealer):
    print("Push")
    C.push()

def play_again():
    return input("Another Game?").lower().startswith("y")


win = 0
lose = 0
tie = 0
print("Welcome to BlackJack")

C = Chips()
D = Deck()
P = Player(input("Please enter your name: "))
Dealer = Player("Dealer")

##P.draw(D)
##P.show()
##print(P.value)
        
for i in range(2):
    P.draw(D)
for i in range(2):
    Dealer.draw(D)
print(P.name + "'s hand:")
P.show()
print(P.value)
print("\n")
print("Dealer's hand: ")
Dealer.show()
print(Dealer.value)
print("\n")

while P.value < 21:
    hos = input("Hit or Stick? ")
    print("\n")
    if hos == "Hit":
        print(P.name + "'s New Hand: ")
        P.draw(D)
        P.show()
        print(P.name + "'s points: ")
        print(P.value)
    if hos == "Stick" and Dealer.value < 21:
        print("Dealer playing...")
        break
if P.value == 21:
        print(P.name + " Wins!")
if P.value > 21:
    print(P.name + " is Bust")
    print("\n")
    
if Dealer.value < 21:
    Dealer.draw(D)
    print("Dealer's hand: ")
    Dealer.show()
    print(Dealer.value)
    print("\n")
if Dealer.value == 21:
    print("Dealer wins")
elif Dealer.value > 21:
        print(Dealer.name + " is Bust")
elif P.value < 21:
    hos = input("Hit or Stick? ")
    print("\n")
    if hos == "Hit":
        print(P.name + "'s New Hand: ")
        P.draw(D)
        P.show()
        print(P.name + "'s points: ")
        print(P.value)
    if hos == "Stick" and Dealer.value < 21:
        print("Dealer playing...")
        Dealer.draw(D)
        print("Dealer's Hand: ")
        Dealer.show()
        print(Dealer.value)
        if Dealer.value == 21:
            print(Dealer.name + " Wins!")
        elif Dealer.value > 21:
            print(Dealer.name + " is Bust")
            print("\n")

if Dealer.value < 21:
    Dealer.draw(D)
    print("Dealer's hand: ")
    Dealer.show()
    print(Dealer.value)
    print("\n")
if Dealer.value == 21:
    print("Dealer wins")
elif Dealer.value > 21:
        print(Dealer.name + " is Bust")
elif P.value < 21:
    hos = input("Hit or Stick? ")
    print("\n")
    if hos == "Hit":
        print(P.name + "'s New Hand: ")
        P.draw(D)
        P.show()
        print(P.name + "'s points: ")
        print(P.value)
    if hos == "Stick" and Dealer.value < 21:
        print("Dealer playing...")
        Dealer.draw(D)
        print("Dealer's Hand: ")
        Dealer.show()
        print(Dealer.value)
        if Dealer.value == 21:
            print(Dealer.name + " Wins!")
        elif Dealer.value > 21:
            print(Dealer.name + " is Bust.")
            print("\n")
    
##if Dealer.value < 21:
##    Dealer.draw(D)
##    print("\n")
##    print("Dealer's hand: ")
##    Dealer.show()
##    print(Dealer.value)
##elif Dealer.value == 21:
##    print("\n")
##    print("Dealer wins")
##elif Dealer.value > 21:
##    print(P.name + " Wins!")
##elif P.value > 21:
##    print(P.name + " is Bust!")
##
##if Dealer.value == 21:
##    print("Dealer Wins.")
##elif Dealer.value > 21:
##    print(P.name + " Wins!")
##
##if P.value < 21:
##    hos = input("Hit or Stick?")
##    print("\n")
##elif P.value == 21:
##    print(P.name + " Wins!")
##if hos == "Hit":
##    print(P.name + "'s New Hand: ")
##    P.draw(D)
##    P.show()
##    print(P.name + "'s points: ")
##    print(P.value)
##elif hos == "Stick" and Dealer.value < 21:
##    print("Dealer playing...")
##    if Dealer.value < 21:
##        Dealer.draw(D)
##        print("Dealer's hand: ")
##        Dealer.show()
##        print(Dealer.value)
##    elif Dealer.value == 21:
##        print("Dealer wins")
##    elif Dealer.value > 21:
##        print(P.name + " Wins!")
##elif P.value > 21:
##    print(P.name + " is Bust!")

    

    



##while hitOrStand(Dealer, P):
##    if P.value > 21:
##        showAll(P, Dealer)
##        playerBust(C, P)
##        lose += 1
##        break
##if P.value <= 21:
##    while Dealer.value < 17:
##        hit(D, Dealer)
##    showAll(P, Dealer)
##if Dealer.value > 21:
##    dealerBust(C, Dealer)
##    win += win
##elif Dealer.value > P.value:
##    dealerWin(C, Dealer)
##    lose += lose
##elif Dealer.value < P.value:
##    playerWins(C, P)
##    win += win
##else:
##    push(C, P, Dealer)
##    tie += tie
            

                                                                                           


## After this ask Hit or Stick (we will ignore betting for the simple first
## first version. If stick, go to an if > 21 draw for Dealer. If hit draw
## draw for player. Require a function to check value against 21 after EVERY
## draw including the first 2 draws. Play until one goes bust.
## Look through all the functions and find if any fit in here!



##    while hitOrStand(D, P):
##        showAll(P, Dealer)
##        if P > 21


