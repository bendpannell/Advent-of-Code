

test = list(open('test.txt', 'r'))
inputs = list(open('input.txt', 'r'))

my_input = inputs

key_list = []
dir_list = []
result = {}

for cmd in my_input:
    
    # print(cmd.strip())
    my_cmd = cmd.strip()

    if '$ cd' in my_cmd:
        if '..' in my_cmd:
            key_list = key_list[:-1]
        else:
            if my_cmd[5:] not in result.keys():
                result[my_cmd[5:]] = 0
            
            if my_cmd[5:] not in dir_list:
                dir_list.append(my_cmd[5:])
                
            key_list.append(my_cmd[5:])
    elif '$ ls' in my_cmd:
        continue
    else:
        lst = my_cmd.split(' ')
        
        if 'dir' in lst[0]:
            dir_list.append(lst[1])
            result[lst[1]] = 0
        else:
            
            result[lst[1]] = int(lst[0])

            for k in key_list:
                result[k] += int(lst[0])
    
# print(dir_list)
print(result)
# print(my_input)
total = 0

for d in dir_list:
    
    print(d, result[d])
    if result[d] <= 100000:
        # print(d, result[d])
        total += int(result[d])
        
print(total)

# for k, v in result.items():
#     if int(v) < 100000:
#         print(k)



def part_1(input):
    
    result = {}

    output = build_dic(input, result)
    
    return output
    
    
    
    

def build_dic(input, output):
    
    current_dir = []
    
    for cmd in input:


        if '$ cd' in cmd:
            current_dir = cd(output, current_dir, cmd[5:].strip())
        elif '$ ls' in cmd:
            continue
        else:
            output = add_file(output, current_dir, cmd)
        
    return output
    # print(f'current directory: {current_dir}')
    # print(f'final dict: {output}')
        
def cd(dic, dir_list, cmd): 
    

    if '..' in cmd:
        dir_list = dir_list[:-1]
    else:
        dir_list.append(cmd)
        if cmd not in get_keys(dic):
            dic[cmd] = {}
            
    return dir_list
        
def add_file(dic, dir_list, li): 
    
    list = li.split(" ") 
    
    var = dic 
    
    for dir in dir_list:
        var = var[dir]
        
    if list[0] == 'dir':
        var[list[1].strip()] = {}
    else:
        var[list[1].strip()] = list[0].strip()

    return dic
        
def get_keys(dic):
    
    for key, value in dic.items():
        yield key
        if isinstance(value, dict):
            yield from get_keys(value)
        
        
# output = part_1(my_input)
        
# final = {}

# key_list = []


# def get_kvs(dic):
    
#     for key, value in dic.items():
        
#         final[key] = 0
#         print(f'key: {key}, value: {value}')
#         print(f'key list: {key_list}')
        
#         # for k in key_list:
#         #     #final[key] += int(value)
            
#         #     my_var = my_var[k]
#         #     print(my_var)
        
#         if isinstance(value, dict):
#             key_list.append(key)
            
#             get_kvs(value)
            
#         else: # not isinstance(value, dict):# and key_list:
            
#             final[key] = int(value)      
            
#             if key in my_var.keys():
#                 final[key] += int(value)
#             else:
#                 del key_list[-1]
#         # elif not isinstance(value, dict) and not key_list:
#         #     final[key] = int(value)
            
#         print(f'final dictionary: {final}')
    
# get_kvs(output)



# dic2 = {}
# key_dic = {}
          
# def asdf(dictionary):
    
#     for key, value in dictionary.items():

        
        
#         if isinstance(value, dict):
#             dic2[key] = [value]
#             asdf(value)
#             # continue
#         else:
#             key_dic[key] = value
    
# print(f'Part 1: {part_1(my_input)}')







# asdf(output)

# print(f'Dictionary w/ keys: {dic2} \n')
# print(f'Key Dictionary: {key_dic} \n')

# # def vals(d):
    
# #     for key, value in d.items():
    
# #         if key in key_dic:
# #             print(key_dic[key])
# #         else:
# #             print('you suck')


# test_dic = {'e': {'i': '584'}}
            

# final = {}

# # for key, value in dic2.items():
# #     # print(key, value)
    
# #     final[key] = 0
    
# #     if isinstance(value, dict):
# #         fdsa(value, key_dic)
# #     else:
# #         final[key] = value
# key_list = []

# def fdsa(dictionary):
    
#     for key, value in dictionary.items(): #e: {i:584}
        
#         if isinstance(value, dict):
#             key_list.append(key)
#             fdsa(value)
#         else:
#             if key in key_dic:
#                 final[key] = key_dic[key]

#     print(key_list)
# fdsa(test_dic)
                
# print(final)
            








dic = {'/':  
            {'a': 
                 {'f': 29116,
                  'g': 2557,
                  'h': 62596,
                  'e': 
                      {'i': 584}
                  },
              'b': 14848514,
              'c': 851231212,
              'd': 
                  {'j': 4060000,
                    'd': 8030000,
                    'd.log': 5620000,
                    'k': 7210000}
            }
}
    

# my_list = {}
    
# def my_func(dict):
    
#     for k, v in dict.items():
#         my_list[k] = [list(get_kvs(v))]
        
#         print(test)
#     # print(my_list)
    


# def get_list(dict):
    
#     for k, v in dict.items():
        
#         my_list[k] = [list()]

# my_func(dic)
        
        
        
        
    
# print(dic.values())
# my_list = {}

# my_keys = list(get_keys(dic))

# for key in my_keys:
#     key_sum(key, dic)
#     # print(key)
    

# def key_sum(key, dic):
    
#     for k, v in dic.items():
#         if key == k:
#             print('here')
#             print(key)
#         else:
        
#             print('not here')

# def get_key(dic):
    
#     for key, value in dic.items():
        
#         my_list[key] = []
        
#         if isinstance(value, dict):
#             my_list[key] = list(my_func(value))
#         else:
#             my_list[key] = value

# # get_key(dic)
# print(my_list)

# def my_func(dictionary):
    
#     total = 0
    
#     for k, v in dictionary.items():
#         if isinstance(v, dict):
            
#             yield from my_func(v)
#         else:
#             total += int(v)
#             yield total
        
# # print(list(my_func(dic)))
        
# # print(values({'d': {'i': 62596}}))
            
        
    
# # print(dic.items())
    

    
# # my_list = list(get_keys(dic))
# # print(my_list)

# # ml = list(get_kvs(dic))
# # print(ml)

# # for k in my_list:
# #     my_dic[k] = 0
    
# #     my_dic[k] = get_kvs(k, dic)
    
    
# # print(my_dic)