# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:13:15 2021

@author: bpanusb
"""

import numpy as np
import pandas as pd

ex_list = list(map(int, np.loadtxt('example.txt', dtype = 'str').tolist().split(',')))

test_list = list(map(int, np.loadtxt('input.txt', dtype = 'str').tolist().split(',')))

def fish_count(l, v):
    
    count = 0
    
    for e in l:
        if e == v:
            count +=1
    
    return count

# Initialize fish log
fish_log = pd.DataFrame(data = {
    'Day': 0,
    'f0': fish_count(test_list, 0),
    'f1': fish_count(test_list, 1),
    'f2': fish_count(test_list, 2),
    'f3': fish_count(test_list, 3),
    'f4': fish_count(test_list, 4),
    'f5': fish_count(test_list, 5),
    'f6': fish_count(test_list, 6),
    'f7': fish_count(test_list, 7),
    'f8': fish_count(test_list, 8)}, index = {''})


print(fish_log)

# iterate through the log
def day(fl):
    
    fl['Day'] += 1
    
    # print(fl.iloc[0,1])
    num_zeros = fl.iloc[0, 1]
       
    for i in range(1, 9):
        
        fl.iloc[0,i] = fl.iloc[0, i +1]
                
 
    fl.iloc[0, 9] = num_zeros
    fl.iloc[0, 7] += num_zeros
        
        
    # print(fl)
    return fl


start_day = 0
end_day = 256

while start_day < end_day:
       
    # print(f'Day {start_day}')
    
    day(fish_log)
    start_day += 1

# day(fish_log)
# day(fish_log)
# day(fish_log)
# day(fish_log)


# find total number of fish
total_fish = fish_log.sum(axis = 1)[0] - fish_log['Day']

print(f' Total number of fish: {total_fish}')




# # This code works but will probably kill my machine....
# def day(l):
    
#     for e in range(0, len(l)):
        
#         if np.sign(l[e]):
#             l[e] -= 1
#             # print(l[e])
#         else:
#             l[e] = 6
#             add_fish(l)
    
#     # print(l)
#     return l
    
# def add_fish(l):
    
#     l.append(8)
    
#     return l

# start_day = 0
# end_day = 80

# while start_day < end_day:
       
#     print(f'Day {start_day}')
    
#     day(ex_list)
#     start_day += 1

# fish_count = len(ex_list)
# print(fish_count)