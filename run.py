import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router
from app.ai_handlers import ai_router



bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    dp.include_router(ai_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    #TODO: delete before production
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
