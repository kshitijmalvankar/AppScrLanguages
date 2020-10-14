# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:48:25 2020

@author: kshit
"""



#program to convert hogsheads to litres
#A00268796

#Take all inputs: First Name, Last name, Mother's maiden name, Birthplace
fname = input("First name: ")
lname = input("Last name: ")
mname = input("Mother's Maiden name: ")
birthplace = input("Birthplace name: ")


#Starwars first name
sw_fname = fname[:3] +lname[:2]

#Starwars last name
sw_lname = mname[:2]+birthplace[:3]

#Combining both
swname = sw_fname + " "+sw_lname
swname = swname.title()
print(swname)