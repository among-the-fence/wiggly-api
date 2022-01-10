from pydantic import BaseModel

class TeamBase(BaseModel):
    name : str
    
class TeamCreate(TeamBase):
    name: str
    
class TeamUpdate(TeamBase):
    name: str
    
class TeamInDBBase(TeamBase):
    id: int
    class Config:
        orm_mode = True
        
class Team(TeamInDBBase):
    pass

class TeamInDB(TeamInDBBase):
    pass