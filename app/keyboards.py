from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TUTOR_URL

tutorial = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Невыходы", 
                              url=TUTOR_URL)]]
)