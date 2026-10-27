from aiogram.fsm.state import StatesGroup, State


class BookingState(StatesGroup):
    choosing_service = State()
    choosing_date = State()
    choosing_time = State()
    confirming = State()
