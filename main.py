from flask import Flask
from flask_pymongo import PyMongo
import pika
from src.config.config import Config
from src.controller.controller_category import ControllerCategory

app = Flask(__name__)
config = Config()

#configuration
parameters = pika.URLParameters(config.urlQueue)
connection = pika.BlockingConnection(parameters)

#configuration
app.config["MONGO_URI"] = config.urlDB
mongo = PyMongo(app)


controllerCategory = ControllerCategory()
@app.route("/")
def hello_world():
    # channel = connection.channel()
    # channel.queue_declare(queue="messages")
    # channel.basic_publish(exchange='', routing_key="messages", body='Text')
    # connection.close()

    # Access the "users" collection in MongoDB
    users_collection = mongo.db.roles

    # Query all documents in the "users" collection
    users = users_collection.find()

    # Convert MongoDB cursor to a list of dictionaries
    users_list = list(users)
    print(users_list)
    return "<p>Hello, World! 101</p>"


if __name__ == "__main__":
    controllerCategory.createCategory()
    app.run(host='0.0.0.0', port=8082)