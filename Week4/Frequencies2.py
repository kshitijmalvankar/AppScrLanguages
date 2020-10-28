# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 10:18:54 2020

@author: kshit
"""

from string import ascii_lowercase


paragraph = "aaa bbb ccc jadghfkjahgjkahd"

frequencies = [paragraph.lower().count(x) for x in ascii_lowercase]


#printing the letter and its frequency
for i in range(26):
    print(f"The letter {ascii_lowercase[i]} appeared {frequencies[i]} times.")

max_frq = frequencies.index(max(frequencies))
print(f"The letter that appeared the most is {ascii_lowercase[max_frq]}")