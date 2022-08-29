from flask import Flask, jsonify
from flask_login_multi.login_manager import LoginManager
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from config import config
from db.conn import db
from utils.serializer.ma import ma

from models.admin import AdminModel
from models.user import CustomerModel

from resources.user import CustomerLogin, CustomerRegister

app = Flask(__name__)
login_manager = LoginManager()

app.config.from_object(config)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@login_manager.user_loader
def load_user(id: str, endpoint: str):
    print(endpoint)
    if endpoint == 'admin':
        return AdminModel.query.get(int(id))
    else:
        return CustomerModel.query.get(int(id))


# jwt = JWTManager(app)

api.add_resource(CustomerRegister, "/customer/register")
api.add_resource(CustomerLogin, "/customer/login")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)
    app.run(port=5000, debug=True)
