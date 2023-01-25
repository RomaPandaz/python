# напишите программу которая принимает на вход 5 чисел и ищет максимальное

#первое решение
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
c = int(input('Введите число C: '))
d = int(input('Введите число D: '))
e = int(input('Введите число E: '))
max = a
if b>max:
    max = b
if c>max:
    max = c
if d>max:
    max = d
if e>max:
    max = e
print(max)

#второе решение
list = [a,b,c,d,e]
for i in list:
    if max < i:
        max = i
print(max)

#третье решение
list2 = []
for i in range(5):
    list2.append(int(input(f'Введите число {i+1}: ')))
for i in list2:
    if max < i:
        max = i
print(max)