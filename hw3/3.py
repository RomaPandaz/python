# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
amount = random.randint(1, 3)
list = [round(random.uniform(0, 10), amount) for i in range(10)]
max = min = list[0] % 1
for i in range(1, len(list)):
    temp = list[i] % 1
    if temp > 0:
        if temp > max:
            max = temp
        if temp < min:
            min = temp

print(f'{list} = > {round(max - min, 4)}')