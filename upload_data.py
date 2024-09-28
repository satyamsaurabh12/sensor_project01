from pymongo.mongo_client import MongoClient
import urllib.parse

import pandas as pd
import json

username = urllib.parse.quote_plus('satyam')
password = urllib.parse.quote_plus('12ABab@#')
uri = f"mongodb+srv://{username}:{password}@cluster0.b555v.mongodb.net/?retryWrites=true&w=majority"


# create a new client and connect to server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME = "satyam_db"
COLLECTION_NAME = "waferfault"

import pandas as pd
# df = pd.read_csv("./wafer_23012020_041211.csv")
df = pd.read_csv(r"C:\Users\satyam saurabh\Desktop\Project\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis = 1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)