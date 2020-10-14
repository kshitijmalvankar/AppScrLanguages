# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:47:06 2020

@author: kshit
"""

from random import randint

print("This is a program to play the dice game")


#Take the input
guess = input("Please enter your guess (Even/ Odd)")


#Get the dice rolls
d1 = randint(1,6)
d2 = randint(1,6)


#Find out whether even or odd
total = d1+d2
if(total%2 == 0):
    ans = "even"
else:
    ans = "odd"
print(f"Dice Rolls: {d1} and {d2}. The total is {total} which is {ans}")

#Check with the user guess
if(guess.lower() == ans):
    print("You guessed right")
else:
    print("You guessed wrong")