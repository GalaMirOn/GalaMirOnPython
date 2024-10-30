from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7945501431:AAFiSLBVYJgXjsocCm1XRXDN28KPPrHko0g" # Токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button2 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
kb.insert(button1)
kb.insert(button2)

class UserState(StatesGroup):
    age = State()           # возраст
    growth = State()          # рост
    weight = State()        # вес

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer(f'Привет, {message.from_user.first_name}! Я Бот, помогающий твоему здоровью!', reply_markup=kb)


@dp.callback_query_handler(text = ['formulas'])
async def set_age(call):
    await call.message.answer('Для мужчин: 10*вес(кг) + 6.25*рост(см) - 5*возраст(г) + 5')
    await call.message.answer('Для женщин: 10*вес(кг) + 6.25*рост(см) - 5*возраст(г) - 161', reply_markup=kb)
    await call.answer()

@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
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
    calories_men = 10 * weight_int + 6.25 * growth_int - 5 * age_int + 5
    await message.answer(f'Рекомендуемое количество калорий для мужчин: {calories_men}')
    calories_wumen = 10 * weight_int + 6.25 * growth_int - 5 * age_int - 161
    await message.answer(f'Рекомендуемое количество калорий для женщин: {calories_wumen}', reply_markup=kb)
    await state.finish()

@dp.message_handler()
async def set_age(message):
    await message.answer('Введите команду /start чтобы начать общение')


if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)
