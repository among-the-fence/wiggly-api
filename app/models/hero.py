from sqlalchemy import Column, Integer, String

from app.db.base_class import Base

class Hero(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    localized_name = Column(String(256), nullable=False)