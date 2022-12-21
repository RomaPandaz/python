# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

list = []
n = int(input('Введите число: '))
b = -n
result = 1
while b <= n:
    list.append(b)
    b = b + 1
print(list)
file = open("File.txt", "r")
a = file.readlines()
for i in range(len(a)):
    a[i] = int(a[i].strip())
print(a)
for i in range(len(a)):
    result = result * list[a[i]]
print(result)
