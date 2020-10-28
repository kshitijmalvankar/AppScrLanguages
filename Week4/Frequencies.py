# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:01:32 2020

@author: kshit
"""

from string import ascii_lowercase

#Setting the initial text
paragraph = '''Python is fun '''


#List with frequencies for each letter set to 0
frequencies = [0]*26

#using lower() to check for both upper case and lower case
for ch in paragraph.lower():
    if ch.isalpha():
        index = ascii_lowercase.find(ch) #index of the alphabet
        frequencies[index] += 1 #incrementing the frequency of the alphabet
    
#printing the letter and its frequency
for i in range(26):
    print(f"The letter {ascii_lowercase[i]} appeared {frequencies[i]} times.")

max_frq = frequencies.index(max(frequencies))
print(f"The letter that appeared the most is {ascii_lowercase[max_frq]}")