from datetime import datetime
from pyrogram import filters, Client
import requests
from config import *

# ping checker

@Client.on_message(filters.command(["ping"], ["/", ".", "!"]) & filters.user(SUDO_USERS))
async def ping(Client, message):
    start = datetime.now()
    loda = await message.reply_text("» __⏤͟͞𝙍𝙤𝙣𝙣𝙮™𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩__")
    end = datetime.now()
    mp = (end - start).microseconds / 1000
    await loda.edit_text(f"__🤖 ᴘɪɴɢ__\n» `{mp} ms`")

