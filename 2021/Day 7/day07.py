# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:17:51 2021

@author: bpanusb
"""

import numpy as np
import pandas as pd

ex_list = np.array(list(map(int, np.loadtxt('example.txt', dtype = 'str').tolist().split(','))))

test_list = np.array(list(map(int, np.loadtxt('input.txt', dtype = 'str').tolist().split(','))))



mean = int(round(test_list.mean(), 0))

first_q = int(round(np.quantile(test_list, 0.25), 0))
third_q = int(round(np.quantile(test_list, 0.75), 0))

manual = 481

# Get the fuel cost of a specific position p (int) with a specific measure m (int_)
def fuel_cost(p, m):
    
    fc = abs(p - m)
    
    return fc

# Get the total fuel costs at a specific measure m (int)
def get_costs(l, m):
    
    fuel_usage = 0
    
    for i in l:
        
        fuel_usage += fuel_cost(i, m)
        
    return fuel_usage

# print(mean)
# m = 333
# print(get_costs(test_list, m-1))
# print(get_costs(test_list, m))
# print(get_costs(test_list, m+1))

# Optimize the measure to get the lowest fuel cost
def optimize(l, m):
    

    i = 5
    
    diff = get_costs(l, m) - get_costs(l, m + 1)
    print(diff)
    
    c = 1
    
    while i > 0:
        
        print(m)
        
        
        if np.sign(diff) > 0:
            diff = get_costs(l, m) - get_costs(l, m + 1)

            m += 1
            
            print(f'positive {diff}')
        elif np.sign(diff) == 0:
            
            print(f'optimzed? {diff}')
        elif np.sign(diff) < 0:
            diff = get_costs(l, m) - get_costs(l, m + 1)
            m -= 1
            
            print(f'negative {diff}')
    
        i -= 1
    
    return diff

# optimize(test_list, 333)

print(get_costs(test_list, 333))

# print(first_q)
# print(third_q)

# print(mode)
# print(mean)


# manual = 478

# fuel_array = pd.DataFrame()


# for i in range(first_q, third_q):
    
#     fuel_array[0] = i
#     fuel_array[1] = fuel_cost(i)
#     # print(i, fuel_cost(i))

# print(fuel_array)

# def fuel_cost(l, v):
    
#     for i in l:
        
#         fc = abs(x - v)

#     return fc


# print(fuel_cost(ex_list, 2))

# for i in range(first_q, first_q + 5):
    
#     final_pos = np.array(i)
    
#     fuel_used = fuel_cost(test_list, i)
# #     for p in test_list:
        
#     print(final_pos)
#     print(fuel_used)

    # fc_list = np.append(fc_list_p, fc_list_end)

# print(fc_list)


# fuel_usage = 0

# for i in test_list:
#     # print(i)
    
#     # print(fuel_cost(i))

#     fuel_usage += fuel_cost(i)
    
# print(fuel_usage)