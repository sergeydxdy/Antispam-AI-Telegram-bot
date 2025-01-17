import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router
from app.ai_handlers import ai_router
from aiogram.fsm.storage.memory import MemoryStorage

from database.models import async_main


storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)


async def main():
    dp.include_router(router)
    dp.include_router(ai_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


async def on_startup(dispatcher):
    await async_main()

if __name__ == '__main__':
    # TODO: delete before production
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
