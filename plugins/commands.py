# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import sys
import asyncio 
from database import Db, db
from config import Config, temp
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
import psutil
import time as time
from os import environ, execle, system

START_TIME = time.time()

# Sequence image list
IMAGE_LIST = [
    "https://i.postimg.cc/0jmnDVFJ/FORWARD-BOT-PIC-1.png",
    "https://i.postimg.cc/hGj0pDNn/FORWARD-BOT-PIC-10.png",
    "https://i.postimg.cc/3x310CBd/FORWARD-BOT-PIC-11.png",
    "https://i.postimg.cc/pd6J7NtF/FORWARD-BOT-PIC-12.png",
    "https://i.postimg.cc/kXQw5hW0/FORWARD-BOT-PIC-13.png",
    "https://i.postimg.cc/26L7NHzX/FORWARD-BOT-PIC-14.png",
    "https://i.postimg.cc/bNhH4H43/FORWARD-BOT-PIC-15.png",
    "https://i.postimg.cc/xjH3sFpX/FORWARD-BOT-PIC-16.png",
    "https://i.postimg.cc/D0qQ884r/FORWARD-BOT-PIC-17.png",
    "https://i.postimg.cc/8zkdzkpv/FORWARD-BOT-PIC-18.png",
    "https://i.postimg.cc/4yTVks2m/FORWARD-BOT-PIC-2.png",
    "https://i.postimg.cc/90tTcKs1/FORWARD-BOT-PIC-3.png",
    "https://i.postimg.cc/ZK4pwYyQ/FORWARD-BOT-PIC-4.png",
    "https://i.postimg.cc/sg2SRnm9/FORWARD-BOT-PIC-5.png",
    "https://i.postimg.cc/cHftcP1Z/FORWARD-BOT-PIC-6.png",
    "https://i.postimg.cc/NG7r2hPk/FORWARD-BOT-PIC-7.png",
    "https://i.postimg.cc/HLcyrVfr/FORWARD-BOT-PIC-8.png",
    "https://i.postimg.cc/J4xJvwNz/FORWARD-BOT-PIC-9.png"
]

# ⬇ Create a user_image_index collection for tracking
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config
client = AsyncIOMotorClient(Config.DATABASE_URI)
USER_TRACKER = client.userdb.image_index  # new collection

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    user_id = user.id

    # Add to user DB if new
    if not await db.is_user_exist(user_id):
        await db.add_user(user_id, user.first_name)

    # Fetch or initialize user's image index
    data = await USER_TRACKER.find_one({"_id": user_id})
    index = 0 if not data else (data.get("index", 0) + 1) % len(IMAGE_LIST)

    # Save updated index
    await USER_TRACKER.update_one(
        {"_id": user_id},
        {"$set": {"index": index}},
        upsert=True
    )

    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/MR_ABHAY_K')],
        [InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/AK_BOTZ_SUPPORT'),
         InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/AK_BOTZ_UPDATE')],
        [InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@Tech_VJ')],
        [InlineKeyboardButton('👨‍💻 ʜᴇʟᴘ', callback_data='help'),
         InlineKeyboardButton('💁 ᴀʙᴏᴜᴛ', callback_data='about')],
        [InlineKeyboardButton('⚙ sᴇᴛᴛɪɴɢs', callback_data='settings#main')]
    ])

    await message.reply_photo(
        photo=IMAGE_LIST[index],
        caption=Script.START_TXT.format(user.mention, temp.U_NAME, temp.B_NAME),
        reply_markup=reply_markup
    )
    
# ✅ Restart command
@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER))
async def restart(client, message):
    msg = await message.reply_text(text="<i>Trying to restarting.....</i>")
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "main.py", environ)

# ✅ Help callback
@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    buttons = [[
        InlineKeyboardButton('🤔 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓', callback_data='how_to_use')
    ],[
        InlineKeyboardButton('Aʙᴏᴜᴛ ✨️', callback_data='about'),
        InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='settings#main')
    ],[
        InlineKeyboardButton('• back', callback_data='back')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(text=Script.HELP_TXT, reply_markup=reply_markup)

# ✅ How to use callback
@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    buttons = [[InlineKeyboardButton('• back', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.HOW_USE_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# ✅ Back callback
@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=Script.START_TXT.format(query.from_user.first_name))

# ✅ About callback
@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    buttons = [[
         InlineKeyboardButton('• back', callback_data='help'),
         InlineKeyboardButton('Stats ✨️', callback_data='status')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.ABOUT_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

# ✅ Status callback
@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    forwardings = await db.forwad_count()
    upt = await get_bot_uptime(START_TIME)
    buttons = [[
        InlineKeyboardButton('• back', callback_data='help'),
        InlineKeyboardButton('System Stats ✨️', callback_data='systm_sts'),
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.STATUS_TXT.format(upt, users_count, bots_count, forwardings),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

# ✅ System Stats callback
@Client.on_callback_query(filters.regex(r'^systm_sts'))
async def sys_status(bot, query):
    buttons = [[InlineKeyboardButton('• back', callback_data='help')]]
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    disk_usage = psutil.disk_usage('/')
    total_space = disk_usage.total / (1024**3)  # Convert to GB
    used_space = disk_usage.used / (1024**3)    # Convert to GB
    free_space = disk_usage.free / (1024**3)
    text = f"""
╔════❰ sᴇʀᴠᴇʀ sᴛᴀᴛs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ᴛᴏᴛᴀʟ ᴅɪsᴋ sᴘᴀᴄᴇ</b>: <code>{total_space:.2f} GB</code>
║┣⪼ <b>ᴜsᴇᴅ</b>: <code>{used_space:.2f} GB</code>
║┣⪼ <b>ꜰʀᴇᴇ</b>: <code>{free_space:.2f} GB</code>
║┣⪼ <b>ᴄᴘᴜ</b>: <code>{cpu}%</code>
║┣⪼ <b>ʀᴀᴍ</b>: <code>{ram}%</code>
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

# ✅ Bot uptime function
async def get_bot_uptime(start_time):
    uptime_seconds = int(time.time() - start_time)
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_string = ""
    if uptime_hours != 0:
        uptime_string += f" {uptime_hours % 24}H"
    if uptime_minutes != 0:
        uptime_string += f" {uptime_minutes % 60}M"
    uptime_string += f" {uptime_seconds % 60} Sec"
    return uptime_string
