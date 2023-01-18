from aiogram import Bot, Dispatcher, executor, types


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = '5444310369:AAHDqUKWLTmNoq3TMDopc6rj2tnn7fyaWYo'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\n📝 Это тестовая версия бота PhysicsBot.\nЯ предназначен для помощи девятиклассникам с теорией по физике <3\nПока я умею немного, но ты можешь попробовать отправить мне команды:\n/materialpoint\n/moving')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message_handler(commands=['materialpoint'])
async def process_help_command(message: types.Message):
    await message.answer('⚙️✏️ Механика: Материальная точка и система отсчета (1.1)\n\nТеория - https://www.yaklass.ru/p/fizika/9-klass/mekhanicheskie-iavleniia-osnovy-kinematiki-12594/poniatie-materialnoi-tochki-sistemy-otscheta-322880\nВидеоурок - https://www.youtube.com/watch?v=DdiQlBwYF3g&list=PLvtJKssE5Nri3tJqj1YcRFWIMy9d6aGmW&index=1')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message_handler(commands=['moving'])
async def process_help_command(message: types.Message):
    await message.answer('⚙️🐌  Механика: Перемещение. Скорость прямолинейного равномерного движения (1.2)\n\nТеория - https://www.yaklass.ru/p/fizika/9-klass/mekhanicheskie-iavleniia-osnovy-kinematiki-12594/peremeshchenie-skorost-priamolineinogo-ravnomernogo-dvizheniia-12597\nВидеоурок - https://www.youtube.com/watch?v=YoXiUSQUITY&list=PLvtJKssE5Nri3tJqj1YcRFWIMy9d6aGmW&index=2')

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения, кроме команд "/start" и "/help"
@dp.message_handler()
async def send_echo(message: types.Message):
    await message.answer('🤔 Не совсем понял тебя. Для того, чтобы узнать что я умею напиши /start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)