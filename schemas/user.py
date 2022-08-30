
from utils.serializer.ma import ma

from marshmallow import fields

from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    email = fields.Email()
    username = fields.String()
    role = fields.Integer()

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("password",)
        dump_only = ("id",)
        include_fk = True
