from utils.serializer.ma import ma

from schemas.book import BookSchema
from schemas.user import UserSchema

from models.order import OrderModel

from marshmallow import fields


class OrderSchema(ma.SQLAlchemyAutoSchema):
    customer_id = fields.Integer()

    customer = ma.Nested(UserSchema)
    book = ma.Nested(BookSchema)

    class Meta:
        model = OrderModel
        load_instance = True
        dump_only = ("id",)
        include_fk = True
