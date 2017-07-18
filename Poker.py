from random import randint

class Card (object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def printCard(self):
        if self.value == 1:
            print "Ace of",self.suit
        elif self.value == 11:
            print "Jack of",self.suit
        elif self.value == 12:
            print "Queen of", self.suit
        elif self.value == 13:
            print "King of", self.suit 
        else:
            print self.value, "of", self.suit
            
    
class Player(object):
    def __init__(self,name,hand=[],bal=500):
        self.name = name
        self.hand = hand
        self.bal = bal

    def checkBal(self):
        print self.name + ", your current balance is: $",self.bal
        
    def addCard(self):
        self.hand.append(dealCard())
        
    def displayHand(self):
        for card in self.hand:
            card.printCard()
        
    def placeBet(self,amount):
        while True:
            if (amount > self.bal):
                print "You don't have enough money!"
                amount = input("Try again: ")
                continue
            else: break
        while True:
            if (amount < 0):
                print "You can't place a negative bet!"
                amount = input("Try again: ")
                continue
            else: break
        self.bal -=amount
        return amount
        
###############################################################
        
def createDeck():
    deck = []
    for tempsuit in ["Spades","Hearts","Diamonds","Clubs"]:
        for tempnumb in range(1,14):
            tempcard = Card(tempsuit,tempnumb) 
            deck.append(tempcard)
    return deck

def displayDeck():
    for tempcard in deck:
        print tempcard.value,"of",tempcard.suit
        
def dealCard():
    dealtCard = deck.pop(randint(0,len(deck)))
    return dealtCard

deck = createDeck()
david = Player("David")
print david.name
david.addCard()
david.addCard()
david.displayHand()
    
    

#class Hearts8(Card):
#    def __init__(self,suit,value):
#        Card.__init__(self,suit,value)
#
#x = Hearts8("Hearts",8)
#
#x.printCard()
