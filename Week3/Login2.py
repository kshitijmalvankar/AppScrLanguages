# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:50:47 2020

@author: kshit
"""

username = input("Please enter your username: ")
password = input("Please enter your password: ")

while username != "aladdin" and password != "open_sesame":
    print("Invalid Login. Please try again")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

print("Login successful")