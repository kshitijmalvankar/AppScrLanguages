# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:25:08 2020

@author: kshit
"""

#Code for Lotto Quick Pick Part 1

from random import randint

#Empty List
quick_pick = []

#Check whether there are less than 6 numbers in the list
while len(quick_pick) < 6:
    number = randint(1, 48)
    
    print("You picked",number)
    #Add if the number is not present in the list
    if not number in quick_pick:
        quick_pick.append(number)
    
quick_pick.sort();
print(quick_pick)