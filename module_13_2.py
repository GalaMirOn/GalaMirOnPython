from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "Ключ для бота"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['Фото в Жизнь', 'Твой Диайн'])
async def foto_message(message):
    print('Сообщение для "Фото в Жизнь"')

@dp.message_handler(commands = ['start'])
async def start_message(message):
    print('Начало работы бота "Фото в Жизнь"')

@dp.message_handler()
async def all_message(message):
    print('Мы получили сообщение для "Фото в Жизнь"')


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
