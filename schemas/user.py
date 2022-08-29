
from utils.serializer.ma import ma

from marshmallow_sqlalchemy import auto_field
from marshmallow import fields

from models.user import CustomerModel
from models.order import OrderModel


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    email = fields.Email()
    username = fields.String()

    class Meta:
        model = CustomerModel
        load_instance = True
        load_only = ("password",)
        dump_only = ("id",)
        include_fk = True
