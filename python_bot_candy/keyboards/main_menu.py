from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import random

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)     #доска с кнопками

btn_set_candy1 = KeyboardButton(f'/set_candy {random.randint(29,100)}')
btn_set_candy2 = KeyboardButton(f'/set_candy {random.randint(29,100)}')
btn_set_candy3 = KeyboardButton(f'/set_candy {random.randint(29,100)}')
btn_set_candy4 = KeyboardButton(f'/set_candy {random.randint(29,500)}')
btn_set_candy5 = KeyboardButton(f'/set_candy {random.randint(29,500)}')
btn_set_candy6 = KeyboardButton(f'/set_candy {random.randint(29,500)}')
btn_help = KeyboardButton(f'/help 🐼')

kb_menu.add(btn_set_candy1, btn_set_candy2, btn_set_candy3, btn_set_candy4,\
            btn_set_candy5, btn_set_candy6, btn_help)