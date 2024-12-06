import asyncio
import logging

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer('Привет!', reply_markup=kb.main_keyboard)

@router.message(Command('info'))
async def get_help(message: Message):
    await message.answer('Информация о боте', reply_markup=kb.info)

@router.message(F.text == 'Как дела?')
async def answer_how_are_you(message: Message):
    await message.answer('Нормально')

@router.message(F.text == 'Покажи группы')
async def answer_how_are_you(message: Message):
    await message.reply('Выши группы:', reply_markup=await kb.inline_groups())

@router.message(F.photo)
async def send_photo_id(message: Message):
    await message.answer(f'Photo ID {message.photo[-1].file_id}')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMyZ0ng2PiSokh6t6vP4M2y5L8p4N8AAnHlMRuxmlBKXYV4plX-DwcBAAMCAAN5AAM2BA',
                               caption='Кушаю чипсы, делаю бота')
@router.message(Command('my_id'))
async def get_user_id(message: Message):
    await message.reply(f'Your ID is {message.from_user.id}')

