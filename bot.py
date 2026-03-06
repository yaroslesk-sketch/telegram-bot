import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

TOKEN = "8570820876:AAEsirWUfNGrlcF0FcXcJ5O3ahquAX74xv8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="Доставка", callback_data="delivery")],
        [InlineKeyboardButton(text="Добро пожаловать", callback_data="welcome")]
    ]
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        """Добро пожаловать в Nina Showroom ✨

Nina Showroom — это пространство современной люксовой моды, где каждая деталь имеет значение. Мы тщательно отбираем одежду, обувь и аксессуары, чтобы предложить нашим клиентам стиль, качество и актуальные тенденции мировых коллекций.

В нашем шоуруме представлены модели, которые подчеркивают индивидуальность и создают безупречный образ.

Выберите нужный раздел ниже:""",
        reply_markup=keyboard
    )


@dp.message(Command("contacts"))
async def contacts(message: Message):
    await message.answer(
        """Контакты Nina Showroom ✨

Мы всегда готовы ответить на ваши вопросы, помочь с подбором моделей и оформить заказ.

Телефон для связи:
📞 89025445443

E-mail:
📧 твояпочта
твоя инста/телега/вк

Мы также можем ответить вам в социальных сетях:
• Telegram
• Instagram
• VK

Свяжитесь с нами — мы с удовольствием проконсультируем вас по наличию товаров, размерам и доставке."""
    )


@dp.message(Command("delivery"))
async def delivery(message: Message):
    await message.answer(
        """Доставка Nina Showroom 🚚

Мы отправляем заказы по всей России.

Условия доставки:
• отправка после подтверждения заказа
• доставка в любой регион РФ
• срок зависит от города получателя

Стоимость доставки:
💰 рассчитывается индивидуально в зависимости от города и службы доставки.

После оформления заказа мы сообщим точную стоимость и сроки доставки.

По всем вопросам:
📞 89025445443
твоя почта
также"""
    )


@dp.message(Command("welcome"))
async def welcome(message: Message):
    await message.answer(
        """Добро пожаловать в Nina Showroom ✨

Мы рады приветствовать вас в нашем пространстве люксовой моды.

В Nina Showroom вы найдете:
• стильную одежду
• премиальную обувь
• элегантные аксессуары

Мы тщательно отбираем каждую модель, чтобы предложить нашим клиентам актуальные коллекции и высокое качество.

Приятного знакомства с Nina Showroom ✨"""
    )


@dp.callback_query()
async def buttons(callback: CallbackQuery):

    if callback.data == "contacts":
        await callback.message.answer(
            """Контакты Nina Showroom ✨

Мы всегда готовы ответить на ваши вопросы, помочь с подбором моделей и оформить заказ.

Телефон для связи:
📞 89025445443

E-mail:
📧 твояпочта
твоя инста/телега/вк

Мы также можем ответить вам в социальных сетях:
• Telegram
• Instagram
• VK

Свяжитесь с нами — мы с удовольствием проконсультируем вас по наличию товаров, размерам и доставке."""
        )

    elif callback.data == "delivery":
        await callback.message.answer(
            """Доставка Nina Showroom 🚚

Мы отправляем заказы по всей России.

Условия доставки:
• отправка после подтверждения заказа
• доставка в любой регион РФ
• срок зависит от города получателя

Стоимость доставки:
💰 рассчитывается индивидуально в зависимости от города и службы доставки.

После оформления заказа мы сообщим точную стоимость и сроки доставки.

По всем вопросам:
📞 89025445443
твоя почта
также"""
        )

    elif callback.data == "welcome":
        await callback.message.answer(
            """Добро пожаловать в Nina Showroom ✨

Люксовая одежда, обувь и аксессуары для вашего идеального образа."""
        )

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
