# Day 2

# Rock      = A, X
# Paper     = B, Y
# Scissors  = C, Z

import numpy as np

#define variables
test = np.loadtxt('test.txt', dtype = 'str')
input = np.loadtxt('input.txt', dtype = 'str')

mylist = input

# Part 1 Mapping
win = {"A": "Y",
        "B": "Z",
        "C": "X"}

draw = {"A": "X",
        "B": "Y",
        "C": "Z"}

lose = {"A": "Z",
        "B": "X",
        "C": "Y"}

# Part 2 Mapping
rock = {"A": "Y",
        "B": "X",
        "C": "Z"}

paper = {"A": "Z",
         "B": "Y",
         "C": "X"}

scissors = {"A": "X",
            "B": "Z",
            "C": "Y"}



def win_value(part, sign):
    
    if part == 1:
        map = {"X": 1,
               "Y": 2,
               "Z": 3}
        
    elif part == 2:
        map = {"X": 0,
               "Y": 3,
               "Z": 6}
    
    if sign in map:
        return map[sign]
    
    
def main(part):
    results = []
    
    for round in mylist:
        # Part 1
        if part == 1:
            if round[0] in win and round[1] == win[round[0]]:
                results.append(6 + win_value(part, round[1]))
        
            elif round[0] in draw and round[1] == draw[round[0]]:
                results.append(3 + win_value(part, round[1]))
        
            elif round[0] in lose and round[1] == lose[round[0]]:
                results.append(win_value(part, round[1]))
                
                
        elif part == 2:
            #Part 2
            if round[0] in rock and round[1] == rock[round[0]]:
                results.append(1 + win_value(part, round[1]))
                
            elif round[0] in paper and round[1] == paper[round[0]]:
                results.append(2 + win_value(part, round[1]))
                
            elif round[0] in scissors and round[1] == scissors[round[0]]:
                results.append(3 + win_value(part, round[1]))
            
    print(f"Part {part}: {sum(results)}")
    
main(1)
main(2)

