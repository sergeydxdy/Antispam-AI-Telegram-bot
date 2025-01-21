from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

add_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Добавить бота в чат',
            url='https://t.me/antispam_ai_light_bot?startgroup&admin=promote_members+delete_messages+restrict_members+invite_users+pin_messages+manage_video_chats'
        )]
    ])
