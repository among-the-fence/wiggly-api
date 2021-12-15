from pydantic import BaseModel

class UserBase(BaseModel):
    did = int
    rating = float
    confidence = float
        
class UserCreate(UserBase):
    did = int
    rating = float
    confidence = float
    
class UserUpdate(UserBase):
    did = int
    rating = float
    confidence = float
    
class UserInDBBase(UserBase):
    id: int
    class Config:
        orm_mode = True
        
class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    pass