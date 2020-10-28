# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:32:39 2020

@author: kshit
"""

#Code for Lotto Quick Pick part 3

from random import  shuffle

#Creatinf list with numbers 1 - 47
main_list = list(range(1,48))
quick_pick = []

#shuffling the list
shuffle(main_list)


#Getting the first 6 from the shuffled list
quick_pick = main_list[:6]
quick_pick.sort()

print("Your picks are: ",quick_pick)
