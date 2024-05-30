from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    type = Column(String, unique=True, index=True)
    sound = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())