from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Pick(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="picks")
    hero_id = Column(Integer, ForeignKey("hero.id"), nullable=False)
    hero = relationship("Hero", back_populates="picker")
    match_id = Column(Integer, ForeignKey("match.id"))
    team_id = Column(Integer, ForeignKey("team.id"))
    team = relationship("Team", back_populates="picks")