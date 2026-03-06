import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8570820876:AAF0S8AaDACmwxWBnnQ0eZBRZc9nxJjaM7g"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Бот работает")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
