from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Match(Base):
    id = Column(Integer, primary_key=True, index=True)
    winner = Column(Integer)
    picks = relationship("Pick")
    