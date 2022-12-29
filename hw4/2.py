# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

digit = int(input("Введите натуральное число: "))
simple_digit_list = list(range(2, digit+ 1))        # не получилось обернуть в функцию, выдает <function get_simple_list at 0x000001AD13253E20>
for i in simple_digit_list:
    j = 2
    while i * j <= digit:
        if i * j in simple_digit_list:
            simple_digit_list.remove(i * j)
        j = j + 1
def get_simple_digit(digit, simple_digit_list):
    count = 0
    for i in simple_digit_list:
        if digit % i == 0:
            print(i)
            count = count +1
    if count == 0:
        print("Простые множители отсутсвуют")
get_simple_digit(digit, simple_digit_list)