# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
list = [random.randint(1, 6) for i in range(random.randint(4, 8))]
result = []
print(list)
for i in range(len(list) // 2):
    result.append(list[i] * list[len(list) - 1 - i])
if len(list) % 2 != 0:
    result.append(list[((len(list) -1) - (len(list) // 2))] ** 2)
print(result)