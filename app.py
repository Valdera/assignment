from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from config import config
from db.conn import db
from resources.book import BookAdmin, BookItemAdmin
from utils.auth.manager import login_manager
from utils.serializer.ma import ma

from models.user import UserModel

from resources.customer import Customer, CustomerLogin, CustomerRegister

app = Flask(__name__)

app.config.from_object(config)
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@login_manager.user_loader
def load_user(id: str):
    return UserModel.query.get(int(id))


api.add_resource(CustomerRegister, "/customer/register")
api.add_resource(CustomerLogin, "/customer/login")
api.add_resource(AdminRegister)
api.add_resource(Customer, "/customer")
api.add_resource(BookAdmin, "/admin/ebook")
api.add_resource(BookItemAdmin, "/admin/ebook/<int:id>")
api.add_resource()

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)
    app.run(port=5000, debug=True)
