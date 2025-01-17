from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup

import app.keyboards as kb

router = Router()


class AddBotState(StatesGroup):
    bot_add_event = State()
    bot_command_start = State()


@router.message(CommandStart(), F.chat.type == 'private')
async def command_start_handler(message: Message):
    await message.answer('Привет!\nЯ бот по фильтрации спама. '
                         'Просто добавь меня в чат с правами администратора и я начну работать',
                         reply_markup=kb.add_button)


@router.message(F.text == 'Добавить чат', F.chat.type == 'private')
async def start_reg_channel(message: Message):
    await message.answer(
        'Добавьте бота к себе в чат через кнопку ниже и дайте ему права администратора',
        reply_markup=kb.add_button
    )
