# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 16:41:50 2021

@author: bendp
"""

import numpy as np
import pandas as pd

ex_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

test_list = np.loadtxt('input.txt', dtype = 'str')


    
def get_gamma_rate(l):
    # Initialize variables
    df = pd.DataFrame()
    gamma = []
    
    # create loop to convert strings to pandas dataframe
    for i in range(0, len(l)):
        
        strlist = list(l[i])
        series = pd.Series(strlist)
        
        df = df.append(series, ignore_index = True)
        
    #print(df.head())
    
    # loop to find most and least frequent values in each column
    for index in df.columns:
        
        eq_flag = 0
        
        freqs = df[index].value_counts()
        
        if len(freqs) > 1:
            most_freq_count = freqs[0]
            least_freq_count = freqs[-1]
            
            if most_freq_count == least_freq_count:
                eq_flag = 1
                # gamma[index].append('1')
            # else:
            #     continue
        if eq_flag == 0:
            gamma.append(df[index].value_counts().index[0])
        else:
            gamma.append('X')
        
        
    # convert to strings
    # gamma_bin_str = ''.join(gamma)
    
    #convert binary to decimal
    # gamma_dec = int(gamma_bin_str, 2)
    
    #print(f'Gamma rate: {gamma}')
    
    return gamma
    
def get_epsilon_rate(l):
    # Initialize variables
    df = pd.DataFrame()
    epsilon = []
    
    # create loop to convert strings to pandas dataframe
    for i in range(0, len(l)):
        
        strlist = list(l[i])
        series = pd.Series(strlist)
        
        df = df.append(series, ignore_index = True)
        
    #print(df.head())
    
    # loop to find most and least frequent values in each column
    for index in df.columns:
        
        eq_flag = 0
        
        freqs = df[index].value_counts()
        
        if len(freqs) > 1:
            most_freq_count = freqs[0]
            least_freq_count = freqs[-1]
            
            if most_freq_count == least_freq_count:
                eq_flag = 1
                # gamma[index].append('1')
            # else:
            #     continue
        if eq_flag == 0:
            epsilon.append(df[index].value_counts().index[-1])
        else:
            epsilon.append('X')
        
        
        # epsilon.append(df[index].value_counts().idxmin())
        
    # convert to strings
    # epsilon_bin_str = ''.join(epsilon)
    
    #convert binary to decimal
    # epsilon_dec = int(epsilon_bin_str, 2)
    
    #print(f'Epsilon rate: {epsilon}')
    
    return epsilon

# print(get_gamma_rate(ex_list))
# print(get_epsilon_rate(ex_list))

def bin_to_dec(str):
    
    return int(str, 2)


def ox_gen_rate(l):
    
    gr = get_gamma_rate(l)
    # print(f'Starting Gamma Rate: {gr}')
    
    list_len = len(l)
    
    ox_gen_list = l.copy().tolist()
    
    j = 0 
    
    while len(ox_gen_list) > 1:
        
        # print(f'Index location: {j}')
        # print('\n')
        for i in range(0, len(l)):
             
            bin_list = list(l[i])
            # print(bin_list)
            
            if gr[j] == 'X':
                gr[j] = '1'
            
            if l[i][j] == gr[j]:
                # print(f'yup {l[i][j]}')
                continue
            else:
                if (l[i] in ox_gen_list):
                    ox_gen_list.remove(l[i])
                    # print(f'nope {l[i][j]}')
        
        # print(ox_gen_list)
        gr = get_gamma_rate(ox_gen_list)
        # print(f'New Gamma Rate: {gr}')
        j += 1
        
     
    list_len = len(ox_gen_list)
    # print(ox_gen_list)     
        
    return ox_gen_list[0]

def co2_scrub_rate(l):
    
    er = get_epsilon_rate(l)
        
    list_len = len(l)
    
    co2_scrub_list = l.copy().tolist()
    
    j = 0 
    
    while len(co2_scrub_list) > 1:
        
        for i in range(0, len(l)):
             
            bin_list = list(l[i])
            # print(bin_list)
            
            if er[j] == 'X':
                er[j] = '0'
            
            if l[i][j] == er[j]:
                continue
            else:
                if (l[i] in co2_scrub_list):
                    co2_scrub_list.remove(l[i])
                    
        
        # print(ox_gen_list)
        er = get_epsilon_rate(co2_scrub_list)
        
        j += 1
        
     
    list_len = len(co2_scrub_list)
    # print(ox_gen_list)     
        
    return co2_scrub_list[0]
    
    
    
    
#Part 1
# print(f'Engine power consumption: {common_bin(test_list)}')

#Part 2
ox_rate_bin = ox_gen_rate(test_list)
ox_rate = bin_to_dec(ox_rate_bin)

co2_rate_bin = co2_scrub_rate(test_list)
co2_rate = bin_to_dec(co2_rate_bin)

print(f'Oxygen Generation Rate: {ox_rate} from {ox_rate_bin} \n')
print(f'CO2 Scrub Rate: {co2_rate} from {co2_rate_bin} \n')
print(f'Life Support Rate: {ox_rate * co2_rate}')