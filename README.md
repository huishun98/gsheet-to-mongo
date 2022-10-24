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
4. Set up Python development environment and run python script
   ```
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python main.py
   ```

## Useful mongosh commands

### 1. Change field type
```
db.chat_data.find().forEach(obj => {
   obj.chat_id=parseInt(obj.chat_id);
   obj.tz_offset=parseFloat(obj.tz_offset);
   obj.created_by=parseInt(obj.created_by);
   print(obj);
   db.chat_data.replaceOne({_id: obj._id}, obj);
});

db.user_data.find().forEach(obj => {
   obj.user_id=parseInt(obj.user_id);
   print(obj);
   db.user_data.replaceOne({_id: obj._id}, obj);
});

db.job_data.find().forEach(obj => {
   obj.created_by=parseInt(obj.created_by);
   obj.last_updated_by=parseInt(obj.last_updated_by);
   obj.chat_id=parseInt(obj.chat_id);
   print(obj);
   db.job_data.replaceOne({_id: obj._id}, obj);
});


```
### 2. Find duplicates
```
db.chat_data.aggregate([
    {"$group" : { "_id": "$chat_id", "count": { "$sum": 1 } } },
    {"$match": {"_id" :{ "$ne" : null } , "count" : {"$gt": 1} } }, 
    {"$project": {"chat_id" : "$_id", "_id" : 0} }
]);

db.user_data.aggregate([
    {"$group" : { "_id": "$user_id", "count": { "$sum": 1 } } },
    {"$match": {"_id" :{ "$ne" : null } , "count" : {"$gt": 1} } }, 
    {"$project": {"user_id" : "$_id", "_id" : 0} }
]);

db.job_data.aggregate([
    {"$group" : { "_id": "$created_ts", "count": { "$sum": 1 } } },
    {"$match": {"_id" :{ "$ne" : null } , "count" : {"$gt": 1} } }, 
    {"$project": {"created_ts" : "$_id", "_id" : 0} }
]);
```
