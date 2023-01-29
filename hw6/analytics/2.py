# 4 ДЗ ЗАДАЧА НОМЕР 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
def gen_list(min=0, max=9, len =15):
    rnd_list = []
    for i in range(len):
        rnd_list.append(random.randint(min,max))
    print(rnd_list) 
    return rnd_list
# def exclusive_list(rnd_list):
#     result = []
#     for i in rnd_list:
#         if rnd_list.count(i) == 1:
#             result.append(i)
#     return result
# result = exclusive_list(gen_list())
rnd_list = gen_list()
result = list(filter(lambda x: rnd_list.count(x) == 1, rnd_list))
print(result)

