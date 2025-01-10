from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавить чат')],
    [KeyboardButton(text='Приобрести подписку')],
    [KeyboardButton(text='Инфо'), KeyboardButton(text='Настройки')]],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')

info = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация о всех группах', callback_data='info_2')],
    [InlineKeyboardButton(text='Инфа по отдельности', callback_data='info_2')]
])

add_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text='Добавьте бота в чат',
        url='https://t.me/antispam4000_bot?startgroup&admin=promote_members+delete_messages+restrict_members+invite_users+pin_messages+manage_video_chats'
    )]
])


groups = ['Коты в картинках', 'Подслушано центр Э', 'Еще группа']

async def inline_groups():
    keyboard = InlineKeyboardBuilder()
    for group in groups:
        keyboard.add(InlineKeyboardButton(text=group, callback_data=f"group_{group}"))
    return keyboard.adjust(1).as_markup()
