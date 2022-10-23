# GSheet to Mongo

A simple script to quickly transfer your Google Sheet data to MongoDB.

## Steps
1. Set up a Google Cloud Service Account ([documentation](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating)) 
   1. Save the key file as `keys.json` in root directory
   2. Share your Google Sheet with the `SERVICE_ACCOUNT_INFO_CLIENT_EMAIL` (defined in the key file)
2. Set required environment variables:
   1. `GSHEET_ID`
   2. `MONGODB_CONNECTION_STRING`
3. Configure `SHEETNAME` and `MONGODB_DB` in [config.py](./config.py)
