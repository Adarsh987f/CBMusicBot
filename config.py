import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("program v2", "session")
BOT_TOKEN = getenv("7146569463:AAE8dlnVRUnP7HEj0bh7sgrJPj4LarGQv3M")
BOT_NAME = getenv("BOT_NAME", "Music bot 🎸")
BG_IMAGE = getenv("BG_IMAGE", "https://graph.org/file/4b6c180e566d4ae40207c.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://graph.org/file/4b6c180e566d4ae40207c.jpg")
AUD_IMG = getenv("AUD_IMG", "https://graph.org/file/69b8db5170e22e937fdda.jpg")
QUE_IMG = getenv("QUE_IMG", "https://graph.org/file/69b8db5170e22e937fdda.jpg")
API_ID = int(getenv("27412728"))
API_HASH = getenv("0ef7db3bf8f66b685cbdbfd82829ae0b")
BOT_USERNAME = getenv("BOT_USERNAME", "@Adarsh_musicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "👑 𝐌ɪ𝐬𝐬᭄𝐒ʜʀᴇʏᴀ 👑")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "@indian_best_english_chatting")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/indian_best_english_chatting")
OWNER_NAME = getenv("OWNER_NAME", "👑 𝐌ɪ𝐬𝐬᭄𝐒ʜʀᴇʏᴀ 👑") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("7047834233")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1002103631960")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
