# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти')
value = int(input())
if value == 1:
    print('(0...∞; 0...∞')
elif value == 2:
    print('(0...-∞; 0...∞')
elif value == 3:
    print('(0...-∞; 0...-∞')
elif value == 4:
    print('(0...∞; 0...-∞')
