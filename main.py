import logging
import os

import wikipedia
from dotenv import load_dotenv

load_dotenv()
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("TOKEN")

wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Assalomu alaykum Botimizga xush kelibsiz 😇 \nSizga kerakli ma'lumotni kerakli Sahifasini kiriting 👇")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("....natija topilmadi❌")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
