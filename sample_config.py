import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7635703422:AAHEZl8Gvv_VEnqunDL41E-uiv1H_j66lvc")

    APP_ID = int(os.environ.get("APP_ID", 20047839))

    API_HASH = os.environ.get("API_HASH", "e635f85a4dae812a26c450c0d41276b0")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6691338079").split())
