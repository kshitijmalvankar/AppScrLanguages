# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:42:27 2020

@author: kshit
"""

from random import choice
quick_pick=[]

#List with all numbers
main_list = list(range(1, 48)) 

#Repeat 6 times for 6 picks
for x in range(0, 6):
    number= choice(main_list )
    main_list.remove(number) #remove the number
    quick_pick.append(number) #Append to the list
quick_pick.sort();
print("Your picks are:",quick_pick)