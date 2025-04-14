from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(messeage: Message):
    await messeage.reply(f"Hello!.\n Твой ID: {messeage.from_user.id}\n Имя : {messeage.from_user.first_name}",
                        reply_markup=await kb.inline_cars())

@router.message(Command('help'))
async def get_help(message:Message):
    await message.answer("Чем могу помочь ? Это была команда /help")

@router.message(F.text == "Как дела?")#f это сообщение от пользователя
async def how_are_you(message: Message):
    await message.answer("ОК!")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото : {message.photo[-1].file_id}")

@router.message(Command('get_photo'))
async def get_user_photo(message: Message):
    await message.answer_photo(photo= 'AgACAgIAAxkBAANfZ_0Eps1d-bvqlGwzxn6Vcz5sXwYAAr71MRvKQ-lLXVMAAbicpnPXAQADAgADeAADNgQ', caption="Это твоя фотография ?")

@router.message(Command('vidio'))
async def start_vidio(message:Message):
    await message.answer("Какое видео вы хотите посмотреть?")