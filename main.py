import asyncio

from config import bot, dp
from app.handlers import router

async def main():
    dp.include_router(
        router
    )

    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        pass