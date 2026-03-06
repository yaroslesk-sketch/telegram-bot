import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

TOKEN = "8570820876:AAEsirWUfNGrlcF0FcXcJ5O3ahquAX74xv8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# главное меню
main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ассортимент", callback_data="catalog")],
        [InlineKeyboardButton(text="Контакты", callback_data="contacts")],
        [InlineKeyboardButton(text="Доставка", callback_data="delivery")]
    ]
)

# клавиатура товаров
catalog_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Товар #1", callback_data="item1")],
        [InlineKeyboardButton(text="Товар #2", callback_data="item2")],
        [InlineKeyboardButton(text="Товар #3", callback_data="item3")],
        [InlineKeyboardButton(text="Товар #4", callback_data="item4")],
        [InlineKeyboardButton(text="Товар #5", callback_data="item5")],
        [InlineKeyboardButton(text="Товар #6", callback_data="item6")],
        [InlineKeyboardButton(text="Товар #7", callback_data="item7")],
        [InlineKeyboardButton(text="Товар #8", callback_data="item8")],
        [InlineKeyboardButton(text="Товар #9", callback_data="item9")],
        [InlineKeyboardButton(text="Товар #10", callback_data="item10")],
    ]
)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        """Добро пожаловать в Nina Showroom ✨

Nina Showroom — это пространство современной люксовой моды, где каждая деталь имеет значение. Мы тщательно отбираем одежду, обувь и аксессуары, чтобы предложить нашим клиентам стиль, качество и актуальные тенденции мировых коллекций.

В нашем шоуруме представлены модели, которые подчеркивают индивидуальность и создают безупречный образ.

Выберите нужный раздел ниже:""",
        reply_markup=main_keyboard
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

Свяжитесь с нами — мы с удовольствием проконсультируем вас по наличию товаров, размерам и доставке.""",
        reply_markup=main_keyboard
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
также""",
        reply_markup=main_keyboard
    )


@dp.message(Command("catalog"))
async def catalog(message: Message):
    await message.answer(
        """Ассортимент Nina Showroom ✨

Здесь представлены товары нашего шоурума.  
Выберите интересующий вас товар ниже:""",
        reply_markup=catalog_keyboard
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

Свяжитесь с нами — мы с удовольствием проконсультируем вас по наличию товаров, размерам и доставке.""",
            reply_markup=main_keyboard
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
также""",
            reply_markup=main_keyboard
        )

    elif callback.data == "catalog":
        await callback.message.answer(
            """Ассортимент Nina Showroom ✨

Здесь представлены товары нашего шоурума.  
Выберите интересующий вас товар ниже:""",
            reply_markup=catalog_keyboard
        )

    elif callback.data.startswith("item"):
        await callback.message.answer(
            "тута твои товары будут, если надо:)",
            reply_markup=catalog_keyboard
        )

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
