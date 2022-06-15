import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝙷𝙴𝙻𝙻𝙾 {mention} 😊,\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href='https://t.me/TVSERIEZZZ2_bot'>𝑬𝒍𝒔𝒂</a>,\n\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 𝙰𝙽𝙳 𝚂𝙴𝚁𝙸𝙴𝚂 😍,\n\n©️ MᴀɪɴᴛᴀɪɴᴇD Bʏ : <a href='https://t.me/tvseriezzz_group'>♠️ 𝑨𝒍𝒍 𝑰𝒏 𝑶𝒏𝒆 𝑮𝒓𝒐𝒖𝒑</a>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝙷𝙴𝙻𝙻𝙾 {mention} 😊,\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href='https://t.me/TVSERIEZZZ2_bot'>𝑬𝒍𝒔𝒂</a>,\n\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 𝙰𝙽𝙳 𝚂𝙴𝚁𝙸𝙴𝚂 😍,\n\n𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙹𝚘𝚒𝚗 𝙸𝚗 𝙼𝚢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕 𝚃𝚘 𝚄𝚜𝚎 𝙼𝚎\n\n𝙺𝚒𝚗𝚍𝚕𝚢 𝙿𝚕𝚎𝚊𝚜𝚎 𝙹𝚘𝚒𝚗 𝙼𝚢 𝙲𝚑𝚊𝚗𝚗𝚎𝚕\n\n©️ MᴀɪɴᴛᴀɪɴᴇD Bʏ : <a href='https://t.me/tvseriezzz_group'>♠️ 𝑨𝒍𝒍 𝑰𝒏 𝑶𝒏𝒆 𝑮𝒓𝒐𝒖𝒑</a>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>🎥 Name :- {filename}</b>\n\n<b>Join <a href='https://t.me/tvseriezzz_group'>♠️ 𝑨𝒍𝒍 𝑰𝒏 𝑶𝒏𝒆 𝑮𝒓𝒐𝒖𝒑</a> for more Movies & Series</b>")

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
