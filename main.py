from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
import pika, json
from src.config.config import Config
from src.controller.controller_category import ControllerCategory

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
config = Config()

#configuration
parameters = pika.URLParameters(config.urlQueue)
connection = pika.BlockingConnection(parameters)

#configuration
app.config["MONGO_URI"] = config.urlDB
mongo = PyMongo(app)


controllerCategory = ControllerCategory()

@app.route("/category_update", methods=['PATCH'])
def update_category():
    data = request.data
    data_decode = data.decode("utf-8")
    print(data_decode)
    return jsonify({"status": True, "message": 'update category success'})

@app.route("/category_delete", methods=['DELETE'])
def delete_category():
    data = request.data
    data_decode = data.decode("utf-8")
    print(data_decode)
    return jsonify({"status": True, "message": 'update category success'})

@app.route("/category", methods=["POST"])
def create_category():
    body = request.data
    category = body.decode("utf-8")
    controllerCategory.createCategory(mongo, category)
    return jsonify({"status": True, "message": 'create category success'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)