# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:14:02 2021

@author: bpanusb
"""

ex = open('example.txt').read().split('\n')
test = open('input.txt').read().split('\n')

ex.append('0')

data = ex

chars = {
    '[]': {'open': '[',
           'close': ']',
           'count': 0},
    '()': {'open': '(',
           'close': ')',
           'count': 0},
    '{}': {'open': '{',
           'close': '}',
           'count': 0},
    '<>': {'open': '<',
           'close': '>',
           'count': 0}}

corrupt_scores = {
    ')': 3, 
    ']': 57,
    '}': 1197,
    '>': 25137}

close_scores = {
    ')': 1, 
    ']': 2,
    '}': 3,
    '>': 4}




corrs = []

def close_score(o):
    
    print(o)
    
    s = 0
    
    for i in range(len(o)-1, -1, -1):
        
        # print(o)
        
        s *= 5
        
        if o[i] == chars['()']['open']:
            s += 1
            o.pop(-1)
            
        elif o[i] == chars['[]']['open']:
            s += 2
            o.pop(-1)
            
        elif o[i] == chars['{}']['open']:
            s += 3
            o.pop(-1)
            
        elif o[i] == chars['<>']['open']:
            s += 4
            o.pop(-1)
               
    return s



for d in data: 
    
    corr_flag = 0
    opens = []
    closes = []
    
    for i in d:
        
        if i == (chars['[]']['open']):
            chars['[]']['count'] += 1
            opens.append(i)
            
            
        elif i == chars['[]']['close']:
            
            if opens[-1] == chars['[]']['open']:
                opens.pop(-1)
                chars['[]']['count'] -= 1
                
            else:
                corr_flag = 1
                corrs.append(i)
                break
                      
            
        elif i == (chars['()']['open']):
            chars['()']['count'] += 1
            opens.append(i)
            
        elif i == chars['()']['close']:
            
            if opens[-1] == chars['()']['open']:
                opens.pop(-1)
                chars['()']['count'] -= 1
                
            else:
                corr_flag = 1
                corrs.append(i)
                break
              
            
        elif i == (chars['{}']['open']):
            chars['{}']['count'] += 1
            opens.append(i)
            
        elif i == chars['{}']['close']:
            
            if opens[-1] == chars['{}']['open']:
                opens.pop(-1)
                chars['{}']['count'] -= 1
                
            else:
                corr_flag = 1
                corrs.append(i)
                break 
            
            
        elif i == (chars['<>']['open']):
            chars['<>']['count'] += 1
            opens.append(i)
            
        elif i == chars['<>']['close']:
            
            if opens[-1] == chars['<>']['open']:
                opens.pop(-1)
                chars['<>']['count'] -= 1
            
            else:
                corr_flag = 1
                corrs.append(i)
                break
            
        
    if corr_flag == 0:
        closes.append(close_score(opens))
    else:
        closes.append(0)
     
    print(closes)


def error_score(c):
    
    t = 0
    
    for i in c:
        
        t += int(corrupt_scores[i])
        # t += int(i)
    
    return t


print(f'Part 1: {error_score(corrs)}')


def mid_score(c):
    
    
    n = []
    
    for i in c:
        if i > 0:
            n.append(i)

    n.sort()
    print(n)
    
    m = int((round((len(n) / 2), 0)))
        
    return n[m]

print(closes)

# print(f'Part 2: {mid_score(closes)}')
# print(close_score(tclose_score))
        
# print(scores['>'])
# {([(<{}[<>[]}>{[]{[(<()>
        

