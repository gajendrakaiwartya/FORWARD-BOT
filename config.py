
from os import environ

class temp:
    U_NAME = "@MR_ABHAY_K"
    B_NAME = "@AK_BOTZ_FORWARD_BOT"
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

class Config:
    API_ID = int(environ.get("API_ID", "123456"))  # Put default valid int to avoid crash
    API_HASH = environ.get("API_HASH", "")
    BOT_TOKEN = environ.get("BOT_TOKEN", "")
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot")
    DATABASE_URI = environ.get("DATABASE_URI", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "7037505654"))  # Default owner for safe testing
