#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"✯ 𝙼𝚈 𝙽𝙰𝙼𝙴 : <a href='https://t.me/tvseriezzz_bot'>𝙰𝚕𝚊𝚗 𝚆𝚊𝚕𝚔𝚎𝚛</a>\n✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href='https://t.me/tvseriezzz'>𝚃𝚎𝚊𝚖 𝙰𝚕𝚕 𝚒𝚗 𝙾𝚗𝚎 𝙶𝚛𝚘𝚞𝚙</a>\n✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href='https://docs.pyrogram.org'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>\n✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: <a href='https://www.python.org'>𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</a>\n✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: <a href='https://heroku.com'>𝙷𝙴𝚁𝙾𝙺𝚄</a>\n✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]\n\n𝙵𝚘𝚛 𝙼𝚘𝚛𝚎 👇👇\n\n/start - start the bot or get posts\n\n/batch - create link for more than one posts\n\n/genlink - create link for one post\n\n/users - view bot statistics\n\n/broadcast - broadcast any messages to bot users",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
