from typing import List
from db.conn import db


class AdminModel(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime())

    @classmethod
    def find_by_id(cls, id: int) -> "AdminModel":
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls) -> List["AdminModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


    