import asyncio
import logging

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.models import User
from database.requests import set_user

import app.keyboards as kb

router = Router()


class AddBotState(StatesGroup):
    bot_add_event = State()
    bot_command_start = State()


@router.message(CommandStart(), F.chat.type == 'private')
async def command_start_handler(message: Message):
    await message.answer('Привет!', reply_markup=kb.main_keyboard)


@router.message(F.text == 'Инфо')
async def answer_how_are_you(message: Message):
    await message.answer(
        'Выберете группу, информацию о которой хотите получить',
        reply_markup=await kb.inline_groups())


@router.message(Command('info'))
async def get_help(message: Message):
    await message.answer('Информация о ваших группах', reply_markup=kb.info)


@router.callback_query(F.data == 'info_2')
async def get_user_id(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберете группу, информацию о которой хотите получить',
        reply_markup=await kb.inline_groups())


@router.message(F.text == 'Добавить чат')
async def start_reg_channel(message: Message):
    await message.answer(
        'Добавьте бота к себе в чат через кнопку ниже и дайте ему права администратора',
        reply_markup=kb.add_button
    )


@router.message(F.content_type.in_([ContentType.NEW_CHAT_MEMBERS]))
async def bot_joined_chat(message: Message, state: FSMContext):
    await state.set_state(AddBotState.bot_add_event)
    await state.update_data(bot_add_event=True)
    await state.set_state(AddBotState.bot_command_start)


@router.message(CommandStart(), F.chat.type != 'private', AddBotState.bot_command_start)
async def bot_start_chat(message: Message, state: FSMContext):
    await state.set_state(AddBotState.bot_command_start)
    await state.update_data(bot_command_start=True)

    user = User(user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                date=message.date)

    bot = message.bot

    try:
        await set_user(user)
        await bot.send_message(message.from_user.id, 'Бот успешно добавлен')
    except:
        await bot.send_message(message.from_user.id, 'Возникла ошибка')

    await state.clear()

