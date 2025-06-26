import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🌿 О Ибоге"))
menu.add(KeyboardButton("🌀 Как проходит церемония"))
menu.add(KeyboardButton("💬 Отзывы участников"))
menu.add(KeyboardButton("📅 Записаться на консультацию"))
menu.add(KeyboardButton("❓ Частые вопросы"))
menu.add(KeyboardButton("📞 Контакт"))
menu.add(KeyboardButton("📸 Instagram"))

# Инлайн-кнопка Instagram
instagram_btn = InlineKeyboardMarkup().add(
    InlineKeyboardButton("📸 Перейти в Instagram", url="https://instagram.com/vale_winds_magic")
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Приветствую тебя на пути духовного пробуждения 🌿\n\n"
        "Этот бот создан для знакомства с Ибогой — древней африканской растительной медициной.\n\n"
        "Ниже — кнопка на наш Instagram ✨",
        reply_markup=instagram_btn
    )
    await message.answer("Выбери интересующий раздел 👇", reply_markup=menu)

@dp.message_handler(lambda message: message.text == "🌿 О Ибоге")
async def about_iboga(message: types.Message):
    await message.answer(
        "Ибога — сакральное растение из Центральной Африки, использующееся в традиции Бвити для исцеления души и тела. "
        "Оно открывает доступ к древней мудрости и помогает трансформировать подсознательные программы. 🌱"
    )

@dp.message_handler(lambda message: message.text == "🌀 Как проходит церемония")
async def ceremony(message: types.Message):
    await message.answer(
        "Церемония проводится с проводником в безопасной и поддерживающей обстановке. "
        "Перед приёмом — подготовка, настрой, детокс. После — интеграция опыта. 🌌"
    )

@dp.message_handler(lambda message: message.text == "💬 Отзывы участников")
async def testimonials(message: types.Message):
    await message.answer(
        "✨ 'После церемонии я почувствовал, как будто родился заново. Это было путешествие в самую глубину моей души.'\n\n"
        "✨ 'Ибога помогла мне избавиться от страхов и зависимостей. Я снова чувствую любовь к жизни.'"
    )

@dp.message_handler(lambda message: message.text == "📅 Записаться на консультацию")
async def booking(message: types.Message):
    await message.answer(
        "Записаться можно через наш сайт 👉 https://plantmagicworld.com/",
        parse_mode='Markdown'
    )

@dp.message_handler(lambda message: message.text == "❓ Частые вопросы")
async def faq(message: types.Message):
    await message.answer(
        "❓ *Легальна ли Ибога?*\nВ некоторых странах — да, в других — запрещена. Мы консультируем по безопасным маршрутам.\n\n"
        "❓ *Это безопасно?*\nПри правильной подготовке и сопровождении — да. Наши проводники обучены в традиции Бвити.",
        parse_mode='Markdown'
    )

@dp.message_handler(lambda message: message.text == "📞 Контакт")
async def contact_info(message: types.Message):
    await message.answer(
        "📩 Telegram-группа: https://t.me/+T7Pyz7jnErowMGI1\n🌍 Сайт: https://plantmagicworld.com/"
    )

@dp.message_handler(lambda message: message.text == "📸 Instagram")
async def instagram_link(message: types.Message):
    await message.answer(
        "Следи за нашими историями, ритуалами и трансформациями в Instagram 💫\n\n"
        "👉 https://instagram.com/vale_winds_magic",
        parse_mode='Markdown'
    )

executor.start_polling(dp)
