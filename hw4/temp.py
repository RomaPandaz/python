# # работа со словарями и парсинг многочлена

# dict1 = {'key1': 10, 'key2': 30, 'key3': 50}
# dict2 = {'key1': 3, 'key2': 25, 'key3': 100}
# dict3 = {}

# for value,key in dict1.items():
#     dict3[value] = dict2.get(value) + dict1.get(value)

# print(dict1)
# print(dict2)
# print(dict3)

equation = '-83*x^5 + 43*x^4 + 6*x^3 - 39*x^2 + 28*x + 78 = 0'
my_dict = {}
equation = equation.replace('-', '+ -').replace(' ','').replace('=0','').split('+')
for item in equation:
    temp_list = item.split('*')
    if len(temp_list) == 2:
        my_dict[temp_list[1].replace('^','').replace('x', '')] = int(temp_list[0])
    elif len(temp_list) == 1:  #без X добавляется в начало вместо конца
        my_dict[1] = temp_list[0]
    # elif temp_list[1] == '':
    #     my_dict[1] = temp_list[0]
print(my_dict)


# my_list = [100, 1]
# my_dict = {}    

# print(my_list)
# print(my_dict)

# my_dict[my_list[1]] = my_list[0]

# print(my_dict)
# print(equation)