from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from .database import Base
from datetime import datetime


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'Post({self.title})'