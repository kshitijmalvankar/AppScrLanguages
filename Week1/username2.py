# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:30:53 2020

@author: kshit
"""
#generating a user name from full name
fullname = input("Please enter a full name: ")
name = fullname.split(" ",1)

username = (name[0]+name[1][0]).lower()
print("Username:",username)