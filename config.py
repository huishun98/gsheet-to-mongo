from os import getenv
from dotenv import load_dotenv

load_dotenv()

SHEETNAME = "job data"  # "job data", "chat data", "user data", "whitelist"
MONGODB_DB = "rm_bot"

GSHEET_ID = getenv("GSHEET_ID")  # can be found in the gsheet's url
MONGODB_CONNECTION_STRING = getenv("MONGODB_CONNECTION_STRING")
