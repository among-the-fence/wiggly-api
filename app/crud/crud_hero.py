from app.crud.base import CRUDBase
from app.models.hero import Hero
from app.schemas.hero import HeroCreate, HeroUpdate

class CRUDHero(CRUDBase[Hero, HeroCreate, HeroUpdate]):
    ...
    
hero = CRUDHero(Hero)