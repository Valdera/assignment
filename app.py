from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from marshmallow import ValidationError

from config import config
from db.conn import db
from utils.auth.manager import login_manager
from utils.serializer.ma import ma

from models.user import UserModel

from resources.admin import AdminRegister, AdminLogin
from resources.book import Book, BookItem, BookAdmin, BookItemAdmin
from resources.customer import CustomerLogin, CustomerRegister, CustomerOrder
from resources.order import Order

app = Flask(__name__)

app.config.from_object(config)
api = Api(app)
migrate = Migrate(app, db)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@login_manager.user_loader
def load_user(id: str):
    return UserModel.query.get(int(id))

@login_manager.unauthorized_handler
def unauth_handler():
    return {"message": "You do not have the permissions. Please login to authorized role first"}, 401


api.add_resource(CustomerRegister, "/customer/register")
api.add_resource(CustomerLogin, "/customer/login")
api.add_resource(CustomerOrder, "/customer/orders")
api.add_resource(AdminRegister, "/admin/register")
api.add_resource(AdminLogin, "/admin/login")
api.add_resource(BookAdmin, "/admin/ebook")
api.add_resource(BookItemAdmin, "/admin/ebook/<int:id>")
api.add_resource(Book, "/ebook")
api.add_resource(BookItem, "/ebook/<int:id>")
api.add_resource(Order, "/order")

db.init_app(app)
ma.init_app(app)
login_manager.init_app(app)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
