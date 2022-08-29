
from utils.serializer.ma import ma
from models.admin import AdminModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AdminSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdminModel
        load_instance = True
        load_only = ("password",)
        dump_only = ("id",)
        include_fk = True

 