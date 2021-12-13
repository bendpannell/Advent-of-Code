# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:13:22 2021

@author: bpanusb
"""

import numpy as np
import re

ex_list = np.loadtxt('example.txt', dtype = 'str')
test_list = np.loadtxt('input.txt', dtype = 'str')
my_list = [['9,4' '->' '3,4'],
 ['2,2' '->' '2,1'],
 ['7,0' '->' '7,4']]

def make_board(dir):
    
    board = []
    size = 0
    nums = []
    
    plays = re.findall(r'[0-9]{1,3}', str(dir.tolist()))
    
    # print(dir.tolist())
    # print(len(plays))
    
    for i in plays:
        
        # print(i)
        
        nums = str(i).split(',')
        
        # print(nums)
        
        for i in nums:
            # print(type(int(i)))
            # print(type(board_size))
            
            if int(i) > size:
                size = int(i) + 1
            
            
    print(size)
    board = [[0] * size] * size
    
    return board

def play_game(grid, dir):
    
    grid = np.array(grid)
    
    if type(dir) == 'list':
        plays = dir
    else:
        plays = dir.tolist()
        
    # plays = re.findall(r'(\d.\d)', str(dir))
    
       
    for i in plays:
        # print(i)
        # print(i[0])
        # print(i[-1])
        x_i = int(str(i[0]).split(',')[0])
        y_i = int(str(i[0]).split(',')[-1])
        x_f = int(str(i[-1]).split(',')[0])
        y_f = int(str(i[-1]).split(',')[-1])
    
        # print(x_i, y_i, x_f, y_f)
        
    
        if y_i == y_f:
            # print('horizontal move')
            
            if x_i < x_f:
                for i in range(x_i, (x_f + 1)):
                    
                
                    if (type(grid[y_i][i]) == 'int'):
                        grid[y_i][i] += 1
                    else:
                        grid[y_i][i] += 1
                        # int(grid[y_i][i])
                    # print(grid)
            else:
                for i in range(x_f, (x_i + 1)):
                    
                    if (type(grid[y_i][i]) == 'int'):
                        grid[y_i][i] += 1
                    else:
                        grid[y_i][i] += 1
                        # int(grid[y_i][i])
                
        elif x_i == x_f:
            # print('vertical move')
            
            if y_i < y_f:
                for j in range(y_i, (y_f + 1)):
                                        
                    if (type(grid[j][x_i]) == 'int'):
                        grid[j][x_i] += 1
                    else:
                        grid[j][x_i] += 1
                        # int(grid[j][x_i])
            else:
                for j in range(y_f, (y_i + 1)):
                                        
                    if (type(grid[j][x_i]) == 'int'):
                        grid[j][x_i] += 1
                    else:
                        grid[j][x_i] += 1
                        # int(grid[j][x_i])
                
        else:
            print(i)
            
            if x_i < x_f:
                if y_i < y_f:
                    # print('down right')
                    length = max(x_f - x_i, y_f - y_i)
                    
                    
                    for x in range(0, length + 1):
                        
                        grid[y_i + x][x_i + x] += 1
                    
                else:
                    # print('down left')
                    length = max(x_f - x_i, y_i - y_f)
                    
                    for x in range(0, length + 1):
                    
                        grid[y_i - x][x_i + x] += 1
                        
            elif x_i > x_f:
                if y_i < y_f:
                    # print('up right')
                    length = max(x_i - x_f, y_f - y_i)
                    
                    for x in range(0, length + 1):
                        
                            grid[y_i + x][x_i - x] += 1
                else:
                    # print('up left')
                    length = max(x_i - x_f, y_i - y_f)
                    
                    for x in range(0, length + 1):
                        
                            grid[y_i - x][x_i - x] += 1
                    
            # print('Thats a diagonal')
            
    # print(grid)
        
        
        
    return grid

def intersection_count(grid):
    
    count = 0
    
    for i in grid:
        
        for j in i:
            
            if j > 1:
                count += 1
                
    return count



# print(ex_list)
grid = make_board(test_list)
# print(grid)
# print(test_list[2])
final_grid = play_game(grid, test_list)
# print(final_grid)
print(intersection_count(final_grid))



    

# my_play.get_start()
# my_play.get_end()
# print(str(my_list[0]).split('->')[0])