from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()

async def start_order(message: types.Message, state: FSMContext):
    await Test.Q1.set()
    await message.answer("пожалйста ответье на вопросы снизу. эти вопросы нужны чтобы отправить ваш заказ.\n"
                         "вопрос №1\n"
                         "напишите ваше ФИО.")


async def answer_q2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q1'] = message.text
        await Test.next()
        await message.reply("Введите ваш адресс")


async def process_done(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Q2'] = message.text
        await state.finish()
        await message.reply(
            "Спасибо. Мы с вами свяжемся.",
            reply_markup=ReplyKeyboardRemove()
        )


async def shaurma(message: types.Message):
    await message.answer_photo(
        open('./photo/arabskaja-shaurma.jpg', 'rb'),
        caption='сочная шаурма вам на стол, вкус арабской ночи.')


async def ham(message: types.Message):
    await message.answer_photo(
        open('./photo/hamburger.jpeg', 'rb'),
        caption='любите гамбургеры? тогда вам к нам!'
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'])
    dp.register_message_handler(answer_q2, state=Test.Q1)
    dp.register_message_handler(process_done, state=Test.Q2)
    dp.register_message_handler(shaurma, commands=['shaurma'])
    dp.register_message_handler(ham, commands=['ham'])