# Создайте программу для игры с конфетами человек против человека. 
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
 
# a) Добавьте игру против бота 
# b) Подумайте как наделить бота 'интеллектом' 
 
import random 
 
def set_count_candy(): 
    count = int(input('Введите количетсво конфвет: ')) 
    print(f'Отлично, конфет выбранно: {count}. Начинаем !!!') 
    return count 
 
def get_name(): 
    p1 = input('Игрок 1, представьтесь: ') 
    p2 = input('Игрок 2, представьтесь: ') 
    name_list = [p1, p2] 
    return name_list 
 
def lottery(my_list: list): 
    x = random.randint(0,1) 
    lot = [] 
    if x == 0: 
        print(f'Первым ходит игрок {my_list[0]}') 
        lot = my_list 
    else: 
        print(f'Первым ходит игрок {my_list[1]}') 
        lot.append(my_list[1]) 
        lot.append(my_list[0]) 
    return lot 
 
def validate(get_candy):
    if candy > 28: 
        while (not 0 < get_candy <= 28) or candy < get_candy: 
            get_candy = (int(input(f'Можно взять только от 1 до 28 конфет! Попробуй ещё раз!'))) 
    else:
        while (not 0 < get_candy <= candy) or candy < get_candy: 
            get_candy = (int(input(f'Можно взять только от 1 до {candy} конфет! Попробуй ещё раз!'))) 
    return get_candy 
 
 
candy = set_count_candy() 
players = get_name() 
lotr = lottery(players) 
 
while candy > 0: 
    print(f'Игрок {lotr[0]}, Ваш ход!') 
    get_candy_to_valid = int(input(f'Бери конфеты, {lotr[0]}: ')) 
    get_candy = validate(get_candy_to_valid)  
    candy = candy - get_candy 
    print(f'{lotr[0]} взял {get_candy} конфет, осталось {candy}') 
    if candy == 0: 
        print(f'Игрок {lotr[0]} побеждает!') 
        break 
 
    print(f'Игрок {lotr[1]}, Ваш ход!') 
    get_candy_to_valid = int(input(f'Бери конфеты, {lotr[1]}: ')) 
    get_candy = validate(get_candy_to_valid) 
    candy = candy - get_candy 
    print(f'{lotr[1]} взял {get_candy} конфет, осталось {candy}') 
    if candy == 0: 
        print(f'Игрок {lotr[1]} побеждает!') 
        break 
 
print('Игра окончена')