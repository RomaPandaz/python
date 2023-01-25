# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
#   *пример*
# Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число: '))
a = 1
my_list = []
my_list.append(a)
for _ in range(n-1):
    a = a * -3
    my_list.append(a)
print(*my_list, sep=', ')