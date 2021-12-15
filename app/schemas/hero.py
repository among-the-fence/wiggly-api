from pydantic import BaseModel

class HeroBase(BaseModel):
    name : str
    localized_name: str
    
class HeroCreate(HeroBase):
    name: str
    localized_name: str
    
class HeroUpdate(HeroBase):
    name: str
    localized_name: str
    
class HeroInDBBase(HeroBase):
    id: int
    class Config:
        orm_mode = True
        
class Hero(HeroInDBBase):
    pass

class HeroInDB(HeroInDBBase):
    pass