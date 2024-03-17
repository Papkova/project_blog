from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from .database import Base
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_manager



# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


class User(UserMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='default.jpg')
    password = Column(String(60), nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User({self.id}, {self.username}, {self.email}, {self.password}, {self.image_file})'

