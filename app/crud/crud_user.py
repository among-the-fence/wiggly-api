from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from typing import Any

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    ...
    def get_by_shortname(self, db: Session, shortname: str):
        return db.query(self.model).filter(self.model.shortname == shortname).first()
user = CRUDUser(User)