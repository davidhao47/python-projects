
# coding: utf-8

# In[2]:

import random
from __future__ import print_function

class Player(object):
    def __init__(self,name,hand=[0,0],value = 0,bal=100,debt=0):
        self.name = name
        self.bal = bal
        self.hand = hand
        self.debt = debt
        self.value = value
        
    def checkBal(self):
        print (self.name + ", your current balance is: $",self.bal)
        
    def placeBet(self,amount):
        while True:
            if (amount > self.bal):
                print ("You don't have enough money!")
                amount = input("Try again: ")
                continue
            else: break
        while True:
            if (amount < 0):
                print ("You can't place a negative bet!")
                amount = input("Try again: ")
                continue
            else: break
        self.bal -=amount
        return amount
    
    def topUp(self):
        while True:
            amount = raw_input("How much would you like to inject?" )
            try: float(amount)
            except: print ("You must enter a number! Try again: ")
            else: 
                if float(amount)>0:
                    break
                else: 
                    print ("Cannot be negative! Try again: ")
                    continue
        self.bal  += float(amount)
        self.debt += float(amount)
    
class Dealer(object):
    
    def __init__(self,hand=[0,0],value=0):
        self.hand = hand
        self.value = value
        
    def dealerPlay(self):
        while valueHand(self.hand) < 17:
            hitMe(self.hand)
            
cardDeck = ["Spades A", "Spades 2", "Spades 3", "Spades 4", "Spades 5", "Spades 6",
             "Spades 7", "Spades 8" , "Spades 9", "Spades 10", "Spades Jack",
             "Spades Queen", "Spades King", "Hearts A", "Hearts 2", "Hearts 3", 
             "Hearts 4", "Hearts 5", "Hearts 6", "Hearts 7", "Hearts 8" , "Hearts 9",
             "Hearts 10", "Hearts Jack", "Hearts Queen", "Hearts King", "Clubs A", 
             "Clubs 2", "Clubs 3", "Clubs 4", "Clubs 5", "Clubs 6", "Clubs 7",
             "Clubs 8" , "Clubs 9", "Clubs 10", "Clubs Jack", "Clubs Queen",
             "Clubs King","Diamonds A", "Diamonds 2", "Diamonds 3", "Diamonds 4",
             "Diamonds 5", "Diamonds 6","Diamonds 7", "Diamonds 8" , "Diamonds 9",
             "Diamonds 10", "Diamonds Jack", "Diamonds Queen", "Diamonds King"]

#Spades (0 to 12), Hearts (13 to 25), Clubs (26 to 38), Diamonds (39 to 51)
# 1 or 11: 0,13,26,39
# 2: 1,14,27,40
# 3: 2,15,28,41
# 4: 3,16,29,42
# 5: 4,17,30,43
# 6: 5,18,31,44
# 7: 6,19,32,45
# 8: 7,20,33,46
# 9: 8,21,34,47
# 10: 9,10,11,12,22,23,24,25,35,36,37,38,48,49,50,51

def dealHand():
    first = random.randint(0,51)
    while True:
        second = random.randint(0,51)
        if first == second:
            second = random.randint(0,51)
        else: break 
    return [cardDeck[first],cardDeck[second]]

def valueHand(hand):
    sum = 0
    for num in range(0,len(hand)):
        #print cardDeck.index(hand[num])
        #print hand[num]
        
        if cardDeck.index(hand[num]) in (1,14,27,40):
            sum += 2
        elif cardDeck.index(hand[num]) in (2,15,28,41):
            sum += 3
        elif cardDeck.index(hand[num]) in (3,16,29,42):
            sum += 4
        elif cardDeck.index(hand[num]) in (4,17,30,43):
            sum += 5
        elif cardDeck.index(hand[num]) in (5,18,31,44):
            sum += 6
        elif cardDeck.index(hand[num]) in (6,19,32,45):
            sum += 7
        elif cardDeck.index(hand[num]) in (7,20,33,46):
            sum += 8
        elif cardDeck.index(hand[num]) in (8,21,34,47):
            sum += 9
        elif cardDeck.index(hand[num]) in (9,10,11,12,22,
                    23,24,25,35,36,37,38,48,49,50,51):
            sum += 10
        else: pass
    for num in range(0,len(hand)):
        if cardDeck.index(hand[num]) in (0,13,26,39):
            if (sum + 11) > 21:
                sum += 1
            else: sum +=11
    return sum
    
