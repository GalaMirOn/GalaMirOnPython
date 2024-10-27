from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = "" # Токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()           # возраст
    growth = State()          # рост
    weight = State()        # вес

@dp.message_handler(text = ['Calories', 'calories', 'cal', '0', 'Да', 'да', 'ДА'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(data_age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(data_growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(data_weight=message.text)
    data = await state.get_data()
    age_int = int(data['data_age'])
    growth_int = int(data['data_growth'])
    weight_int = int(data['data_weight'])
    # print('Возраст ', age_int,'рост ', growth_int,'вес ', weight_int)
    calories_men = 10 * weight_int + 6.25 * weight_int - 5 * age_int + 5
    await message.answer(f'Рекомендуемое количество калорий для мужчин: {calories_men}')
    calories_wumen = 10 * weight_int + 6.25 * weight_int - 5 * age_int - 161
    await message.answer(f'Рекомендуемое количество калорий для женщин: {calories_wumen}')
    await state.finish()

@dp.message_handler()
async def set_age(message):
    await message.answer('Добро пожаловать в бот подсчёта калорий. Вам посчитать? (Да)')


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
