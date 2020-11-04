# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 09:43:59 2020

@author: kshit
"""
from math import sqrt
countries_list = []
region_list = []
gnp_list = []
birth_rate_list = []
life_males_list = []
life_females_list= []
headers = []
 
try:
 with open("life.csv") as datafile:
     headers=datafile.readline()
     for line in datafile:      
        country,region,gnp,birth_rate, life_males, life_females= line.split(",")
        countries_list.append(country)
        region_list.append(int(region))
        try:
            gnp_list.append(int(gnp)) # watch out for the GNP - what if it's *
        except ValueError:
            print("The value cannot be converted to an integer. Default value used.")
            gnp_list.append(0)
        
        birth_rate_list.append(float(birth_rate))
        life_males_list.append(float(life_males))
        life_females_list.append(float(life_females))

except FileNotFoundError as fnf_error:
    print("The file you're trying to open cannot be found",fnf_error)

except ValueError as value_error:
    print("The value is incorrect",value_error)
   

#p1
print("number of countries",len(countries_list))
#p2
print ("number of regions", len(sorted(list(set(region_list)))))

#p3

print("Average number of countries per region", int(len(set(countries_list))/len(set(region_list))))

#4
values =sorted(list(set(region_list)))
frequencies = [ region_list.count(value) for value in values ]
mode_ind = frequencies.index(max(frequencies))
print(f"The mode is region {values[mode_ind]}")


#5 Mean GNP 
print("The Mean GNP per country is",sum(gnp_list)/len(gnp_list))

#6
sorted_list = sorted(gnp_list)
if len(sorted_list) %2 == 0:
    med1 = sorted_list[(int(len(sorted_list)/2))]
    med2 = sorted_list[(int(len(sorted_list)/2)-1)]
    median = (med1 +med2)/2
else:
    median = sorted_list[(int(len(sorted_list)/2))]

print("Median GNP per country:", median)


rangeGnp = max(gnp_list) - min(gnp_list)
print("The range for the GNP is", rangeGnp)


gnp_mean=sum(gnp_list)/len(gnp_list)
variance=sum( pow (x-gnp_mean,2)for x in gnp_list)/len(gnp_list)
standard_deviation=sqrt(variance)
squared_deviations = [ (x - gnp_mean) ** 2 for x in gnp_list ]
print("The standard deviation for the GNP values is: ",standard_deviation)




mean_x = sum(birth_rate_list)/len(birth_rate_list)
mean_y = sum(life_females_list)/len(life_females_list)
x_deviations =[x - mean_x for x in birth_rate_list]
y_deviations= [y - mean_y for y in life_females_list ]
x_squared_deviations = [ (x - mean_x) ** 2 for x in birth_rate_list ] 
y_squared_deviations = [ (y - mean_y) ** 2 for y in life_females_list] 
xy_deviations = [ x*y for (x,y) in zip(x_squared_deviations,y_squared_deviations)]
 
correlation = (sum(xy_deviations)/sqrt(sum(x_squared_deviations)))*(sqrt(sum(y_squared_deviations)))

print("Correlation is",correlation)