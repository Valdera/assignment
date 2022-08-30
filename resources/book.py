from flask_restful import Resource
from flask import request

from schemas.book import BookSchema
from models.book import BookModel
from utils.auth.manager import login_required
from utils.response.messages import *

book_schema = BookSchema()
book_list_schema = BookSchema(many=True)


class BookAdmin(Resource):
    @classmethod
    @login_required("admin")
    def post(cls):
        book = book_schema.load(request.get_json())
        book.save_to_db()
        return {"data": book_schema.dump(book)}, 201

    @classmethod
    @login_required("admin")
    def get(cls):
        return {"data": book_list_schema.dump(BookModel.find_all())}, 200


class BookItemAdmin(Resource):
    @classmethod
    @login_required("admin")
    def get(cls, id: int):
        book = BookModel.find_by_id(id)
        if not book:
            return {"message": ITEM_NOT_FOUND}, 404
        return {"data": book_schema.dump(book)}, 200

    @classmethod
    @login_required("admin")
    def put(cls, id: int):
        book_data = book_schema.load(request.get_json())

        book = BookModel.find_by_id(id)
        if not book:
            return {"message": ITEM_NOT_FOUND}, 404

        book.title = book_data.title
        book.author = book_data.author
        book.synopsis = book_data.synopsis
        book.price = book_data.price
        book.image_url = book_data.image_url
        book.content_url = book_data.content_url

        book.save_to_db()

        return {"data": book_schema.dump(book)}, 201

    @classmethod
    @login_required("admin")
    def delete(cls, id: int):
        book = BookModel.find_by_id(id)
        if not book:
            return {"message": ITEM_NOT_FOUND}, 404

        book.delete_from_db()

        return {"message": ITEM_DELETED}


class Book(Resource):
    @classmethod
    def get(cls):
        return {"data": book_list_schema.dump(BookModel.find_all())}, 200


class BookItem(Resource):
    @classmethod
    def get(cls, id: int):
        book = BookModel.find_by_id(id)
        if not book:
            return {"message": ITEM_NOT_FOUND}, 404
        return {"data": book_schema.dump(book)}, 200
