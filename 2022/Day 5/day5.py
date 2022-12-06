# Day 5 python 

import numpy as np
import pandas as pd

test = 'test.txt'
input = 'input.txt'

# Parse Input
raw = pd.read_csv(test, header = None)


l = []
instructions = []

for row in raw[0]:
    if 'move' in row:
        instructions.append(row)
    else:
        l.append(list(filter(None, row.replace("    ", " xx ").split(" "))))

        
warehouse = pd.DataFrame(l).iloc[::-1].reset_index(drop=True)
warehouse.drop(index = [0,0], axis = 0, inplace = True)
warehouse = warehouse.reset_index(drop=True)


#find last value in start col:
def find_last_value(df, start_col):
    last_value_index = -1
    
    for i, v in enumerate(df[start_col]):
        
        if v != 'xx':
            last_value_index = i
        else:
            break

    return last_value_index

#find last open position in target col:
def find_open_index(df, target_col):
    first_empty_row = -1
    
    for i, v in enumerate(df[target_col]):

        if v == 'xx':
            first_empty_row = i
            break

    return first_empty_row

def move(df, count, start_col, target_col):
    
    cycle_count = 0

    # Number of cols to move:
    while cycle_count < count:
        
        if find_open_index(df, target_col) == -1: 
            
            new_row = pd.DataFrame(np.full((1, len(df.columns)), 'xx'))
            new_df = pd.concat([df, new_row]).reset_index(drop = True)
            
        else:
            new_df = df
 
        
        if find_last_value(new_df, start_col) == -1: #FLV 6
            print('here')
            break
        else:
        
            new_df[target_col][find_open_index(new_df, target_col)] = df[start_col][find_last_value(new_df, start_col)]
            new_df[start_col][find_last_value(new_df, start_col)] = 'xx'
        
        df = new_df
        cycle_count += 1
    
    return new_df

def part_1(warehouse):
    
    move_count = 0
    results = []

    for i,v in enumerate(instructions):

        count = int(v.split(" ")[1])
        start = int(v.split(" ")[3]) - 1
        end = int(v.split(" ")[5]) - 1
        
        warehouse = move(warehouse, count, start, end)
        
            
    print(f"final warehouse:\n {warehouse} \n")
    
    
    for c in warehouse:
        results.append(warehouse[c][find_last_value(warehouse, c)])

    return "".join(results)

print(f"Starting warehouse:\n {warehouse} \n")
print(f"Part 1: {part_1(warehouse)}")
