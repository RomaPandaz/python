from aiogram import types
from loader import dp

@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    print(message)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Бог поможет')

@dp.message_handler()
async def mes_all(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, смотри чего поймал - '
                        f'{message.text}')    