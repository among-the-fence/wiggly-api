from fastapi import FastAPI, APIRouter, Request, Depends
from app.schemas.hero import Hero
from app.schemas.user import User, UserCreate
from app.schemas.pick import Pick
from app.herodata import herodata
from app import crud
from sqlalchemy.orm import Session
from app import deps

app = FastAPI()

api_router = APIRouter()

@app.get("/", status_code=200)
async def root():
    return {"message": "WIGGLETIME"}


@app.get("/variable/{number}")
async def variable(number):
    return {"number": number}

@app.get("/hero/{hero_id}", status_code=200, response_model=Hero)
async def fetch_hero(
    hero_id: int,
    db: Session = Depends(deps.get_db),
    ):
    result = crud.hero.get(db=db, id=hero_id)
    if result:
        return result

@app.get("/pick/{pick_id}", status_code=200, response_model=Pick)
async def fetch_pick(
    pick_id: int,
    db: Session = Depends(deps.get_db),
    ):
    result = crud.pick.get(db=db, id=pick_id)
    if result:
        return result
    
@app.post("/user/", status_code=201, response_model=UserCreate)
async def create_user(
    user_in: UserCreate, 
    db: Session = Depends(deps.get_db),
    ):
    user = crud.user.create(db=db, obj_in=user_in)
    
    return user

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn,run(app, host="0.0.0.0", port=8001, log_level="debug")