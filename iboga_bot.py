import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
user_language = {}

# Меню языков
language_menu = ReplyKeyboardMarkup(resize_keyboard=True)
language_menu.add(KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))

# Меню на русском
menu_ru = ReplyKeyboardMarkup(resize_keyboard=True)
menu_ru.add(
    KeyboardButton("🌿 О Ибоге"),
    KeyboardButton("🌀 Как проходит церемония"),
    KeyboardButton("💬 Отзывы участников"),
    KeyboardButton("📅 Записаться на консультацию"),
    KeyboardButton("❓ Частые вопросы"),
    KeyboardButton("📞 Контакт"),
    KeyboardButton("📸 Instagram")
)

# Меню на английском
menu_en = ReplyKeyboardMarkup(resize_keyboard=True)
menu_en.add(
    KeyboardButton("🌿 About Iboga"),
    KeyboardButton("🌀 Ceremony Details"),
    KeyboardButton("💬 Testimonials"),
    KeyboardButton("📅 Book a Session"),
    KeyboardButton("❓ FAQ"),
    KeyboardButton("📞 Contact"),
    KeyboardButton("📸 Instagram")
)

instagram_btn = InlineKeyboardMarkup().add(
    InlineKeyboardButton("📸 Instagram", url="https://instagram.com/vale_winds_magic")
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_language[message.from_user.id] = None
    await message.answer("🌍 Choose your language / Выберите язык:", reply_markup=language_menu)

@dp.message_handler(lambda message: message.text in ["🇷🇺 Русский", "🇬🇧 English"])
async def set_language(message: types.Message):
    lang = 'ru' if "Русский" in message.text else 'en'
    user_language[message.from_user.id] = lang
    if lang == 'ru':
        await message.answer("Язык установлен: 🇷🇺 Русский. Выберите раздел ниже:", reply_markup=menu_ru)
    else:
        await message.answer("Language set to 🇬🇧 English. Choose a section below:", reply_markup=menu_en)

@dp.message_handler()
async def handle_menu(message: types.Message):
    lang = user_language.get(message.from_user.id, 'en')

    if lang == 'ru':
        if message.text == "🌿 О Ибоге":
            await message.answer("Ибога — сакральное растение из Центральной Африки, используемое в традиции Бвити для исцеления души и тела. 🌱")
        elif message.text == "🌀 Как проходит церемония":
            await message.answer("Церемония проходит с проводником в безопасной обстановке. Подготовка, настрой, очищение, интеграция. 🌌")
        elif message.text == "💬 Отзывы участников":
            await message.answer("✨ 'Я как заново родился.' ✨ 'Ибога помогла мне освободиться от страха и зависимостей.'")
        elif message.text == "📅 Записаться на консультацию":
            await message.answer("Записаться можно через сайт 👉 https://plantmagicworld.com/")
        elif message.text == "❓ Частые вопросы":
            await message.answer("❓ *Легальна ли Ибога?* В некоторых странах — да. ❓ *Это безопасно?* При сопровождении — да.", parse_mode='Markdown')
        elif message.text == "📞 Контакт":
            await message.answer("📩 Группа: https://t.me/+T7Pyz7jnErowMGI1\n🌍 Сайт: https://plantmagicworld.com/")
        elif message.text == "📸 Instagram":
            await message.answer("👉 https://instagram.com/vale_winds_magic", reply_markup=instagram_btn)
    else:
        if message.text == "🌿 About Iboga":
            await message.answer("Iboga is a sacred plant from Central Africa used in Bwiti tradition for deep healing and soul work. 🌱")
        elif message.text == "🌀 Ceremony Details":
            await message.answer("Ceremony is held with a trained guide in a safe space. Preparation, intention, detox, integration. 🌌")
        elif message.text == "💬 Testimonials":
            await message.answer("✨ 'I felt like I was reborn.' ✨ 'Iboga helped me release fear and addiction.'")
        elif message.text == "📅 Book a Session":
            await message.answer("You can book via the website 👉 https://plantmagicworld.com/")
        elif message.text == "❓ FAQ":
            await message.answer("❓ *Is Iboga legal?* In some countries — yes. ❓ *Is it safe?* With proper guidance — yes.", parse_mode='Markdown')
        elif message.text == "📞 Contact":
            await message.answer("📩 Telegram group: https://t.me/+T7Pyz7jnErowMGI1\n🌍 Website: https://plantmagicworld.com/")
        elif message.text == "📸 Instagram":
            await message.answer("👉 https://instagram.com/vale_winds_magic", reply_markup=instagram_btn)

executor.start_polling(dp)
