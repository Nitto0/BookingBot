from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.reply import kb_start


rt_start = Router()


@rt_start.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Здравствуйте!", reply_markup=kb_start)
    await state.clear()


@rt_start.message(F.text == "О боте")
async def about(message: Message):
    await message.answer("Бот позволяет выбрать услугу и свободное время для записи.")
