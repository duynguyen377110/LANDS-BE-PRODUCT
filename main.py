from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
import pika
from src.config.config import Config
from src.router.router_category import router_category
from src.controller.controller_product import ControllerProduct

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
config = Config()

# CONFIGURATION
parameters = pika.URLParameters(config.urlQueue)
connection = pika.BlockingConnection(parameters)

app.config["MONGO_URI"] = config.urlDB
mongo = PyMongo(app)

app.register_blueprint(router_category)

controllerProduct = ControllerProduct()

# PRODUCT
@app.route("/api/v1/product", methods=["POST"])
def create_product():
    data = request.data
    data_decode = data.decode("utf-8")
    return controllerProduct.create_product(mongo, data_decode)


@app.route("/api/v1/product_update", methods=["PATCH"])
def update_product():
    data = request.data
    data_decode = data.decode("utf-8")
    return controllerProduct.update_product(mongo, data_decode)


@app.route("/api/v1/product_delete", methods=["DELETE"])
def delete_product():
    data = request.data
    data_decode = data.decode("utf-8")
    return controllerProduct.delete_product(mongo, data_decode)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)