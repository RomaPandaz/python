# Напишите программу которая принимает на вход два числа и проеряет является ли одно число квадратом другого:

a = int(input('Введите А: '))
b = int(input('Введите B: '))

if a * a == b or b * b == a:
    print('да')
else:
    print('нет')