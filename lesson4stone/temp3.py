my_dict = {}

num_list = '1213451'
print(my_dict)

for item in num_list:
    my_dict[item] = my_dict.get(item, 0) + 1
    print(item)
    print(my_dict)

print(my_dict)