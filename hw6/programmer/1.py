# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input('Введите первый элемент арифмитической прогрессии: '))
d = int(input('Задайте разность прогрессии: '))
n = int(input('Задайте количество элементов прогрессии: '))
zero = 0

my_list = []
for i in range(n):
    my_list.append(a+zero)
    zero = d
    d = d + 2

print(my_list)