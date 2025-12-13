from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"Received: {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp)
