from typing import List
from db.conn import db


class BookModel(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    synopsis = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    image_url = db.Column(db.Text(), nullable=False)
    content_url = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime())

    orders = db.relationship(
        "OrderModel", back_populates="book", lazy="dynamic")

    @classmethod
    def find_by_id(cls, id: int) -> "BookModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["BookModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
