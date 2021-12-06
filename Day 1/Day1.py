# -*- coding: utf-8 -*-
import numpy as np

testlist = [199,200,208,210,200,207,240,269,260,263]
list = np.loadtxt('input.txt')

# Part 1
def is_larger(x, y):
    
    if x < y:
        return 1
    else:
        return 0
    

def larger_counter(l):
    
    list_length = len(l)
    i = 0
    larger_count = 0
    
    while i < (list_length - 1):
        
        if (is_larger(l[i], l[i+1])):
            larger_count += 1
        i += 1
            
    return larger_count
    
print(larger_counter(list))

# Part 2

three_list = []

for i in range(0, len(list)):
    if i < (len(list) - 2):
        three_list = np.append(three_list, [list[i] + list[i + 1] + list[i + 2]])
    else:
        print('done')

print(larger_counter(three_list))






















