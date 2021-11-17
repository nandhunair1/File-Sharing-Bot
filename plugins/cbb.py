#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from Script import script
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = script.ABOUT_TXT.format,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏠 Home", callback_data = "start"),
                        InlineKeyboardButton("♥️ Source", callback_data= "source")
                    ],
                    [
                        InlineKeyboardButton("ℹ️ Help", callback_data= "help"),
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = script.HELP_TXT.format(query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏠 Home", callback_data= "start"),
                        InlineKeyboardButton("😊 About", callback_data= "about")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "source":
        await query.message.edit_text(
            text = script.SOURCE_TXT,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("👩‍🦯 Back", callback_data= "about")
                        InlineKeyboardButton("🔒 Close", callback_data = "close"),
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
