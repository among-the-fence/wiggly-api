from app.crud.base import CRUDBase
from app.models.hero import Hero
from app.schemas.hero import HeroCreate, HeroUpdate
from sqlalchemy.orm import Session
from typing import Any

class CRUDHero(CRUDBase[Hero, HeroCreate, HeroUpdate]):
    ...
    def get_by_name(self, db: Session, name: str):
        return db.query(self.model).filter(self.model.localized_name == name).first()
hero = CRUDHero(Hero)