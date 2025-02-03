import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7880140653:AAFwU7Zvs5g5QoneNfLWfs5kuuA61Lf20k0")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29762406"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "146fcf83a1670e2e926ce874ce31fcb3")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6670233911"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
