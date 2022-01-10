from pydantic import BaseModel

from app.schemas.hero import Hero
from app.schemas.user import User

class PickBase(BaseModel):
    hero_id: int
    user_id: int
    team_id: int
    
class PickCreate(PickBase):
    hero_id: int
    user_id: int
    team_id: int
class PickUpdate(PickBase):
    hero_id: int
    user_id: int
    team_id: int
class PickInDBBase(PickBase):
    id: int
    hero_id: int
    user_id: int
    team_id: int
    user: User
    hero: Hero
    class Config:
        orm_mode = True
        
class Pick(PickInDBBase):
    pass

class PickInDB(PickInDBBase):
    pass