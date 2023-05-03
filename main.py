from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from Front.Handlers import register_handlers
import asyncio
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def main():
    register_handlers(dp)
    await dp.skip_updates()
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())