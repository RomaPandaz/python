from aiogram import types
from loader import dp

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
    if message.text.isdigit():
        total_dict[message.from_user.id] -= int(message.text)
        await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
                                f'На столе осталось {total_dict[message.from_user.id]} конфет')


    # @dp.message_handler()
    # async def bon_get(message: types.Message):
    #     global total
    #     if message.text.isdigit():
    #         total -= int(message.text)
    #         await message.answer(f'{message.from_user.first_name} взял {message.text} конфет. '
    #                             f'На столе осталось {total} конфет')