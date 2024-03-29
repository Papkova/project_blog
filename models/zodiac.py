from sqlalchemy import Column, Integer, String
from .database import Base
from flask_login import UserMixin


class Zodiac(UserMixin, Base):
    __tablename__ = "zodiacs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String(20), unique=True, nullable=False)

    def __init__(self, name: str, username: str):
        self.name = name
        self.username = username
