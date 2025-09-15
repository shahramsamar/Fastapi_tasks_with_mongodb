from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb://localhost:27017/?directConnection=true"

clinet = MongoClient(uri,server_api=ServerApi("1"))


try:
    clinet.admin.command("ping")
    print("Pinged your deployment.You successfilly connected to MongoDb!!!!!")
except Exception as e:
    print(e)

db = clinet.tasks
tasks_collection = db['task']     