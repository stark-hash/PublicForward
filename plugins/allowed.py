from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import UPDATES_CHANNEL, DEV_LINK

@Client.on_message(filters.private & filters.incoming)
async def handle_message(bot, message: Message):
    btn = [[
        InlineKeyboardButton('Updates Channel', url=UPDATES_CHANNEL)
    ],[
        InlineKeyboardButton('Contact', url=DEV_LINK)
    ]]
    await message.reply("Welcome to the bot! Feel free to explore the options below.", reply_markup=InlineKeyboardMarkup(btn)) 
