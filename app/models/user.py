from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import BigInteger, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    did = Column(BigInteger, nullable=False, index=True)
    rating = Column(Float, index=True)
    confidence = Column(Float, index=True)
    shortname = Column(String(64))
    picks = relationship("Pick", cascade="all", back_populates="user")