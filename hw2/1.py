# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('Введите вещественное число : ')
value = input()
valueSTR = str(value)
l = float(value)
sum = 0
i = 0
if l >= 1:
    while i < len(value):
        while value[i] != '.':
            sum = sum + (l%10)
            l = l//10
            i = i + 1
        else:
            i = i +1
            while i < len(value):
                if valueSTR[i] != '.':
                    sum = sum + int(valueSTR[i])
                    i = i + 1
    else:
            i = i +1
else:
     while i < len(valueSTR):
        if valueSTR[i] != '.':
            sum = sum + int(valueSTR[i])
            i = i + 1
        else:
            i = i +1
print(f'{value} -> {int(sum)}')