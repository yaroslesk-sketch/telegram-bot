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
        """Добро пожаловать в Nina Showroom ✨

Nina Showroom — это пространство современной люксовой моды, где каждая деталь имеет значение. Мы тщательно отбираем одежду, обувь и аксессуары, чтобы предложить нашим клиентам стиль, качество и актуальные тенденции мировых коллекций.

В нашем шоуруме представлены модели, которые подчеркивают индивидуальность, создают безупречный образ и позволяют чувствовать себя уверенно в любой ситуации — от повседневных выходов до особых событий.

Мы уделяем особое внимание:
• качеству материалов  
• актуальности моделей  
• комфорту и посадке  
• деталям, которые формируют настоящий стиль

В Nina Showroom вы найдете:
• элегантную и трендовую одежду  
• премиальную обувь  
• стильные аксессуары, завершающие образ

Наша цель — помочь вам создать образ, который подчеркнет вашу индивидуальность и станет отражением вашего вкуса.

Если у вас есть вопросы по наличию товаров, размерам или доставке — мы всегда готовы помочь и подобрать для вас идеальный вариант.

Выберите нужный раздел ниже и познакомьтесь с Nina Showroom ✨ \nВыберите раздел:""",
        reply_markup=keyboard
    )


@dp.message(Command("command1"))
async def contacts(message: Message):
    await message.answer(
        """Контакты Nina Showroom ✨

Мы всегда готовы ответить на ваши вопросы, помочь с подбором моделей и оформить заказ.

Телефон для связи:
📞 89025445443
Так ну а сюда почту твою надо
Сюда еще можно будет инсту/тг/вк

Свяжитесь с нами — мы с удовольствием проконсультируем вас по наличию товаров, размерам и доставке."""
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
        """Контакты Nina Showroom ✨

Мы всегда готовы ответить на ваши вопросы, помочь с подбором моделей и оформить заказ.

Телефон для связи:
📞 89025445443

Свяжитесь с нами — мы с удовольствием проконсультируем вас по наличию товаров, размерам и доставке."""
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
