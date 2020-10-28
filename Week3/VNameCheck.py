# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:20:33 2020

@author: kshit
"""


choice = "y"
while choice =="y":

    print("Variable name check!")
    
    vname = input("Please enter the variable you wish to use: ")
    
    for ch in vname:
        if not ch.isalnum() and ch!= "_":
            print("Variable is not valid")
            break
    else:
        print("The variable name you chose is valid!")
    choice = input("Do you wiah to continue? (y/n)")