from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(messeage: Message):
    await messeage.reply(f"Hello!.\n Твой ID: {messeage.from_user.id}\n Имя : {messeage.from_user.first_name}",
                        reply_markup= kb.main)

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


@router.callback_query(F.data == 'catalog')
async def catalog(callback:CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text("Привет!", reply_markup= await kb.inline_cars()) 


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите ваше имя :")


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Reg.number)
    await message.answer("Введите ваш номер :")

@router.message(Reg.number)
async def two_tree(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f"Регистрация, успешно завершена!\n Имя : {data["name"]}\n Номер : {data["number"]}")
    await state.clear()