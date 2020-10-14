# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:48:25 2020

@author: kshit
"""

fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")

fname = fname.lower()
lname = lname.lower()

username = fname[0] + lname

print("username is",username)