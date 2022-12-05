

import numpy as np

test = np.loadtxt('test.txt', dtype='str')
input = np.loadtxt('input.txt', dtype='str')

my_list = input

def part(number):
    
    total = 0
    
    for line in my_list:
        
        # print(line.split(','))        
        
        l1 = range(int(line.split(',')[0].split('-')[0]), 
                   int(line.split(',')[0].split('-')[1]) + 1, 1)
        
        l2 = range(int(line.split(',')[1].split('-')[0]), 
                   int(line.split(',')[1].split('-')[1]) + 1, 1)
        
        # print(list(l1), list(l2))
        if number == 1:
            check1 = all(item in l1 for item in l2)
            check2 = all(item in l2 for item in l1)
            
        elif number == 2:
            check1 = any(item in l1 for item in l2)
            check2 = any(item in l2 for item in l1)
        
            
        
        if check1 or check2:
            total += 1
        
    return total
        

print(f"Part 1: {part(1)}")
print(f"Part 2: {part(2)}")