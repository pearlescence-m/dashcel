import pymongo
import sys
import os
from dotenv import load_dotenv

load_dotenv('.env')

CONNECTION_STRING = os.getenv('CONN_STRING')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

try:
  client = pymongo.MongoClient(CONNECTION_STRING)
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)

# use a database named "myDatabase"
db = client[MONGODB_DATABASE]

# use a collection named "recipes"
my_collection = db["recipes"]

