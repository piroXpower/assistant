import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    WELCOME_MSG = os.environ.get("WELCOME_MSG", None)
    RULES = os.environ.get("RULES", None)
