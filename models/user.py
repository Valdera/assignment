from typing import List
from db.conn import db
from flask_login import UserMixin
import hmac


class CustomerModel(db.Model, UserMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50))
    address = db.Column(db.String(100))

    orders = db.relationship(
        "OrderModel", back_populates="customer", lazy="dynamic")

    @classmethod
    def find_by_id(cls, id: int) -> "CustomerModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email: str) -> "CustomerModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username: str) -> "CustomerModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def authenticate(cls, username: str, password: str) -> "CustomerModel":
        customer = cls.query.filter_by(username=username).first()

        if customer and hmac.compare_digest(customer.password, password):
            return customer

    @classmethod
    def find_all(cls) -> List["CustomerModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
