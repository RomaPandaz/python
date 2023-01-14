# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random as rnd

k =int(input('Введите максимальную степень: '))
equation = {}
for i in range(k, -1, -1):
    equation[i] = rnd.randint(-100,100)
# print (equation)

eq_str = ''
for key, value in equation.items():
    if key == 1:
        eq_str += f'{value}*x + '
    elif key == 0:
        eq_str += f'{value} + '
    elif value < 0:
        eq_str += f'({value})*x^{key} + '
    else:
        eq_str += f'{value}*x^{key} + '
else: eq_str = eq_str[:-3] + ' = 0'
print(eq_str)
file_obj = open('4.txt', 'w')
file_obj.write(eq_str)
file_obj.close()

# def gen_k_list(k):                          # СПИСОК СТЕПЕНЕЙ
#     list = []
#     j = k
#     for i in range(k+1):
#         list.append(j)
#         j = j - 1
#     return list

# def gen_koef_list(list):                    # СПИСОК КОЭФФИЦИЭНТОВ
#     koef_list=[]
#     for i in range(k+1):
#         koef_list.append(rnd.randint(0,100))
#     koef_list
#     koef_list
#     return koef_list

# k = int(input('Укажите степень: '))

# k_list = gen_k_list(k)
# print(k_list)

# koef_list = gen_koef_list(list)
# print(koef_list)