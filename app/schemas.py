from pydantic import BaseModel
from datetime import datetime

class PetsBase(BaseModel):
    name: str
    type: str
    sound: str | None

class PetsCreate(PetsBase):
    pass

class Pets(PetsBase):
    id: int
    created_at: datetime
    updated_at: datetime 