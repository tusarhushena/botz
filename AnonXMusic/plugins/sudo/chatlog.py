import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from Grabber import user_collection, app

JOINLOGS = "-1001879440964"

async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"˹ʟᴜꜱᴛ ✘ ᴄᴀᴛᴄʜᴇʀ˼\n#NEWCHAT \n ᴄʜᴀᴛ ᴛɪᴛʟᴇ : {matlabi_jhanto}\n ᴄʜᴀᴛ ɪᴅ : {chat_id}\n ᴄʜᴀᴛ ᴜɴᴀᴍᴇ : {chatusername}\n ᴀᴅᴅᴇᴅ ʙʏ : {added_by}"
        await lul_message(JOINLOGS, lemda_text)
        
