# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

digit = int(input('Введите число: '))

if (digit%5 == 0 and digit%10 == 0 or digit%15 == 0) and not digit%30 == 0:
    print('+')
else:
    print('-')