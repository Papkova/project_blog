from sqlalchemy import Column, Integer, String
from .database import Base
from flask_login import UserMixin
from sqlalchemy.orm import relationship


class Sing(UserMixin, Base):
    __tablename__ = "sings"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password = Column(String(60), nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'Sing({self.username}, {self.email}, {self.image_file})'