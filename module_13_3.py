from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "" # Токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['Фото в Жизнь', 'Твой Дизайн'])
async def foto_message(message):
    print('Сообщение для "Фото в Жизнь"')
    await message.answer('Добро пожаловать в "Фото в Жизнь"')

@dp.message_handler(commands = ['start'])
async def start_message(message):
    print('Начало работы бота "Фото в Жизнь"')
    await message.answer('Рады Вас видеть в нашем Сервис-Боте!')

@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение для "Фото в Жизнь"')
    await message.answer(message.text.upper())


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
