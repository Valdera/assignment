from utils.serializer.ma import ma
from models.book import BookModel
from models.order import OrderModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class BookSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = BookModel
        load_instance = True
        dump_only = ("id",)
        include_fk = True
