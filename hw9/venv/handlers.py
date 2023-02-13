from aiogram import types
from loader import dp
import random

total_dict = {}

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    print(message)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Бог поможет')

#/set 200
@dp.message_handler(commands=['set'])
async def set_bon(message: types.Message):
    global total
    count = message.text.split()[1]
    if message.text.split()[1].isdigit():
        total = int(count)
        await message.answer(f'Конфет тепрь будет {count}')

@dp.message_handler(commands=['add_player'])
async def mes_start(message: types.Message):
    player_id = message.from_user.id
    total_dict[player_id] = 150
    await message.answer(player_id)
    await message.answer(total_dict)


@dp.message_handler()
async def bon_get(message: types.Message):
    global total_dict
    if total_dict[message.from_user.id]!=0:
        if message.text.isdigit():
            if 0 < int(message.text) < 29 and 0 < int(message.text) < total_dict[message.from_user.id]:
                total_dict[message.from_user.id] -= int(message.text)
                await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                        f'На столе осталось {total_dict[message.from_user.id]} конфет')
            elif total_dict[message.from_user.id]<int(message.text) < 28 and 0 <= int(message.text) < total_dict[message.from_user.id]:
                await message.answer(f'Введи число от 1 до {total_dict[message.from_user.id]}')
                bon_get()
            else:
                await message.answer(f'Введи число от 1 до 28')
                bon_get()
        else:
            await message.answer(f'Пиши нормально')
            bon_get()
    else:
        await message.answer(f'Победил человек')
    if total_dict[message.from_user.id]!=0:
    #ходит бот
        if total_dict[message.from_user.id] <= 28:
                rnd_bot_get = random.randint(1,total_dict[message.from_user.id])
        else:
                rnd_bot_get = random.randint(1,28)
        total_dict[message.from_user.id] -= rnd_bot_get
        await message.answer(f'Бот взял {rnd_bot_get} конфет. Осталось {total_dict[message.from_user.id]}')
    elif total_dict[message.from_user.id]!=0:
        await message.answer(f'Ваш ход')
    else:
        await message.answer(f'Робедил бот')

    # @dp.message_handler()
    # async def bon_get(message: types.Message):
    #     global total
    #     if message.text.isdigit():
    #         total -= int(message.text)
    #         await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
    #                             f'На столе осталось {total} конфет')