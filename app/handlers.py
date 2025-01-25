from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest

from config import bot

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    try:
        # Проверяем статус пользователя в группе
        result = await bot.get_chat_member(chat_id='-1002430560587', user_id=message.from_user.id)
        
        # Если пользователь найден в группе
        if result.status in ['member', 'administrator', 'creator']:
            await message.answer('Вы состоите в группе!')
        else:
            await message.answer('Вас всё ещё нет в нашей группе!')
    
    except TelegramBadRequest as e:
        # Обработка ошибок, например, если пользователь не найден
        if 'USER_ID_INVALID' in str(e) or 'PARTICIPANT_ID_INVALID' in str(e):
            await message.answer('Вас всё ещё нет в нашей группе!')
        else:
            await message.answer('Произошла ошибка: ' + str(e))