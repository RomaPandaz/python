# Задайте список. Напишите программу, которая определит присутсвует ли в заданном списоке строк число.

my_list = ['qwertyui123', '123qwerty', 'sssss', 'x55478']
print(my_list)

search = input('Введите искомое число: ')

for item in my_list:
    if search in item:
        print(f'Число {search} входит в заданный список')
        break
else:
     print(f'Число {search} НЕ входит в заданный список')