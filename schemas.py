from pydantic import BaseModel


class PetBase(BaseModel):
    name: str
    kind: str
    color: str
    

class PetCreate(PetBase):
    ...

class Pet(PetBase):
    id: int
    

    class Config:
        orm_mode = True
   


