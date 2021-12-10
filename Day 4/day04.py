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



hits = [[],[],[]]

horiz_map = {
    'row 1': 0,
    'row 2': 0,
    'row 3': 0,
    'row 4': 0,
    'row 5': 0
    }

vert_map = {
    'col 1': 0,
    'col 2': 0,
    'col 3': 0,
    'col 4': 0,
    'col 5': 0
    }

def play_game(boards, calls):
        
    
    
    for call in calls:
        
        print(f'Bingo call: {call}')
        
        for i, board in enumerate(boards):
            
            hits[i].append(make_play(board, call))
            
            print(board)
            print('\n')
            if did_i_win(hits[i]):
                print(hits[i])
                break
                  
            
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

def did_i_win(hits):
    
    # horiz_map = {
    #     'row 1': 0,
    #     'row 2': 0,
    #     'row 3': 0,
    #     'row 4': 0,
    #     'row 5': 0
    #     }

    # vert_map = {
    #     'col 1': 0,
    #     'col 2': 0,
    #     'col 3': 0,
    #     'col 4': 0,
    #     'col 5': 0
    #     }
    
    winner = 0
    
    if len(hits) > 5:
        # print('maybe')
        
        for i, hit in enumerate(hits):
            # print(i)
            if horizontal(hit) == 1:
                winner = 1
                print('BINGO on horiz')
                break
            elif vertical(hit) == 1:
                winner = 1
                print('BING0 on vert')
                break
        print(horiz_map)
        print(vert_map)

    return winner
            
        

def horizontal(hit):
    
    win_flag = 0
    
    for i in hit:
        
        if len(i) > 0:
            if i[0] == 0:
                horiz_map['row 1'] += 1
            elif i[0] == 1:
                horiz_map['row 2'] += 1
            elif i[0] == 2:
                horiz_map['row 3'] += 1
            elif i[0] == 3:
                horiz_map['row 4'] += 1
            elif i[0] == 4:
                horiz_map['row 5'] += 1
        
        for i, r in enumerate(horiz_map.values()):
            if r == 5:
               
                win_flag = 1
                
    return win_flag

def vertical(hit):
    
    win_flag = 0
    
    for i in hit:
        
        if len(i) > 0:
            if i[-1] == 0:
                vert_map['col 1'] += 1
            elif i[-1] == 1:
                vert_map['col 2'] += 1
            elif i[-1] == 2:
                vert_map['col 3'] += 1
            elif i[-1] == 3:
                vert_map['col 4'] += 1
            elif i[-1] == 4:
                vert_map['col 5'] += 1
        
        for i, r in enumerate(vert_map.values()):
            if r == 5:
                
                win_flag = 1
                
    return win_flag




my_test_hit = [[(2, 4)], [(1, 3)], [(2, 1)], [(3, 4)], [(0, 3)], [(0, 2)], [(1, 2)], [(1, 1)], [(1, 1)],[(1, 1)]]
    
boards = get_boards(ex_list)
calls = get_call_list(ex_list)

play_game(boards, calls)

# did_i_win(my_test_hit)
# print(make_play(boards[0], calls[0]))

# hits = [[],[],[]]
# hits[0].append(make_play(boards[1], calls[7]))
# print(hits)


