# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:16:38 2020

@author: kshit
"""

from random import randint

d1 = randint(1,6)
d2 = randint(1,6)

total = d1+d2

if(total == 7 or total == 11):
    print(f"You rolled {d1} and {d2} and your total is {total}")
    print("You Win")
elif total ==2 or total ==3 or total == 12:
    print(f"You rolled {d1} and {d2} and your total is {total}")
    print("You Lose")
else:
    point = total;
    total = 0
    while total != 7 and total != point:
        d1 = randint(1,6)
        d2 = randint(1,6)
        total = d1+d2
        print(f"You rolled {d1} and {d2} and your total is {total}")
    else:
        if total == point:
            
            print("You Win")
        elif total == 7:
            
            print("You Lose")
    
        
    