def hitMe(hand):
    
    hit = random.randint(0,51)
    for num in range(0,len(hand)):
        while hit == cardDeck.index(hand[num]):
            hit = random.randint(0,51)
    hand.append(cardDeck[hit])
    return
#################################################

print ("Welcome to David's Casino!")
name = raw_input("Please enter your name: ")

david = Player(name, dealHand())

while True:
    
    david.hand = dealHand()
    david.value = valueHand(david.hand)

    house = Dealer(dealHand())
    house.value = valueHand(house.hand)
    
    print ("")
    david.checkBal()
    x = raw_input("Would you like to increase your balance? y/n: ")
    if x == "y":
        david.topUp()
        print ("Your new balance is $",david.bal)
        print ("")
    else: pass

    while True:
        try: z = float(raw_input("Please place your bet: "))
        except: z = (raw_input("Invalid bet! Try again: "))
        else: break 

    betAmount = david.placeBet(z)

    print ("")
    print ("Blackjack will now begin.")
    print ("")

    print ("Your hand is: ",end="")
    for num in range(0,len(david.hand)):
        print (david.hand[num],end="  ")

    print ("")
    print ("The dealer's hand is showing: ", house.hand[0])
    
    ddchoice = raw_input("Would you like to double down? y/n: ")
    if ddchoice.lower() == "y":
        david.bal -= betAmount
        betAmount *= 2
        hitMe(david.hand)
        print ("Your hand is now: ",end="")
        for num in range(0,len(david.hand)):
            print (david.hand[num],end="  ")
        print ("")
        david.value = valueHand(david.hand)
    else: 
        while david.value < 21:
            choice = raw_input("Input 'y' for a hit, or 'n' to stay: ")
            if choice.lower() == 'y':
                hitMe(david.hand)
                print ("Your hand is now: ",end="")
                for num in range(0,len(david.hand)):
                    print (david.hand[num],end="  ")
                print ("")
                david.value = valueHand(david.hand)
            else: break 

    print ("")
    print ("The dealer reveals his hand: ",end="")
    for num in range(0,len(house.hand)):
            print (house.hand[num],end="  ")
    print ("")

    if house.value < 17:
        house.dealerPlay()
        print ("The dealer deals himself and finishes with: ", end="")
        for num in range(0,len(house.hand)):
            print (house.hand[num],end="  ")
        print ("")

    house.value = valueHand(house.hand)
    david.value = valueHand(david.hand)

    print ("The value of your hand is",david.value)
    print ("The value of the dealer's hand is", house.value)
    print ("")

    if (david.value > house.value and david.value <= 21) or         (house.value > 21 and david.value <= 21):
        print ("Thus, you win!")
        print ("$",betAmount, " goes to you.")
        david.bal += (betAmount*2)
    else:
        if david.value > 21:
            print ("You've gone bust!")
        print ("Thus, you lose!")
        print ("$",betAmount, " goes to the dealer.")
    
    print ("")
    playAgain = raw_input("Would you like to play again? y/n: ")
    if playAgain.lower() == "y":
        continue
    else: break
    
print("")
print("Your final balance is $", david.bal)
if david.bal > 100:
    print ("This represents a GAIN of $", (david.bal-100))
elif david.bal == 0: 
    print ("Sucks to be you, loser!")
elif david.bal < 100:
    print ("This represents a LOSS of $", (100-david.bal))

if david.debt > 0:
    print("You owe the casino $", david.debt)
    if (david.bal - david.debt) > 100:
        print("Your net winnings are $",(david.bal-100-david.debt))
    elif (david.bal - david.debt) < 100:
        print("Your net loss is $", (100 - (david.bal - david.debt)))
        
print ("")
print ("Goodbye!")


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



