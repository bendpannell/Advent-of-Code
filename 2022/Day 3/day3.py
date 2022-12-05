

import numpy as np

test = np.loadtxt('test.txt', dtype='str')
input = np.loadtxt('input.txt', dtype='str')

list = input

p1_results = []
p2_results = []

def part_1():
    for item in list:
        
        half = int(len(item)/2)
        c1 = item[0:half]
        c2 = item[half:int(len(item))]
        
        
        for letter in c1:
            if letter in c2:
                # print(letter)
                p1_results.append(get_priority(letter))
                break

    return p1_results

def part_2():
    
    index_s = 0
    groups = len(list) / 3
    
    while index_s < groups:
        
        group = list[(index_s * 3):((index_s * 3) + 3)]
        
        p1 = group[0]
        p2 = group[1]
        p3 = group[2]
        
        for l in p1:
            if l in p2 and l in p3:
                # print(l)
                p2_results.append(get_priority(l))
                break
            
        index_s += 1
        
    return p2_results

def get_priority(char):
    
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96
    
print(f"Part 1: {sum(part_1())}")
print(f"Part 2: {sum(part_2())}")
    
    

