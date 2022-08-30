import hmac
import datetime

from flask_login import login_user, current_user
from flask_restful import Resource
from flask import request

from utils.response.messages import *
from utils.auth.manager import login_required
from utils.generator.username import generate_username
from utils.auth.roles import role_enum

from schemas.user import UserSchema
from schemas.order import OrderSchema
from models.user import UserModel
from models.order import OrderModel

user_schema = UserSchema()
order_list_schema = OrderSchema(many=True, exclude=("customer","customer_id"))

class CustomerRegister(Resource):
    @classmethod
    def post(cls):
        customer = user_schema.load(request.get_json())
        customer.username = generate_username(customer.name)
        customer.role = role_enum["customer"]
        customer.created_at = datetime.datetime.now()

        if UserModel.find_by_email(customer.email):
            return {"message": EMAIL_ALREADY_EXISTS}, 400

        customer.save_to_db()

        return {"message": f"Hi {customer.name}, welcome to the application!!", "data": user_schema.dump(customer)}, 201


class CustomerLogin(Resource):
    @classmethod
    def post(cls):
        customer_data = user_schema.load(request.get_json(), partial=True)
        customer = UserModel.find_by_username(customer_data.username)

        if not customer:
            return {"message": INVALID_CREDENTIALS_USERNAME}, 400

        if not hmac.compare_digest(customer.password, customer_data.password):
            return {"message": INVALID_CREDENTIALS_PASSWORD}, 400

        login_user(customer)

        return {"message": f"Hi {customer.name}, welcome back!!", "data": user_schema.dump(customer)}, 200


class Customer(Resource):
    @classmethod
    @login_required("customer")
    def get(cls):
        print("hi")
        return {"message": "called"}


class CustomerOrder(Resource):
    @classmethod
    @login_required("customer")
    def get(cls):
        return {"data": order_list_schema.dump(OrderModel.find_all_by_customer_id(current_user.id))}, 200
