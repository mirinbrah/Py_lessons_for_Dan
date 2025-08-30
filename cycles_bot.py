import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters.command import Command, CommandObject

# Импортируем токен из нашего нового файла
from config import TOKEN_CYCLES

# Создаем объекты бота и диспетчера
# Добавляем parse_mode="HTML" по умолчанию для всех ответов бота
bot = Bot(
    token=TOKEN_CYCLES,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


#  Обработчик стартового сообщения
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я интерактивный обучающий бот.\n\n"
        "<b>Доступные команды:</b>\n"
        "/math - <i>математические операции</i>\n"
        "/countdown - <i>цикл FOR</i>\n"
        "/repeat - <i>цикл WHILE</i>\n\n"
        "Чтобы узнать подробности и посмотреть примеры, отправь команду /help"
    )


# Обработчик /help
@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "<b>Справочная информация по командам:</b>\n\n"

        "<code>/math [число1] [число2]</code>\n"
        "↳ <i>Выполняет сложение, вычитание, умножение и деление.</i>\n"
        "   <b>Пример:</b> <code>/math 100 25</code>\n\n"

        "<code>/countdown [число]</code>\n"
        "↳ <i>Запускает обратный отсчет. Число должно быть от 1 до 10.</i>\n"
        "   <b>Пример:</b> <code>/countdown 8</code>\n\n"

        "<code>/repeat [текст]</code>\n"
        "↳ <i>Повторяет ваш текст 3 раза. Длина до 50 символов.</i>\n"
        "   <b>Пример:</b> <code>/repeat Учусь делать ботов</code>"
    )
    await message.answer(help_text)

# Обработчик /math
@dp.message(Command("math"))
async def cmd_math(message: types.Message, command: CommandObject):
    if not command.args:
        await message.answer("<b>Ошибка:</b> вы не ввели числа.\nПример: <code>/math 10 5</code>")
        return

    try:
        parts = command.args.split()
        if len(parts) != 2:
            await message.answer("<b>Ошибка:</b> нужно ввести ровно два числа.\nПример: <code>/math 10 5</code>")
            return

        a = float(parts[0])
        b = float(parts[1])

        response_text = (
            f"<b>Демонстрация математики:</b>\n\n"
            f"Дано: a = {a}, b = {b}\n\n"
            f"Сложение: {a} + {b} = {a + b}\n"
            f"Вычитание: {a} - {b} = {a - b}\n"
            f"Умножение: {a} * {b} = {a * b}\n"
            f"Деление: {a} / {b} = {a / b if b != 0 else 'бесконечность'}"
        )
        await message.answer(response_text)

    except ValueError:
        await message.answer("<b>Ошибка:</b> пожалуйста, вводите только числа.")
    except Exception as e:
        await message.answer(f"Произошла непредвиденная ошибка: {e}")

# Обработчик /countdown
@dp.message(Command("countdown"))
async def cmd_countdown(message: types.Message, command: CommandObject):
    if not command.args:
        await message.answer("<b>Ошибка:</b> укажите число для отсчета.\nПример: <code>/countdown 7</code>")
        return

    try:
        start_from = int(command.args)

        if not 0 < start_from <= 10:
            await message.answer("<b>Ошибка:</b> число должно быть от 1 до 10.")
            return

        await message.answer(f"Начинаю обратный отсчет с <b>{start_from}</b>...")
        for i in range(start_from, 0, -1):
            await message.answer(str(i))
            await asyncio.sleep(1)
        await message.answer("Пуск! 🚀")

    except ValueError:
        await message.answer("<b>Ошибка:</b> пожалуйста, введите целое число.")

# Обработчик /repeat
@dp.message(Command("repeat"))
async def cmd_repeat(message: types.Message, command: CommandObject):
    if not command.args:
        await message.answer(
            "<b>Ошибка:</b> введите фразу для повторения.\nПример: <code>/repeat Я люблю Python</code>")
        return

    phrase_to_repeat = command.args

    if len(phrase_to_repeat) > 50:
        await message.answer("<b>Ошибка:</b> ваша фраза слишком длинная (максимум 50 символов).")
        return

    await message.answer(f"Сейчас я повторю вашу фразу 3 раза.")
    counter = 0
    while counter < 3:
        counter += 1
        await message.answer(f"Повтор #{counter}: {phrase_to_repeat}")
        await asyncio.sleep(0.5)


# главная функция запуска
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        # Это действие выполнится после остановки polling (например, по Ctrl+C)
        # Оно корректно закрывает сетевое соединение с Telegram
        await bot.session.close()

# трюк чтобы код исполнялся только если мы этот файл напрямую запускаем, полезно когда файлов несколько
if __name__ == "__main__":
    # Настраиваем логирование здесь, чтобы оно работало для всего приложения
    logging.basicConfig(level=logging.INFO)
    # Оборачиваем запуск в try...except для "ловли" KeyboardInterrupt
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # При нажатии Ctrl+C в консоли появится это сообщение, а не traceback
        print("Бот остановлен вручную.")