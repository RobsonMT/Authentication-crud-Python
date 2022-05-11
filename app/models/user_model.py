from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    last_name: str
    email: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(127), nullable=False)
    last_name = Column(String(511), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(511))

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
