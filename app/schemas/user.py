from pydantic import BaseModel

class UserBase(BaseModel):
    did: int
    rating: float
    confidence: float
    shortname: str
        
class UserCreate(UserBase):
    did: int
    rating: float
    confidence: float
    shortname: str
    class Config:
        orm_mode = True
    
class UserUpdate(UserBase):
    did: int
    rating: float
    confidence: float
    shortname: str
    
class UserInDBBase(UserBase):
    id: int
    class Config:
        orm_mode = True
        
class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass