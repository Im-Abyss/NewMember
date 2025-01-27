from aiogram import Bot, Dispatcher

from .conf import TOKEN, WEATHER_API, TUTOR_URL

bot = Bot(token=TOKEN)

dp = Dispatcher()

w_api = WEATHER_API