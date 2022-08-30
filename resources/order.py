from flask_login import current_user
from flask_restful import Resource
from flask import request

from schemas.order import OrderSchema
from models.order import OrderModel
from utils.auth.manager import login_required
from utils.response.messages import *

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)


class Order(Resource):
    @classmethod
    @login_required("customer")
    def post(cls):
        order = order_schema.load(request.get_json())
        print(current_user.id)
