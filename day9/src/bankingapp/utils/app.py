#test mongo db connection
import os
import sys
#add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from bankingapp.configurations.conf import Config


if __name__ == "__main__":
    config=Config()
    collection= config.db.create_collection("account")
    #insert a document in accounts collection
    collection.insert_one({"account_no": 123456, "balance": 1000})
    print(config.db.list_collection_names())
    print(collection.find_one({"account_no": 123456}))