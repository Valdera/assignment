from functools import partial
from flask_restful import Resource
from flask import request

from utils.errors.messages import *
from utils.generator.username import generate_username

from schemas.customer import CustomerSchema
from models.user import CustomerModel

customer_schema = CustomerSchema()


class CustomerRegister(Resource):
    @classmethod
    def post(cls):
        customer = customer_schema.load(request.get_json())
        customer.username = generate_username(customer.name)

        if CustomerModel.find_by_email(customer.email):
            return {"message": EMAIL_ALREADY_EXISTS}, 400

        customer.save_to_db()

        return {"message": f"Hi {customer.name}, welcome to the application!!", "data": customer_schema.dump(customer)}, 201


class CustomerLogin(Resource):
    @classmethod
    def post(cls):
        customer_data = customer_schema.load(request.get_json(), partial=True)
        customer = CustomerModel.authenticate(
            customer_data.username, customer_data.password)

        if not customer:
            return {"message": "wrong credentials!"}, 400

        return {"message": f"Hi {customer.name}, welcome back!!", "data": customer_schema.dump(customer)}, 200


class Customer(Resource):
    @classmethod
    def get(cls):
        print("hi")
        return {"message": "called"}
