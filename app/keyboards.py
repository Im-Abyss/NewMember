from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TUTOR_URL

tutorial = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти", 
                              url=TUTOR_URL)]]
)