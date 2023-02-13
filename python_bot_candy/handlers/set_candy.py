from loader import dp
from aiogram.types import Message
from data_base import set_candy_db


@dp.message_handler(commands=['set_candy'])
async def set_candy(message: Message):
    set_candy = message.text.split()
    set_candy = set_candy[1]
    print(set_candy)
    id_tg = message.from_user.id
    set_candy_db(set_candy, id_tg)
    await message.answer(f'{message.from_user.first_name} на столе теперь {set_candy} конфет')