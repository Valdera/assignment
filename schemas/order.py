from utils.serializer.ma import ma

from schemas.book import BookSchema
from schemas.customer import CustomerSchema

from models.order import OrderModel

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class OrderSchema(ma.SQLAlchemyAutoSchema):
    customer = ma.Nested(CustomerSchema, many=True)
    book = ma.Nested(BookSchema, many=True)

    class Meta:
        model = OrderModel
        load_instance = True
        dump_only = ("id",)
        include_fk = True
