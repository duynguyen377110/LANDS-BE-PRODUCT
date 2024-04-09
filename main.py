from flask import Flask
from flask_pymongo import PyMongo

from src.config.config import Config
from src.share_connect import ShareConnect

app = Flask(__name__)
config = Config()
connect = ShareConnect.instance()

# CONFIGURATION
app.config["MONGO_URI"] = config.urlDB
mongo = PyMongo(app)

connect.construction()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082, threaded=False)