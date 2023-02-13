from loader import dp
from aiogram.types import Message
from data_base import select_count, set_candy_db
import random


@dp.message_handler()
async def count(message: Message):
    if message.text.isdigit():          #првоерка, что введена цифра
        tg_id = message.from_user.id    #tg_id - id игрока
        count_candy = select_count(tg_id)   #количество конфет на столе игрока в БД
        get_candy = int(message.text)       #преобразуем введеное число в INTEGER
        if count_candy >=28:     #условие когда больше остаток конфет на столе больше или равно 28
            if 1 <= get_candy <= 28:            #проверяем, что введеное число удовлетворяет правилам
                count_candy = count_candy - get_candy   #остаток конфет на столе после хода игрока
                await message.answer(f'{message.from_user.first_name} взял {message.text} конфет')
                await message.answer(f'На столе осталось {count_candy} конфет')
            else:
                await message.answer(f'Можно взять только от 1 до 28 конфет за раз')
                return
        else:                   #условие когда больше остаток конфет на столе меньше 28
            if 1 <= get_candy <= count_candy:            #проверяем, что введеное число удовлетворяет правилам
                count_candy = count_candy - get_candy   #остаток конфет на столе после хода игрока
                await message.answer(f'{message.from_user.first_name} взял {message.text} конфет')
                await message.answer(f'На столе осталось {count_candy} конфет')
            else:
                await message.answer(f'Можно взять только от 1 до {count_candy} конфет за раз')
                return
    else:
        await message.answer(f'{message.from_user.first_name}, введи число')

    if count_candy == 0:
        await message.answer(f'{message.from_user.first_name} выиграл и получает все конфеты!')
        set_candy_db(count_candy, tg_id)
        return
    else:
        pass

    set_candy_db(count_candy, tg_id)

        #ходит ботяо
    if count_candy >= 28:
        bot_get_candy = random.randint(1,28)
        count_candy = count_candy - bot_get_candy
        await message.answer(f'🐼 Панда взял {bot_get_candy} конфет')
        await message.answer(f'На столе осталось {count_candy} конфет')
    else:
        bot_get_candy = count_candy
        count_candy = count_candy - bot_get_candy
        await message.answer(f'🐼 Панда взял {bot_get_candy} конфет')
        await message.answer(f'На столе осталось {count_candy} конфет')

    if count_candy == 0:
        await message.answer(f'🐼 Панда выиграл и получает все конфеты!')
        set_candy_db(count_candy, tg_id)
        return
    else:
        set_candy_db(count_candy, tg_id)