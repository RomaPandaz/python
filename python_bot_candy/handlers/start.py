from loader import dp
from aiogram.types import Message
from data_base import add_player
from keyboards import kb_menu


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    id_tg = message.from_user.id
    name = message.from_user.first_name
    count_candy = 150
    user_name = message.from_user.username
    try:
        add_player([id_tg, name,count_candy, user_name])
    except:
        message.answer(f'Смотрю, ты тут уже не впервый раз)')
        pass
    await message.answer(f'Привет, {message.from_user.first_name}! Сыграем? на столе лежит {count_candy} конфет. Конфеты берем по очереди, но не больше 28 за раз! Последний забирает ВСЕ! Чур - ты первый! /'
                         f'Можешь выбрать любое число конфет написав "/set_candy *ЧИСЛО КОНФЕТ*" или выбрать из рандомных значений ниже. Сыграем?',\
    reply_markup=kb_menu)