# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:50:36 2021

@author: bpanusb
"""

import numpy as np

ex = open('example.txt').read().split('\n')
# test = open('input.txt').read().split('\n')

# temorary entry to build logic. Loop later
ex_test = ex[0]


e = ex_test.split('|')

entry = {
    'clues': e[0].split(' '),
    'puzzle': e[-1].split(' ')}


sorted_clues = entry['clues']
sorted_clues.sort(key = len)

wiring = {
        'tt': '',
        'tl': '',
        'tr': '',
        'mm': '',
        'bl': '',
        'br': '',
        'bb': ''}

##################################################
# CODE USED FOR PART 1
# part1 = 0

# for i in ex_test:
    
#     # print(i)
    

#     # Split into clues and puzzle
    
#     e = i.split('|')
#     # print(e)
#     entry = {
#         'clues': e[0].split(' '),
#         'puzzle': e[-1].split(' ')}


#     sorted_clues = entry['clues']
#     sorted_clues.sort(key = len)
    
#     sorted_puzz = entry['puzzle']
#     sorted_puzz.sort(key = len)
    
#     wiring = {
#         'tt': '',
#         'tl': '',
#         'tr': '',
#         'mm': '',
#         'bl': '',
#         'br': '',
#         'bb': ''}

#     part1 += identify_easy(sorted_puzz)
    
    
# print(part1)
########################################################


# Function to identify lists for 1, 4, 7, and 8
def identify_easy(entry):
    
    count = 0
    
    for e in entry:
        
        # print(len(e), e)
        
        s = set(e)
        
        if len(e) == 2:
            count += 1
            wiring['tr'] = list(s)
            wiring['br'] = list(s)
            one = list(s)
         
        elif len(e) == 3:
            wiring['tt'] = list(s.difference(one))
            seven = list(s)
            count += 1
                       
        elif len(e) == 4:
            
            count += 1
            wiring['tl'] = list(s.difference(one))
            wiring['mm'] = list(s.difference(one))
            four = list(s)
            
        elif len(e) == 7:
            
            count += 1
            wiring['bl'] = list(s - set(one) - set(seven) - set(four))
            wiring['bb'] = list(s - set(one) - set(seven) - set(four))
            eight = list(s)
        
        else:
            continue
        
    one_str = ''.join(one)
    four_str = ''.join(four)
    seven_str = ''.join(seven)
    eight_str = ''.join(eight)
    
    return count, wiring, one_str, seven_str, four_str, eight_str
   

# Get list of entries with length 5
def get_fives(e):
        
    five_list = []
    
    for i in e:
        
        if len(i) == 5:
            five_list.append(i)
            
    return five_list


# Get list of entries with length 6
def get_sixes(e):
    
    six_list = []
    
    for i in e:
        
        if len(i) == 6:
            six_list.append(i)
            
    return six_list


# Function to find 3
def find_three(fl, seven):
    
    th = []
    th_st = ''
    
    for i in fl:
        
        i_s = (list(i))
        i_s.sort()
        
        m = 0
        
        for j in seven:
            if j in i_s:
                m += 1
            
            if m == 3:
                th = i
                th_st = ''.join(i)
                fl.remove(i)
    
    return th, th_st, fl


def find_nine(sl, four):
    
    n = []
    n_st = ''
    
    for i in sl:
        
        i_s = (list(i))
        i_s.sort()
        
        m = 0
        
        for j in four:
            if j in i_s:
                m += 1
                
            if m == 4:
                n = i
                n_st = ''.join(i)
                sl.remove(i)
        
    return n, n_st, sl


# Function to find five and two
def find_five_and_two(fl, four):
    
    
    
    for i in fl:
        
        count = 0
        
        for j in four:
            # print(i, j)
            if j in i:
                count += 1
        
        if count == 3:
            f = i
            
        if count == 2:
            t = i
        
        # print(i)
        # print(count)
    
    return f, t

def find_six_and_zero(sl, seven):
    
    for i in sl:
        
        count = 0
        
        for j in seven:
            
            if j in i:
                count += 1
            
        if count == 3:
            s = i
            
        if count == 2:
            z = i
            
    return s, z

count, wiring, one_str, seven_str, four_str, eight_str = identify_easy(sorted_clues)
five_list = get_fives(sorted_clues)
six_list = get_sixes(sorted_clues)
three, three_str, five_list_no_three = find_three(five_list, seven)
five_str, two_str = find_five_and_two(five_list_no_three, four)
nine, nine_str, six_list_no_nine = find_nine(six_list, four)
six_str, zero_str = find_six_and_zero(six_list_no_nine, seven)


print(f'0: {zero_str}')
print(f'1: {one_str}')
print(f'2: {two_str}')
print(f'3: {three_str}')
print(f'4: {four_str}')
print(f'5: {five_str}')
print(f'6: {six_str}')
print(f'7: {seven_str}')
print(f'8: {eight_str}')
print(f'9: {nine_str}')

