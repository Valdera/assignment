from typing import List
from db.conn import db


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))

    customer = db.relationship("CustomerModel", back_populates="orders")
    book = db.relationship("BookModel", back_populates="orders")

    @classmethod
    def find_by_id(cls, id: int) -> "OrderModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all_by_customer_id(cls, id: int) -> List["OrderModel"]:
        return cls.query.filter_by(customer_id=id).all()

    @classmethod
    def find_all(cls) -> List["OrderModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
