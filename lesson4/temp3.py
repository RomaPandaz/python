my_dict = {}

num_list = '01234567890123456789'
print(my_dict)

for i in num_list:
    my_dict[i] = my_dict.get(i, 0) + 1
    print(i)
    print(my_dict)

print(my_dict)