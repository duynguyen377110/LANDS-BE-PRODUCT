from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

from src.config.config import Config
from src.share_connect import ShareConnect
from src.router.router_category import router_category
from src.router.router_product import router_product

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
config = Config()
connect = ShareConnect.instance()

# CONFIGURATION
app.config["MONGO_URI"] = config.urlDB
mongo = PyMongo(app)

connect.construction()

app.register_blueprint(router_category)
app.register_blueprint(router_product)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)