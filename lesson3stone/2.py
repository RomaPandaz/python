# Напишите программу, оторая определит позицию второго вхождения строки в списке либо сообщит что её нет.

#первый вариант
my_list = ['qwe', 'qwe1', 'wsd', '2e2', '123', 'e21', '2e', 'qwe', 123]
count = 0
search = my_list[0]
for item in range(len(my_list)):
    if my_list[item] == search:
        count = count + 1
        if count > 1:
            print(item)
            break
else:
    print('Повторных вхождений нет')

#второй вариант
my_list = ['qwe', 'qwe1', 'wsd', '2e2', '123', 'e21', '2e', 'qwe', 123]

def check(my_list: list, search: str):
    count = 0
    for i in range(len(my_list)):
        if search == my_list[i]:
            count += 1
            if count == 2:
                print(f'Второй индекс вхождения - {i}')
                break
    else:
        print('Повторных вхождений нет')

check(my_list, 'qwe')