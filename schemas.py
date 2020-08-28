from pydantic import BaseModel
from typing import Optional


class PetBase(BaseModel):
    name: str
    kind: str
    color: str
    

class PetCreate(PetBase):
    ...


class PetUpdate(PetBase):
    name: Optional[str]
    kind: Optional[str]
    color: Optional[str]


class Pet(PetBase):
    id: int
    

    class Config:
        orm_mode = True
   


