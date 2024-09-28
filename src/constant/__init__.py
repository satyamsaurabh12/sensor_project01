import os
import urllib.parse

AWS_S3_BUCKET_NAME = "wafer_fault"
MONGO_DATABASE_NAME = "satyam_db"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
username = urllib.parse.quote_plus('satyam')
password = urllib.parse.quote_plus('12ABab@#')

MONGO_DB_URL = f"mongodb+srv://{username}:{password}@cluster0.b555v.mongodb.net/?retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"
artifact_folder = "artifacts"