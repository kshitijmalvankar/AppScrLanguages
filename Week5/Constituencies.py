# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:50:34 2020

@author: kshit
"""

constituencies_list = []
seats_list = []
headings= []

with open("constituencies.csv") as constituencies:
    headings = constituencies.readline().split(",")
 
 
    for line in constituencies:
        name, seats = line.split(",")
        constituencies_list.append(name)
        seats_list.append(int(seats.strip("\n")))



print(f"The number of constituencies:{len(constituencies_list)}")
print(f"The total number of seats: {sum(seats_list)}")
print(f"The mean number of seats per constituency {sum(seats_list )/len(constituencies_list)}")




sorted_list = sorted(seats_list)
if len(sorted_list) %2 == 0:
    med1 = sorted_list[(int(len(sorted_list)/2))]
    med2 = sorted_list[(int(len(sorted_list)/2)-1)]
    median = (med1 +med2)/2
else:
    median = sorted_list[(int(len(sorted_list)/2))]
    
print(f"The median is {median}")

values =sorted(list(set(seats_list)))
frequencies = [ seats_list.count(value) for value in values ]
print("Type     Constituencies")
for num_seats,frequency in zip(values, frequencies):
    print(f"{num_seats}-Seater {frequency}")
mode_ind = frequencies.index(max(frequencies))
print(f"The mode is {values[mode_ind]}")