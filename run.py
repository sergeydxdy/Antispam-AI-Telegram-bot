import os
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.ai_handlers import ai_router

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(ai_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
