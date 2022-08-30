import hmac

from flask_login import login_user
from flask_restful import Resource
from flask import request

from utils.response.messages import *
from utils.auth.manager import login_required
from utils.generator.username import generate_username
from utils.auth.roles import role_enum

from schemas.user import UserSchema
from models.user import UserModel

user_schema = UserSchema()


class CustomerRegister(Resource):
    @classmethod
    def post(cls):
        customer = user_schema.load(request.get_json())
        customer.username = generate_username(customer.name)
        customer.role = role_enum["customer"]

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
