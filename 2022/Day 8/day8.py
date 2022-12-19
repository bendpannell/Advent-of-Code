import numpy as np

test = np.loadtxt('test.txt', dtype = 'str')
actual = np.loadtxt('input.txt', dtype = 'str')

my_input = actual
# print(my_input)

def part_1(input):
    
    cols = len(input)
    rows = len(input[0])

    print(f'column length: {cols}, row length: {rows}')

    tree_count = 0

    for i in range(cols):
        for j in range(rows):
            
            if (i == 0 or i == (cols - 1)) or (j == 0 or j == (rows - 1)):
                tree_count += 1
            else:
                tree_count += is_visible(i, j, input, 1)
            
    return tree_count

def part_2(input):
    
    cols = len(input)
    rows = len(input[0])
       
    output = []

    for i in range(cols):
        for j in range(rows):
            
            if (i == 0 or i == (cols - 1)) or (j == 0 or j == (rows - 1)):
                continue
            else:
                output.append(is_visible(i, j, input, 2))
                
    return max(output)

def is_visible(tree_row, tree_col, grid, part):
    
    visible = [0,0,0,0]
    
    #check north
    n_index = 1
    
    while n_index <= tree_row:
        
        if grid[tree_row][tree_col] > grid[tree_row - n_index][tree_col]:
        
            visible[0] += 1
        else:
            if part == 1:
                visible[0] = 0
            elif part == 2:
                visible[0] = n_index
            break
        
        n_index += 1      
    
    #check east
    e_index = 1
        
    while e_index < ((len(grid[tree_row])) - tree_col): # 1 < (97)
        
    
        if grid[tree_row][tree_col] > grid[tree_row][tree_col + e_index]:
        
            visible[1] += 1
        else:
            if part == 1:
                visible[1] = 0
            elif part == 2:
                visible[1] = e_index
            break
        
        e_index += 1
    
    #check south
    s_index = 1
    
    while s_index <= ((len(grid) - 1) - tree_row): # 2 <= (3)
        
        if grid[tree_row][tree_col] > grid[tree_row + s_index][tree_col]: #grid[1][2] > grid[3][2]
        
            visible[2] += 1
        else:
            if part == 1:
                visible[2] = 0
            elif part == 2:
                visible[2] = s_index
            break
            
        s_index += 1
    
    #check west
    w_index = 1
    
    while w_index <= tree_col:
        
        if grid[tree_row][tree_col] > grid[tree_row][tree_col - w_index]:
        
            visible[3] += 1
        else:
            if part == 1:
                visible[3] = 0
            elif part == 2:
                visible[3] = w_index
            break
        
        w_index += 1
    
    # print(visible)
    # print(np.prod(visible))
    # output.append(np.prod(visible))
    # print(max(output))
    # print('\n')
    if part == 1:
        return any(visible)
    elif part == 2:
        return np.prod(visible)
    
    
print(f'Part 1: {part_1(my_input)}')
print(f'Part 2: {part_2(my_input)}')
        
        
        
        