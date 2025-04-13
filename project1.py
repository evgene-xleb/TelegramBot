import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


bot = Bot(TOKEN_API,
          default = DefaultBotProperties(parse_mode=ParseMode.HTML)
        )

dp = Dispatcher()


async def start_bot(bot: Bot):
    await bot.send_message(1324526241, text = "Бот запущен и исправно работает!")

async def stop_bot(bot: Bot):
    await bot.send_message(1324526241, text = "Извините бот в данный момент не работает!")

async def get_start(message : Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет {message.from_user.first_name}! я твой помощник по обучению.</b>')
    await message.answer(f'<s>Привет {message.from_user.first_name}! я твой помощник по обучению.</s>')
    await message.reply(f'<tg-spoiler>Привет {message.from_user.first_name}! я твой помощник по обучению.</tg-spoiler>')


@dp.message(Command("id"))
async def get_my_id(message:Message):
    await message.answer(f"Вот ваш ID: {message.from_user.id}")


async def start():
    dp.message.register(get_start)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())

