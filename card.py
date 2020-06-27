class Card:
    def __init__(self, suit, number):
        self._suit = suit
        self._number = number
##        self._value = value

    # __repr__ stands for representation and allows textual representation
    # rather than the pointer to place in stack to be printed
    def __repr__(self):
        return self._number + " of " + self._suit
##    + " points: " + str(self._value)
   
    
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, suit):
        if suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            self._suit = suit.upper()
        else:
            print("That's not a valid suit!")
            
    @property
    def number(self):
        return self._number
    
    @number.setter
    # used the number setter to also set the point value of the cards
    def number(self, number):
        if number in [str(n) for n in range(2, 11)] + ["King", "Queen", "Jack", "Ace"]:
            self._number = number.upper()   
        else:
            print("That's not a valid card number!")


    def show(self):
        print("{} of {}".format(self.number, self.suit))
        
##        if number in [str(n) for n in range(2, 11)]:
##            self._value = number
##        elif number in ["King", "Queen", "Jack", "Ace"]:
##            self._value = 10
##        else:
##            print("No points avaliable!")
##
##    @property
##    def value(self):
##        return self._value
##
##    @number.setter
##    def value(self, number):
##        if number in ["K", "Q", "J", "A"]:
##           self._value = 10
##        else:
##            self._value = int(number)
    

    






