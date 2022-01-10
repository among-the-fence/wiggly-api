import logging
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import base  # noqa: F401
from app.herodata import herodata

logger = logging.getLogger(__name__)

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
teams = [
    {
        "name": "Radiant"
    },
    {
        "name": "Dire"
    }
]
userdata = [
    {
        "did" : 137211044299931649,
        "shortname" : "poddo"
    },
    {
        "did": 137271699824443392,
        "shortname": "chu"
    },
    {
        "did": 875066225309405265,
        "shortname": "matty"
    },
    {
        "did": 137214796029231104,
        "shortname": "zao"
    },
    {
        "did": 137584696396742657,
        "shortname": "henry"
    },
    {
        "did": 137326911566249984,
        "shortname": "ching"
    },
    {
        "did": 137286850111995904,
        "shortname": "zubie"
    },
    {
        "did": 137291242131161088,
        "shortname": "dev"
    },
]

testpick = [
    {
        "user_id" : 1,
        "hero_id" : 10,
        "team_id" : 1
    },
    {
        "user_id" : 4,
        "hero_id" : 10,
        "team_id" : 2
    },
    {
        "user_id" : 1,
        "hero_id" : 56,
        "team_id" : 1
    },
    {
        "user_id" : 1,
        "hero_id" : 10,
        "team_id" : 1
    }
]

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    for team in teams:
        team_in = schemas.TeamCreate(
            name=team["name"]
        )
        crud.team.create(db, obj_in=team_in)
        
    for hero in herodata:
        hero_in = schemas.HeroCreate(
            id=hero["id"],
            name=hero["name"],
            localized_name=hero["localized_name"]
        )
        crud.hero.create(db, obj_in=hero_in)
        
    for user in userdata:
        user_in = schemas.UserCreate(
            did=user["did"],
            rating=25.000,
            confidence=8.333,
            shortname=user["shortname"]
        )
        crud.user.create(db, obj_in=user_in)
        
    for pick in testpick:
        pick_in = schemas.PickCreate(
            user_id=pick["user_id"],
            hero_id=pick["hero_id"],
            team_id=pick["team_id"]
        )
        crud.pick.create(db, obj_in=pick_in)
    
    print("Debug testing info\n")
    print(crud.pick.get(db=db, id=1).user.did)
    list = crud.user.get(db=db, id=1).picks
    for i in list:
        print(i.hero.localized_name)
    userlist = crud.hero.get(db=db, id=10).picker
    for i in userlist:
        print(i.user.shortname)
    print(crud.user.get_by_shortname(db=db, shortname="poddo").id)
    print(crud.hero.get_by_name(db=db, name="Crystal Maiden").name)
    print(crud.pick.get(db=db, id=2).team.name)