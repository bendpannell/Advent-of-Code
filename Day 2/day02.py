# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:00:26 2021

@author: bendp
"""

import numpy as np

example_list = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

#Importing test array w/ 'genfromtxt' automatically deliminates on the 
# space making a 2d array with direction column and value column.
test_list = np.loadtxt('input_2.txt', dtype = 'str', delimiter = '\n')


def get_dir(str):
    
    dir = str.split()
    return dir[0]

def get_value(str):
    
    val = str.split()
    return int(val[1])

def coord_product(list):
    
    """ Find end coordinates from list of direction
    instructions and multiple the final x and y values """
    
    coords = [0, 0]
    
    for i in list:
        
        dir = get_dir(i)
        val = get_value(i)
        
        if dir == 'forward':
            coords[0] += val
        elif dir == 'down':
            coords[1] += val
        elif dir == 'up':
            coords[1] -= val
        
    print(coords)
    return coords[0] * coords[1]

def coord_aim_product(list):
    
    """ Find end coordinates from list of directions, where
    up and down values impact the 'aim' rather than actual 
    movements. Multiply the final x and y values. """
    
    coords = [0, 0]
    aim = 0
    
    for i in list:
        
        dir = get_dir(i)
        val = get_value(i)
        
        if dir == 'forward':
            
            coords[0] += val
            
            if aim == 0:
                coords[1] += 0
            else:
                coords[1] += aim * val
        
        elif dir == 'down':
            aim += val
        elif dir == 'up':
            aim -= val
    

    print(coords)
    return coords[0] * coords[1]
                    

print(f'Part 1 answer: {coord_product(test_list)}')
print(f'Part 2 answer: {coord_aim_product(test_list)}')
