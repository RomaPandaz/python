# Напишите программу которая принимает на вход число N и выводить число от -N до N

n = int(input('Введите целое число: '))
my_list = []
for i in range(-n,n+1,1):
    my_list.append(i)
print(*my_list, sep=', ')