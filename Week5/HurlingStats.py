# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:48:40 2020

@author: kshit
"""

team_list =[]
win_list =[]
last_win_list= []
losses_list=[]
last_loss_list =[]
win_ratio_list = []
 
 
headers = []
 
 
 # open the file
 
with open ("hurling_finalists.csv") as hurling:
    headers = hurling.readline().split(",")
    for  line in hurling:         
        team, win, last_win, final_loss, last_loosing_final, final_win_ratio = line.split(",")
        team_list.append(team)
        win_list.append(int(win))  
        last_win_list.append(last_win)
        losses_list.append(int(final_loss))
        last_loss_list.append(last_loosing_final)  
        win_ratio_list.append(int(final_win_ratio.strip("%\n"))) 


print(f"The number of counties that have competed in an All-Ireland Final: {len(team_list)}")
print(f"The total number of All-Ireland finals: {sum(win_list)}")
print(f"The average number of wins per county: {sum(win_list)/len(team_list )}")

last_win_ind = last_win_list.index("2019")

print(f"The current champions are : {team_list[last_win_ind]}")  

most_wins_index = win_list.index(max(win_list))
print(f"The county with most wins is {team_list[most_wins_index]} and their total wins are {max(win_list)}")

win_ratio_ind = win_ratio_list.index(max(win_ratio_list))

print(f"The county with the highest percentage of final wins is {team_list[win_ratio_ind]}")