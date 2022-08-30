from flask_login import current_user
from flask_restful import Resource
from flask import request

import datetime

from schemas.order import OrderSchema
from models.order import OrderModel
from models.book import BookModel
from utils.auth.manager import login_required
from utils.response.messages import *

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)


class Order(Resource):
    @classmethod
    @login_required()
    def post(cls):
        order = order_schema.load(request.get_json())
        order.customer_id = current_user.id
        order.created_at = datetime.datetime.now()
        
        if not BookModel.find_by_id(order.book_id):
            return ITEM_NOT_FOUND, 400

        order.save_to_db()

        return {"data": order_schema.dump(order)}, 201
