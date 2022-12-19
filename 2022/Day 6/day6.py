
test = list(open('test.txt', 'r'))
input = list(open('input.txt', 'r'))


my_input = input

for i in my_input:
    letters = list(i)
    
# print(letters)

def get_quad(string, index):
    
    return string[index:index+4]

def get_fourteen(string, index):
    
    return string[index:index+14]

def part_1(string):
    for i, v in enumerate(string):
        
        my_list = get_quad(string, i)
    
        if len(my_list) == len(set(my_list)):
            return (i + 4)
            break

def part_2(string):
    for i, v in enumerate(string):
        
        my_list = get_fourteen(string, i)
        
        if len(my_list) == len(set(my_list)):
            return (i + 14)
            break

print(f'Part 1: {part_1(letters)}')
print(f'Part 2: {part_2(letters)}')
    
    