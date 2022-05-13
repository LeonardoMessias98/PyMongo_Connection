from flask_cors import CORS
from flask import Flask
import pymongo
from pymongo import MongoClient
import json
from bson import json_util


app = Flask(__name__)
CORS(app)

cluster = MongoClient(
    "mongodb+srv://<login>:<password>@cluster0.ogtku.mongodb.net/resuolve?retryWrites=true&w=majority")
db = cluster['resuolve']
collection = db['metrics']

data = collection.find({"name": "system_cpu_usage"})


@app.route("/", methods=["GET"])
def get():
    json_docs = [json.dumps(doc, default=json_util.default) for doc in data]

    print(json_docs)

    return {"metrics": json_docs, "status": 201}


if __name__ == "__main__":
    app.run(port=5003)
