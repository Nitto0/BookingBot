from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Записаться"),
            KeyboardButton(text="Мои записи")
        ],
        [
            KeyboardButton(text="О боте")
        ]
    ],
    resize_keyboard=True
)
