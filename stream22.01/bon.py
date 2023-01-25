
import random

total = 150
player_one_name = ''
player_otwo_name = ''

def set_total():
    global total
    total_candies = input('Введите общее количетсво конфет: ')
    total = total_candies

def get_total():
    global total
    return total

def set_player_names():
    while player_two_name == '':
        player_one_name = input('Игрок 1, представьтесь: ')
    player_two_name = input('Игрок 2, представьтесь: ')

    if not player_two_name:
        player_two_name = 'БОТ'
        return True
    else:
        return False

def draw():
    return random.randint(0,1)