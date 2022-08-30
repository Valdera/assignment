import hmac
import datetime

from flask_login import login_user
from flask_restful import Resource
from flask import request

from utils.response.messages import *
from utils.auth.manager import login_required
from utils.generator.username import generate_username
from utils.auth.roles import role_enum

from schemas.user import UserSchema
from models.user import UserModel

user_schema = UserSchema()


class AdminRegister(Resource):
    @classmethod
    def post(cls):
        admin = user_schema.load(request.get_json())
        admin.username = generate_username(admin.name)
        admin.role = role_enum["admin"]
        admin.created_at = datetime.datetime.now()

        if UserModel.find_by_email(admin.email):
            return {"message": EMAIL_ALREADY_EXISTS}, 400

        admin.save_to_db()

        return {"message": f"Hi {admin.name}, welcome to the application!!", "data": user_schema.dump(admin)}, 201


class AdminLogin(Resource):
    @classmethod
    def post(cls):
        admin_data = user_schema.load(request.get_json(), partial=True)
        admin = UserModel.find_by_username(admin_data.username)

        if not admin:
            return {"message": INVALID_CREDENTIALS_USERNAME}, 400

        if not hmac.compare_digest(admin.password, admin_data.password):
            return {"message": INVALID_CREDENTIALS_PASSWORD}, 400

        login_user(admin)

        return {"message": f"Hi {admin.name}, welcome back!!", "data": user_schema.dump(admin)}, 200
