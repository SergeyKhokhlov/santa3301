from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.helper import HelperMode
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5816511074:AAGI1ILeMqIy22rgd2tK4dJZ7GY2Ek3mGAA")
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ["Адрес", "Время доставки", "Любимые роллы", "Отзыв о квесте для тайного санты"]
message_id = 0


class StatesClass(StatesGroup):  # Машина состояний
    mode = HelperMode.snake_case
    code = State()
    info = State()
    address = State()
    delivery = State()
    eat = State()
    feedback = State()
    text = State()


@dp.message_handler(commands=["start"])  # Старт игры
async def cmd_start(message: types.Message):
    message_id = message.chat.id
    await message.answer("Привет, Ксения. Вот ты и перешла к этапу 6. "
                         "Тебе необходимо ввести пароль активации для бота, "
                         "его ты сможешь найти по этой ссылке, это то что "
                         "объдинило нас всех: https://portal.unn.ru/app/profile/home"
                         "\n\n*Введите пароль активации:*", parse_mode="markdown")
    await StatesClass.code.set()


@dp.message_handler(state=StatesClass.code)
async def check_code(message: types.Message, state: FSMContext):
    if message.text == "3822Б1ФИ5":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        for i in kb:
            markup.add(types.KeyboardButton(i))
        await message.answer("*Этап 7. Сбор информации.*\n\n"
                             "У тебя внизу экрана появились кнопки с информацией, которую"
                             "необходимо предоставить для получения подарка.",
                             reply_markup=markup, parse_mode="markdown")
        await StatesClass.info.set()
    else:
        await message.answer("*Введите код активации:*", parse_mode="markdown")


@dp.message_handler(state=StatesClass.info)
async def take_info(message: types.Message, state: FSMContext):
    if message.text == "Адрес":
        await message.answer("*Адрес (улица, дом, квартира):*", parse_mode="markdown",
                             reply_markup=types.ReplyKeyboardRemove())
        await StatesClass.address.set()
    elif message.text == "Время доставки":
        await message.answer("*Напиши, в какие дни и в какое время тебе "
                             "удобно будет принять заказ. О том в какое время он к тебе "
                             "приедет я сообщу:*", parse_mode="markdown",
                             reply_markup=types.ReplyKeyboardRemove())
        await StatesClass.delivery.set()
    elif message.text == "Любимые роллы":
        await message.answer("*Напиши все виды предпочитаемых тобой роллов:*", parse_mode="markdown",
                             reply_markup=types.ReplyKeyboardRemove())
        await StatesClass.eat.set()
    elif message.text == "Отзыв о квесте для тайного санты":
        await message.answer("*Напиши отзыв:*", reply_markup=types.ReplyKeyboardRemove(),
                             parse_mode="markdown")
        await StatesClass.feedback.set()


@dp.message_handler(state=StatesClass.address)
async def send_address(message: types.Message, state: FSMContext):
    for i in kb:
        if i == "Адрес":
            kb.remove(i)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in kb:
        markup.add(types.KeyboardButton(i))
    for i in [755974403, message.chat.id]:
        if i == 755974403:
            await bot.send_message(i, message.text)
        else:
            await bot.send_message(i, "Адрес записан.", reply_markup=markup)
    if len(kb) == 0:
        await message.answer("Спасибо за участие в квесте. Для связи с Тайным Сантой можешь"
                             " использовать тот чат, в котором ты получила ссылку 😉")
        await StatesClass.text.set()
    else:
        await StatesClass.info.set()


@dp.message_handler(state=StatesClass.delivery)
async def send_delivery(message: types.Message, state: FSMContext):
    for i in kb:
        if i == "Время доставки":
            kb.remove(i)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in kb:
        markup.add(types.KeyboardButton(i))
    for i in [755974403, message.chat.id]:
        if i == 755974403:
            await bot.send_message(i, message.text)
        else:
            await bot.send_message(i, "Окей, как закажу доставку, то сразу сообщу.", reply_markup=markup)
    if len(kb) == 0:
        await message.answer("Спасибо за участие в квесте. Для связи с Тайным Сантой можешь"
                             " использовать тот чат, в котором ты получила ссылку 😉")
        await StatesClass.text.set()
    else:
        await StatesClass.info.set()


@dp.message_handler(state=StatesClass.eat)
async def send_eat(message: types.Message, state: FSMContext):
    for i in kb:
        if i == "Любимые роллы":
            kb.remove(i)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in kb:
        markup.add(types.KeyboardButton(i))
    for i in [755974403, message.chat.id]:
        if i == 755974403:
            await bot.send_message(i, message.text)
        else:
            await bot.send_message(i, "Учту)", reply_markup=markup)
    if len(kb) == 0:
        await message.answer("Спасибо за участие в квесте. Для связи с Тайным Сантой можешь"
                             " использовать тот чат, в котором ты получила ссылку 😉")
        await StatesClass.text.set()
    else:
        await StatesClass.info.set()


@dp.message_handler(state=StatesClass.feedback)
async def send_feedback(message: types.Message, state: FSMContext):
    for i in kb:
        if i == "Отзыв о квесте для тайного санты":
            kb.remove(i)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for i in kb:
        markup.add(types.KeyboardButton(i))
    for i in [755974403, message.chat.id]:
        if i == 755974403:
            await bot.send_message(i, message.text)
        else:
            await bot.send_message(i, "Спасибо за отзыв 🤗", reply_markup=markup)

    if len(kb) == 0:
        await message.answer("Спасибо за участие в квесте. Для связи с Тайным Сантой можешь"
                             " использовать тот чат, в котором ты получила ссылку 😉")
        await StatesClass.text.set()
    else:
        await StatesClass.info.set()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)