# Реализуйте алгоритм перемешивания списка.

import random
# a = random.randint(-50,50)
# print(a)

list = [0,1,2,3,4,5,6,7,8,9]
newlist =[]
l = len(list)
print(list)
for i in range(l):
    r = random.randint(-50,50)
    if r >= 0:
        newlist.insert(0,i)
    else:
        newlist.append(i)
print(newlist)