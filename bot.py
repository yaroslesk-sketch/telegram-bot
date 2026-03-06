import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

TOKEN = "8570820876:AAEaz_o-1JkkdTwDbaDvlqTYAGQKPiSEUL4"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Клавиатура с кнопками
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
    [InlineKeyboardButton(text="Доставка", callback_data="delivery")]
])


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать.\nВыберите раздел:",
        reply_markup=keyboard
    )


@dp.message(Command("command1"))
async def contacts(message: Message):
    await message.answer(
        "Контакты:\nТелефон: 89025445443"
    )


@dp.message(Command("command2"))
async def delivery(message: Message):
    await message.answer(
        "Доставка:\nСвяжитесь с нами по номеру 89025445443"
    )


# обработка нажатия кнопок
@dp.callback_query()
async def buttons(callback: CallbackQuery):

    if callback.data == "contacts":
        await callback.message.answer(
            "Контакты:\nТелефон: 89025445443"
        )

    elif callback.data == "delivery":
        await callback.message.answer(
            "Доставка:\nСвяжитесь с нами по номеру 89025445443"
        )

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
