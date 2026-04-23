from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("BOT_TOKEN", "8620751527:AAGolJy8SUxrBLNYyXHJZ-Mw5okvrWiA5I8") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(environ.get("API_ID", 34446649)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(environ.get("OWNER_ID", 7892805795)) # Your(owner's) telegram id
    
    MONGO_STR = environ.get("MONGO_STR", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)

    
