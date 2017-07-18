
# coding: utf-8

# In[ ]:

from __future__ import print_function
from IPython.display import clear_output

def verify():
    global max_step
    check = False
    if (a1+a2+a3== 3 or a1+a2+a3==6 or a1+b2+c3 == 3 or a1+b2+c3 == 6 or 
        a1+b1+c1 == 3 or a1+b1+c1 == 6 or b2+b3+b1 == 3 or b2+b3+b1 == 6 or 
        c1+c2+c3 == 3 or c1+c2+c3 == 6 or a3+b2+c1 == 3 or a3+b2+c1 == 6 or 
        a2+b2+c2 == 3 or a2+b2+c2 == 6 or a2+b2+c2 == 3 or a2+b2+c2 == 6):
            check = True
    elif count == 9:
         max_step = True
    return check

def display():
    
# 1 = X, 2 = O
    
    print ("      A     B     C")
    print ("    _________________ ")
    print ("   |     |     |     |")
    
    if a1 == 1: print ("1  |  X  |",end="")
    elif a1 == 2: print ("1  |  O  |",end="")
    else: print ("1  |     |",end="")
        
    if b1 == 1: print ("  X  |",end="")
    elif b1 == 2: print ("  O  |",end="")
    else: print ("     |",end="")
        
    if c1 == 1: print ("  X  |")
    elif c1 == 2: print ("  O  |")
    else: print ("     |")
    
    print ("   |_____|_____|_____|")
    print ("   |     |     |     |")
 
    if a2 == 1: print ("2  |  X  |",end="")
    elif a2 == 2: print ("2  |  O  |",end="")
    else: print ("2  |     |",end="")
        
    if b2 == 1: print ("  X  |",end="")
    elif b2 == 2: print ("  O  |",end="")
    else: print ("     |",end="")
        
    if c2 == 1: print ("  X  |")
    elif c2 == 2: print ("  O  |")
    else: print ("     |")
    
    print ("   |_____|_____|_____|")
    print ("   |     |     |     |")
    
    if a3 == 1: print ("3  |  X  |",end="")
    elif a3 == 2: print ("3  |  O  |",end="")
    else: print ("3  |     |",end="")
        
    if b3 == 1: print ("  X  |",end="")
    elif b3 == 2: print ("  O  |",end="")
    else: print ("     |",end="")
        
    if c3 == 1: print ("  X  |")
    elif c3 == 2: print ("  O  |")
    else: print ("     |")
        
    print ("   |_____|_____|_____|")
    
def input():
    global x, count, a1, a2, a3, b1, b2, b3, c1, c2, c3
       
    if x == 1: x = 2
    else: x = 1
    s = "Player {a}, enter your choice: ".format(a=x)
    temp = raw_input(s)

    while (not(temp.lower()=="a1" or temp.lower()== "a2" or temp.lower()=="a3" 
           or temp.lower()=="b1" or temp.lower()== "b2" or temp.lower()=="b3" 
           or temp.lower()=="c1" or temp.lower()== "c2" or temp.lower()=="c3")):
            print("Please input a valid position.")
            s = "Player {a}, enter your choice: ".format(a=x)
            temp = raw_input(s)
            
    while ((temp.lower()=="a1" and a1!=99) or (temp.lower()== "a2" and a2!=99)
           or (temp.lower()=="a3" and a3!=99) or (temp.lower()=="b1" and b1!=99)
           or (temp.lower()=="b2" and b2!=99) or (temp.lower()=="b3" and b3!=99) 
           or (temp.lower()=="c1" and c1!=99) or (temp.lower()=="c2" and c2!=99)
           or (temp.lower()=="c3" and c3!=99)):
            print("Please input a valid position.")
            s = "Player {a}, enter your choice: ".format(a=x)
            temp = raw_input(s)
    
    if temp.lower() == "a1" and a1 != 99:   a1=x
    elif temp.lower() == "a2" and a2 != 99: a2=x
    elif temp.lower() == "a3" and a3 != 99: a3=x
    elif temp.lower() == "b1" and b1 != 99: b1=x
    elif temp.lower() == "b2" and b2 != 99: b2=x
    elif temp.lower() == "b3" and b3 != 99: b3=x
    elif temp.lower() == "c1" and c1 != 99: c1=x
    elif temp.lower() == "c2" and c2 != 99: c2=x
    elif temp.lower() == "c3" and c3 == 99: c3=x
    
    if temp.lower() == "a1" and a1 == 99:   a1=x
    elif temp.lower() == "a2" and a2 == 99: a2=x
    elif temp.lower() == "a3" and a3 == 99: a3=x
    elif temp.lower() == "b1" and b1 == 99: b1=x
    elif temp.lower() == "b2" and b2 == 99: b2=x
    elif temp.lower() == "b3" and b3 == 99: b3=x
    elif temp.lower() == "c1" and c1 == 99: c1=x
    elif temp.lower() == "c2" and c2 == 99: c2=x
    elif temp.lower() == "c3" and c3 == 99: c3=x
    else: 
        print ("Error 404")
    count +=1
    
a1 = 99
a2 = 99
a3 = 99
b1 = 99
b2 = 99
b3 = 99
c1 = 99
c2 = 99
c3 = 99
count = 0
x = 2
max_step = False

while verify()==False:
    clear_output()
    display()
    input()

display()
if max_step == True:
    print("The game has ended in a draw.")
else: print ("The game has ended. Player ",x," is the winner.")


# In[ ]:

a1


# ### 

# In[10]:

import re

def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print 'Searching the phrase using the re check: %r' %pattern
        print re.findall(pattern,phrase)
        print '\n'

test_phrase = 'hello iiiii hello i what is hello iii hello 2 am a bitch'

test_patterns = [ 'hello 2i*',     # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                ]

multi_re_find(test_patterns,test_phrase)


# In[ ]:



