import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8570820876:AAF0S8AaDACmwxWBnnQ0eZBRZc9nxJjaM7g"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать.\n\n"
        "Доступные команды:\n"
        "/command1 — Контакты\n"
        "/command2 — Доставка"
    )


@dp.message(Command("command1"))
async def contacts(message: Message):
    await message.answer(
        "Контакты:\n"
        "Телефон: 89025445443"
    )


@dp.message(Command("command2"))
async def delivery(message: Message):
    await message.answer(
        "Доставка:\n"
        "Свяжитесь с нами по номеру 89025445443"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
