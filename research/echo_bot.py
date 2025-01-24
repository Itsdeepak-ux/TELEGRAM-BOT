import logging
from aiogram import Bot, Dispatcher, executor,types
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# print(TELEGRAM_BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

#initialize bot and Dispatcher
bot= Bot(token=TELEGRAM_BOT_TOKEN)
dp= Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or '/help' command
    """
    # await message.reply(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.reply("Hi\nI am Echo Bot !\nPowered by aiogram.")


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)