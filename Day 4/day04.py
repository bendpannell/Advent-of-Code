# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

ex_list = np.loadtxt('Example.txt', dtype = 'str', delimiter = '\n')
# test_list = np.loadtxt('input.txt', dtype = 'str')

bingo_calls = ex_list[0]

first_row = ex_list[1].split()
second_row = ex_list[2].split()

board = np.row_stack([first_row, second_row])
print(board)
# def create_boards(list):
    
#     list[0]
    