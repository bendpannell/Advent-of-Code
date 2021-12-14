# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:17:51 2021

@author: bpanusb
"""

import numpy as np
from scipy import stats

# ex_list = np.array(list(map(int, np.loadtxt('example.txt', dtype = 'str').tolist().split(','))))

test_list = np.array(list(map(int, np.loadtxt('input.txt', dtype = 'str').tolist().split(','))))


mode = int(stats.mode(test_list)[0])


def fuel_cost(p):
    
    fc = abs(p - mode)

    return fc

fuel_usage = 0

for i in test_list:
    # print(i)
    
    # print(fuel_cost(i))

    fuel_usage += fuel_cost(i)
    
print(fuel_usage)