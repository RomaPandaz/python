my_dict = {32:'32', 1:'Один', 'Ключ': 2142345, 'Список': [324,324,543,346], 3: 45}

print(my_dict[1])
print(my_dict.get(1))
print(my_dict.get(2, 'Нет такого ключа'))
print(my_dict.get(2, 0) + my_dict.get(3, 0))

my_dict['New'] = 'value'

print(my_dict)

my_dict[3] = my_dict.get(3) + 1

print(my_dict)