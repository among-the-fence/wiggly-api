from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Hero(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    localized_name = Column(String(256), nullable=False)
    picker = relationship("Pick", cascade="all", back_populates="hero")