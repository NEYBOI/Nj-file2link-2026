# (c) adarsh-goel (c) @biisal
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()
bot_name = "NJ Fɪʟᴇ2Lɪɴᴋ Bᴏᴛ"
bisal_channel = "https://telegram.me/botsbynjboi"
bisal_grp = "https://t.me/movierequestgroupNj"

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '15677455'))
    API_HASH = str(getenv('API_HASH', '136c77d8fa51ccb77860165ca8c01c69'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' , '6053416826:AAHaa6rkyOsI5a3sG-466tasnFj4GqS-TWA'))
    name = str(getenv('name', 'NJfiletolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001883625863'))
    NEW_USER_LOG = int(getenv('NEW_USER_LOG', '-1001872764020'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5019308598").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'neymar_boi'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://thomasinaolive:thomasinaolive@cluster0.1i7t8bk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'botsbynjboi')) 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001883625863")).split()))   
    BAN_CHNL = list(set(int(x) for x in str(getenv("BAN_CHNL", "-1001883625863")).split()))   
    
