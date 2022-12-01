# AoC day 1 



# Import test file
testlist = list(open('Test.txt', 'r'))
inputlist = list(open('input.txt', 'r'))

list = inputlist

elf_calories = 0
max_calories = []

# Part 1
for index, value in enumerate(list):
    if value == '\n':
        max_calories.append(elf_calories)
        elf_calories = 0 
    elif index == (len(list) - 1):
        elf_calories += int(value)
        max_calories.append(elf_calories)
    else:
        elf_calories += int(value)
        
print("Part 1:", max(max_calories))

# Part 2

sorted_calories = sorted(max_calories, reverse = True)[:3]



print("Part 2:", sum(sorted_calories))