# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:07:04 2021

@author: bpanusb
"""

ex = open('example.txt').read().split('\n')
test = open('input.txt').read().split('\n')

input = ex

lows = []
row_count = len(input)
col_count = len(input[0])

def jpos(j):
    
    pos = 999

    if j == 0: # first col
        
        pos = 1
        
    elif j == (col_count - 1): # last col
        
        pos = -1
        
    else: # middle
        
        pos = 0
        
        
    return pos


def top_l(i, x, y):
    
    # print('\n')
    # print(i[x][y]) #2
    # print(i[x][y+1]) #1
    # print(i[x+1][y]) #3
    # print('\n')
    
    
    low = 0
    
    if i[x][y] < i[x][y+1]:
        if i[x][y] < i[x+1][y]:
            low = 1

    return low

def top(i, x, y):
    
    # print('\n')
    # print(i[x][y])
    # print(i[x+1][y])
    # print(i[x][y+1])
    # print(i[x][y-1])
    # print('\n')
    
    low = 0
    
    if i[x][y] < i[x+1][y]:
        if i[x][y] < i[x][y-1]:
            if i[x][y] < i[x][y+1]:
                low = 1
    
    return low

def top_r(i, x, y):
    
    # print('\n')
    # print(i[x][y])
    # print(i[x+1][y])
    # print(i[x][y-1])
    # print('\n')
    
    low = 0
    
    if i[x][y] < i[x+1][y]:
        if i[x][y] < i[x][y-1]:
            low = 1
    
    return low

def left(i, x, y):
    
    # int('\n')
    # print(i[x][y])
    # print(i[x+1][y])
    # print(i[x-1][y])
    # print(i[x][y+1])
    # print('\n')
    
    low = 0
    
    if i[x][y] < i[x+1][y]:
        if i[x][y] < i[x-1][y]:
            if i[x][y] < i[x][y+1]:
                low = 1
    
    return low

def right(i, x, y):
    
    # int('\n')
    # print(i[x][y])
    # print(i[x+1][y])
    # print(i[x-1][y])
    # print(i[x][y-1])
    # print('\n')
    
    low = 0
    
    if i[x][y] < i[x-1][y]:
        if i[x][y] < i[x+1][y]:
            if i[x][y] < i[x][y-1]:
                low = 1
    
    return low

def bottom_l(i, x, y):
    
    return

def bottom_r(i, x, y):
    
    return

def bottom(i, x, y):
    
    return

def main(i, x, y):
    
    return


for i in range(0, row_count): #Loop through rows
   
    for j in range(0, col_count): # Loop through individual entries
    
        if i == 0: # top row
                        
            if jpos(j) > 0: # first col
                # print(input[i][j])
                print(top_l(input, i, j))
                
            elif jpos(j) < 0: # last col
                # print(input[i][j])
                print(top_r(input, i, j))
                
                
            else:            # main body
                # print(input[i][j])
                # print(top(input, i, j))
                print(top(input, i, j))

                
        elif i == (row_count - 1):
            print('bottom row')
            
            jpos(j)
   
                
        else:
            print('body')
            
            jpos(j)
   




