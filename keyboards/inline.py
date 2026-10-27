from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from datetime import datetime, timedelta

from data.schedule import times


def get_days_keyboard():
    today = datetime.now()
    builder = InlineKeyboardBuilder()

    for i in range(1, 6):
        next_date = today + timedelta(days=i)

        date_str = next_date.strftime("%d.%m")
        callback_data = next_date.strftime("%Y-%m-%d")

        builder.add(
            InlineKeyboardButton(
                text=date_str,
                callback_data=callback_data
            )
        )

    builder.adjust(2)

    return builder.as_markup()


def get_times_keyboard():
    builder = InlineKeyboardBuilder()

    for i in range(11, 19):
        builder.add(
            InlineKeyboardButton(
                text=times[f"{i}:00"],
                callback_data=times[f"{i}:00"]
            )
        )
    builder.adjust(4)

    return builder.as_markup()


kb_service = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Консультация", callback_data="consultation"),
            InlineKeyboardButton(text="Telegram-бот", callback_data="telegram_bot")
        ],
        [
            InlineKeyboardButton(text="Python", callback_data="rework_python"),
            InlineKeyboardButton(text="Сайт", callback_data="website")
        ]
    ]
)

kb_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="confirm"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel")
        ]
    ]
)
