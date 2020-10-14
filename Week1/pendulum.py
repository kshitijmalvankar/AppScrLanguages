# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:37:49 2020

@author: kshit
"""



#program to get period (time) for a Pendulum
#A00268796
from math import sqrt, pi

print("This program calculates the time period of a pendulum")

length = int(input("Input the length of the pendulum in metres: "))

time = 2 * pi * (sqrt(length/9.81))

print(f"The time is {time:.2f} seconds")