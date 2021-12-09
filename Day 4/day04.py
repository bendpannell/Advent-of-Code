# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

ex_list = np.loadtxt('Example.txt', dtype = 'str', delimiter = '\n')
# test_list = np.loadtxt('input.txt', dtype = 'str')

# Setting up the boards and calls
def get_call_list(nplist):
    
    calls = nplist[0].split(',')
    
    return calls

def get_boards(nplist):
    
    board_array = []
    j = 0
    
    for i in range(1, (len(nplist)), 5):
        
        first = nplist[i].split()
        second = nplist[i + 1].split()
        third = nplist[i + 2].split()
        fourth = nplist[i + 3].split()
        fifth = nplist[i + 4].split()
        
        board = np.row_stack([first, second, third, fourth, fifth])
        
        j += 1
        board_array.append(board)

    return board_array

def make_call(calls):
    
    return

hits = [[],[],[]]

def play_game(boards, calls):
        
    for call in calls:
        
        print(call)
        for i, board in enumerate(boards):
            
            hits[i].append(make_play(board, call))
            print(hits[i])
        print(boards)
        
    # print(hits)
    
    return

def make_play(board, call):
    
    hit = []
    
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == call:
                board[i][j] = 'X'
                hit.append((i, j))
    
    # print(hit)
    
    
    return hit





    
boards = get_boards(ex_list)
calls = get_call_list(ex_list)

play_game(boards, calls)

# hits = [[],[],[]]
# hits[0].append(make_play(boards[1], calls[7]))
# print(hits)


    