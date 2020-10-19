# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:43:21 2020

@author: kshit
"""
#Initialize count to 0
count = 0    
while count < 3:
    
    #Take the inputs
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    
    
    #Compare the inputs
    if username == "aladdin" and password == "open_sesame":
        print("Login successful")
        break  #Exit the loop
    else:
        count = count +1
        print("Invalid login. Only",3-count,"attemps left")
        
if(count == 3):
    print("Too many failed attempts")
    exit()