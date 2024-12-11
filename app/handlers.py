import asyncio
import logging

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    channel_name = State()
    channel_id = State()



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

@router.callback_query(F.data == 'info_2')
async def get_user_id(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Инфо инфо инфо', reply_markup=await kb.inline_groups())

@router.message(Command('reg_channel'))
async def reg_channel(message: Message, state: FSMContext):
    await state.set_state(Register.channel_name)
    await message.answer('Введите названия канала')

@router.message(Register.channel_name)
async def reg_channel_id(message: Message, state: FSMContext):
    await state.update_data(channel_name=message.text)
    await state.set_state(Register.channel_id)
    await message.answer('Введите id канала или ссылку на него')

@router.message(Register.channel_id)
async def reg_end(message: Message, state: FSMContext):
    await state.update_data(channel_name=message.text)
    data = await state.get_data()
    await message.answer(f'{data}')
    await state.clear()



