# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:15:01 2020

@author: kshit
"""

print("This is the program to check whether username is valid")


#Take the input from the user
username = input("Enter your username: ")

#conditional statements
if(4 <= len(username) <= 8 and username[0].islower() and username.isalnum()):
    print("Valid Username")
else:
    if(len(username) < 4):
        print("Invalid username : The username is too short")
    elif(len(username) > 8):
        print("Invalid username : The username is too long")
        
    if not(username[0].islower()):
        print("Invalid username : The username does not start with lower case")
    if not(username.isalnum()):
        print("Invalid username : The username can only contain alphanumeric characters")
    
    
    
    
