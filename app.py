from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import config

from db.conn import db
from utils.serializer.ma import ma


app = Flask(__name__)

app.config.from_object(config)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
