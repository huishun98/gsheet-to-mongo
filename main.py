from pymongo import MongoClient
import pygsheets
import config
from datetime import datetime
import pandas as pd

gc = pygsheets.authorize(service_file="keys.json")
gsheet = gc.open_by_key(config.GSHEET_ID)

worksheet = gsheet.worksheet_by_title(config.SHEETNAME)
filename = "%s_%s" % (config.SHEETNAME, datetime.today().strftime("%Y%m%d"))
worksheet.export(path="archives", filename=filename)

client = MongoClient(config.MONGODB_CONNECTION_STRING)
db = client[config.MONGODB_DB]
collection = db[config.SHEETNAME.replace(" ", "_")]

raw_df = pd.read_csv("archives/%s.csv" % filename, keep_default_na=False)
for row in raw_df.to_dict(orient="records"):
    print(".")
    if row.get("removed_ts", "") != "":
        continue
    if row.get("superseded_at", "") != "":
        continue

    collection.replace_one(
        {
            "created_ts": row.get("created_ts"),
            "jobname": row.get("jobname"),
            "chat_id": row.get("chat_id"),
            "user_id": row.get("user_id"),
        },
        row,
        upsert=True,
    )
