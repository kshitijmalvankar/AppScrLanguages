# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:52:02 2020

@author: kshit
"""

from random import randint
choice = "y"
while choice == "y":
    print("Get 3 even rolls to wind!")
    counter = 0
    
    for i in range(5):
        print("Press Enter to roll")
        input()
        roll = randint(1,6)
        if roll%2 ==0:
            counter+=1
        print(f"You rolled a {roll}")
        
    if counter >=3:
        print("You Win")
    else:
        print("You lose")
    choice = input("Do you want to continue?")