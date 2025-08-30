import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1. Импорты витальных данных из конфига
from config import TOKEN_LINK, CHANNEL_URL, CHANNEL_NAME

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN_LINK)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    # Код  автоматически использует переменные,
    # которые мы импортировали из конфига.
    join_button = InlineKeyboardButton(
        text=f"✅ Перейти в «{CHANNEL_NAME}»",
        url=CHANNEL_URL
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[join_button]])

    await message.answer(
        "Привет! 👋\n\n"
        "Чтобы перейти в канал, нажми на кнопку!",
        reply_markup=keyboard
    )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())