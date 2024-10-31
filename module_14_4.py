from crud_functions import get_all_products
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = "7945501431:AAFiSLBVYJgXjsocCm1XRXDN28KPPrHko0g" # Токен
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Воспользуйтесь меню")
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
button3 = KeyboardButton(text="Купить")
kb.add(button1, button2)
kb.add(button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
but0 = InlineKeyboardButton(text="Выберите продукт для покупки", callback_data="product_buying")
but1 = InlineKeyboardButton(text="Product1", callback_data="product_buying")
but2 = InlineKeyboardButton(text="Product2", callback_data="product_buying")
but3 = InlineKeyboardButton(text="Product3", callback_data="product_buying")
but4 = InlineKeyboardButton(text="Product4", callback_data="product_buying")
but5 = InlineKeyboardButton(text="Product5", callback_data="product_buying")
but6 = InlineKeyboardButton(text="Product6", callback_data="product_buying")
kb2.add(but1, but2, but3, but4, but5, but6)

class UserState(StatesGroup):
    age = State()           # возраст
    growth = State()          # рост
    weight = State()        # вес

opis = [" ", "Витамин D-3 10000", "Витамин C 1000", "Цинка пиколинат", "Комплекс EVE", "Комплекс ADAM", "Хром"]

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer(f'Привет, {message.from_user.first_name}! Я Бот, помогающий твоему здоровью!', reply_markup=kb)

@dp.message_handler(text = ['Информация'])
async def set_info(message):
    with open('photo_tekst.jpg', 'rb') as img:
        text_about = "Выберите витамины NOW для поддержания своего здоровья и активного образа жизни!"
        await message.answer_photo(img, text_about)

@dp.message_handler(text = ['Купить'])
async def get_buying_list(message):
    pr = get_all_products()
    for prod in pr:
        #print(prod[1], prod[2], prod[3], prod[4])
        with open(prod[4], 'rb') as img:
            text_about = f"{prod[1]} | {prod[2]} | Цена: {prod[3]}"
            await message.answer(text=text_about)
            await message.answer_photo(img, text_about)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb2)

@dp.callback_query_handler(text = ['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!', reply_markup=kb)
    await call.answer()

@dp.message_handler(text = ['Рассчитать'])
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
    calories_men = 10 * weight_int + 6.25 * growth_int - 5 * age_int + 5
    await message.answer(f'Рекомендуемое количество калорий для мужчин: {calories_men}')
    calories_wumen = 10 * weight_int + 6.25 * growth_int - 5 * age_int - 161
    await message.answer(f'Рекомендуемое количество калорий для женщин: {calories_wumen}')
    await state.finish()
    await message.answer("Комплексы витаминов помогут Вам жить полной жизнью!", reply_markup=kb)


@dp.message_handler()
async def set_all(message):
    await message.answer('Введите команду /start чтобы начать общение', reply_markup=kb)


if __name__=='__main__':

    executor.start_polling(dp, skip_updates=True)
