import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from bot.handlers import setup



load_dotenv()
storage = MemoryStorage()
bot = Bot(
    token=os.getenv("TOKEN"),
    default=DefaultBotProperties(parse_mode="HTML")
)

async def main():
    dp = Dispatcher(storage=storage)
    router = setup()
    dp.include_router(router)
    await dp.start_polling(bot)
    try:
        await asyncio.Event().wait()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())