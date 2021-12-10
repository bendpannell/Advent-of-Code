# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:13:22 2021

@author: bpanusb
"""

import numpy as np
import re

ex_list = np.loadtxt('example.txt', dtype = 'str')

my_list = ['3,4' '->' '1,4']

def make_board(dir):
    
    board_size = []
    nums = []
    
    for i in dir:
        print(i)
        # for j in i:
        
            # print(j)
        # print(i[-1])
        
    
    return

# make_board(ex_list)


plays = re.findall(r'(\d.\d)', str(ex_list))

for i in plays:
    
    print(i)

# my_play.get_start()
# my_play.get_end()
# print(str(my_list[0]).split('->')[0])