from app.crud.base import CRUDBase
from app.models.pick import Pick
from app.schemas.pick import PickCreate, PickUpdate

class CRUDPick(CRUDBase[Pick, PickCreate, PickUpdate]):
    ...
    
pick = CRUDPick(Pick)