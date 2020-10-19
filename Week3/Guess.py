# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 12:05:58 2020

@author: kshit
"""

from random import randint

choice = "y"


while choice == "y":
    print("Im guessing a number between 1 and 100. Try to guess it!")
    count = 0
    answer = randint(1,100)
    
    while count < 10:
        guess = int(input("Please enter your guess: "))
        if guess == answer:
            print("The answer was",answer,"and you guessed it!")
            break
        elif guess < answer:
            count = count + 1
            print("Too Low. Please try again, you have",10-count,"attempts left")
        elif guess > answer:
            count = count + 1
            print("Too High. Please try again, you have",10-count,"attempts left")
    else:
        print("You have exhausted all your attempts. The answer was", answer)
    
    choice = input("Do you wante to play again? (y/n)").lower()