# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:46:49 2020

@author: kshit
"""

from string import ascii_lowercase
choice = "y"
while choice == "y":
    print("AtBash Cipher!")
    
    plaintxt = input("Please enter some plain text to be ciphered: ").lower()
    ciphertxt = ""
    
    for c in plaintxt:
        index = ascii_lowercase.index(c)
        ciphertxt+=ascii_lowercase[25-index]
    else:
        print(f"The ciphered version of {plaintxt} is {ciphertxt}")
    
    
    choice = input("Do you wish to continue? (y/n)")
