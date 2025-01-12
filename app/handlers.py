import asyncio
import logging

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated, ContentType
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from database.requests import set_user

import app.keyboards as kb

router = Router()



class RegisterChannel(StatesGroup):
    date = State()
    chat_id = State()
    chat_title = State()

    user_id = State()
    user_first_name = State()
    user_last_name = State()
    user_username = State()

    new_member_id = State()
    left_member_id = State()

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
async def start_reg_channel(message: Message, state: FSMContext):

    await message.answer(
        'Добавьте бота к себе в чат через кнопку ниже и дайте ему права администратора',
        reply_markup=kb.add_button
    )

    await state.set_state(RegisterChannel.chat_id)


@router.message(F.content_type.in_([ContentType.NEW_CHAT_MEMBERS]))
async def user_joined_chat(message: Message, state: FSMContext):

    print(message)

    date = message.date
    chat_id = message.chat.id
    title = message.chat.title

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    new_member_id = message.new_chat_members[0].id

    action = 'add'

    await state.update_data(
        date=date,
        chat_id=chat_id,
        title=title,
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        new_member_id=new_member_id
    )
    data = await state.get_data()

    bot = message.bot
    await bot.send_message(user_id, f'Бот добавлен пользователем {username}.\nДанные: {data}')
    await set_user(data)
    await state.clear()


@router.message(F.content_type.in_([ContentType.LEFT_CHAT_MEMBER]))
async def user_joined_chat(message: Message):
    print(message)

    date = message.date
    chat_id = message.chat.id
    chat_title = message.chat.title

    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_username = message.from_user.username

    left_member_id = message.left_chat_member.id

    action = 'remove'

    print('Bot left')



