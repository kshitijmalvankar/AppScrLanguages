# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:25:29 2020

@author: kshit
"""



#program to convert hogsheads to litres
#A00268796

print("This program converts Imperial hogsheads to Litres")

#hogsheads input converted to float
hogshead = float(input("Enter the imperial Hogsheads:"))


#litres = hogs*barrels*gallons*litres
litres = hogshead * 2.0 * 36.0 * 4.54609


#output
print(f"Equivalent metric volume is {litres:.1f} litres")