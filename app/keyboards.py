from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Заниматься'), KeyboardButton(text='Закончить занятие')],#когда указываеться в одну строку это значит что кнопки в одну линию
    [KeyboardButton(text='Повторить материал')],
    [KeyboardButton(text='Подписка')],
],
            resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню.'
)


settings = InlineKeyboardMarkup(inline_keyboard=[
    # [InlineKeyboardButton(text="Запомнить")],
    [InlineKeyboardButton(text="Перевод", url="https://translate.yandex.ru/")],
    [InlineKeyboardButton(text="Youtube", url="https://youtube.com/")],#при создание кнопки в тексте мы должны добовлять url ну или что то еще
])

cars = ["Mersedes", "Toyota", "Mazda", "BMW"]

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car , url="https://kolesa.kz/"))
    return keyboard.adjust(1).as_markup()