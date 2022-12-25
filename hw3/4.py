# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

import random
digit = random.randint(1, 10)
result = digit
resultbers_list = []
while result > 0:
    if result == 0:
        break
    resultbers_list.append(result % 2)
    result = result // 2
resultbers_list.reverse()
for i in range(len(resultbers_list)):
    result += int(resultbers_list[i])
    if i < (len(resultbers_list)-1):
        result *= 10
print(digit, '->', result)