from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.inline import kb_service, get_days_keyboard, get_times_keyboard, kb_confirm
from keyboards.reply import kb_start
from states.booking import BookingState
from data.services import services
from config import ADMIN_ID


booking_router = Router()


@booking_router.message(F.text == "Записаться")
async def booking_handler(message: Message, state: FSMContext):
    await message.answer("Введите вид услуги", reply_markup=kb_service)
    await state.set_state(BookingState.choosing_service)


@booking_router.callback_query(BookingState.choosing_service)
async def choosing_service_handler(callback: CallbackQuery, state: FSMContext):
    service = callback.data
    await state.update_data(service=service)

    await callback.answer()
    await callback.message.answer("Выберите дату", reply_markup=get_days_keyboard())

    await state.set_state(BookingState.choosing_date)


@booking_router.callback_query(BookingState.choosing_date)
async def choosing_date_handler(callback: CallbackQuery, state: FSMContext):
    date = callback.data
    await state.update_data(date=date)

    await callback.answer()
    await callback.message.answer("Выберите время", reply_markup=get_times_keyboard())

    await state.set_state(BookingState.choosing_time)


@booking_router.callback_query(BookingState.choosing_time)
async def choosing_time_handler(callback: CallbackQuery, state: FSMContext):
    time = callback.data
    await state.update_data(time=time)
    await callback.answer()

    items = await state.get_data()
    service = services.get(items.get("service"))
    date = items.get("date")

    await callback.message.answer(f"Проверьте данные заявки:\n\n"
                                  f"Услуга: {service}\n"
                                  f"Дата: {date}\n"
                                  f"Время: {time}\n\n"
                                  f"Отправить заявку?", reply_markup=kb_confirm)
    await state.set_state(BookingState.confirming)


@booking_router.callback_query(
    BookingState.confirming,
    F.data == "confirm"
)
async def confirming_handler(callback: CallbackQuery, state: FSMContext, bot: Bot):
    items = await state.get_data()

    service = services.get(items.get("service"))
    date = items.get("date")
    time = items.get("time")

    user_id = callback.from_user.id
    user_name = "@" + callback.from_user.username if callback.from_user.username \
        else "Отсутствует"

    await bot.send_message(ADMIN_ID,
                           f"Новая заявка:\n\n"
                           f"Услуга: {service}\n"
                           f"Дата: {date}\n"
                           f"Время: {time}\n\n"
                           f"Telegram id: {user_id}\n"
                           f"Username: {user_name}")
    await callback.answer()
    await callback.message.answer("Заявка подтверждена")
    await state.clear()


@booking_router.callback_query(
    BookingState.confirming,
    F.data == "cancel"
)
async def cancel_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.clear()
    await callback.message.answer("Заявка отменена", reply_markup=kb_start)


@booking_router.message(Command("cancel"))
async def global_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Заполнение заявки отменено", reply_markup=kb_start)
