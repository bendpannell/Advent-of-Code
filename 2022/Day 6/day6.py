
test = list(open('test.txt', 'r'))


my_input = test

for i in my_input:
    letters = list(i)
    
print(letters)

for l in letters:
    
    index = 0
    
    for i in letters[index:index+4]:
        print(i)