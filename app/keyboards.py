from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from sympy.physics.units import action
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Подписаться')],
    [KeyboardButton(text='Добавить группу')],
    [KeyboardButton(text='Инфо'), KeyboardButton(text='Помощь')]

],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню')

info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Info on YouTube', url='https://www.youtube.com/watch?v=gUdHsp5rs5g'),]
])


groups = ['Коты в картинках', 'Подслушано центр Э', 'Еще группа']

async def inline_groups():
    keyboard = ReplyKeyboardBuilder()
    for group in groups:
        keyboard.add(KeyboardButton(text=group))
    return keyboard.adjust(1).as_markup()
