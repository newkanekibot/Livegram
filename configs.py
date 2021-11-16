import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1999537338))
    
    START = str(os.environ.get("START_TEXT", ""))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", ""))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", ""))
