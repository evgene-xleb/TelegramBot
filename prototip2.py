import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_API = os.getenv("BOT_TOKEN")


import asyncio

import logging

from aiogram import Bot, Dispatcher

from app.handlers import router

bot = Bot(token= TOKEN_API)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print("EXIT")