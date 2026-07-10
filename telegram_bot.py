import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def send_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id = int(CHAT_ID), text = message, parse_mode="Markdown")