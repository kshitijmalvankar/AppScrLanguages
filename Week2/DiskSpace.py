# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:38:30 2020

@author: kshit
"""

print("This is a program to calculate the percentage of free space :")


#Take the input(Total space and used space) from the user
total_space = int(input("Please enter the total Disk space available:"))
used_space = int(input("Please enter the used Disk space:"))

#calculate the percent of free space
percent_free = 100 * (total_space - used_space)/total_space


#conditional statements
if(used_space > total_space):
    print("Invalid inut")
else:
    if(0 < percent_free <5):
        print(f"Percent of free space is {percent_free:.1f}")
        print("Warning low disk spcae")
    elif(percent_free == 0):
        print(f"Percent of free space is {percent_free:.1f}")
        print("Warning. System will crash.")
    else:
        print(f"Percent of free space is {percent_free:.1f}")
        print("System has sufficient space")