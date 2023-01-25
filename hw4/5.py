# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

equation = '-83*x^5 + 43*x^4 + 6*x^3 - 39*x^2 + 28*x + 78 = 0'
my_dict = {}

print(equation)
equation = equation.replace('= 0', '').replace('-', '+ -').replace(' - ', ' -').replace(' ', '').split('+')
print(equation)

for item in equation:
    my_list = item.split('x')
    if len(my_list) == 2:
        my_dict[my_list[1].replace('^', '')] = int(my_list[0].replace('*', ''))
print(my_dict)

# dict = {}
# equation = equation.replace(' = 0', '')
# equation = equation.replace('-', '+ -')
# equation = equation.replace('- ', '-')


# for i in equation.split(' + '):
#     list = i.split("x")
#     if len(list) == 1:
#         dict.update({"0": list[0].replace('*', '')})
#     else:
#         if list[1] == '':
#             dict.update({"1": list[0].replace('*', '')})
#         else:
#             dict.update(({list[1].replace('^', ''): list[0].replace('*', '')}))
# print(dict)