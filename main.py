from fastapi import FastAPI, HTTPException, Depends
from schemas import Pet, PetCreate
from typing import List

import models, schemas, crud
from sqlalchemy.orm import Session
from database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {"message": "Você vai conseguir! Foco!!"}

@app.get('/pets', response_model=List[Pet])
async def list_pets(kind: str = None, db: Session = Depends(get_db)):
    return crud.list_pets_with_filter(db, kind)

@app.get('/pets/{id}', response_model=Pet)
async def get_pet(id: int, db: Session = Depends(get_db)):
    pet_db = crud.get_pet(db, id)

    if pet_db:
        return pet_db

    raise HTTPException(status_code=404, detail="Pet not found")

@app.post('/pets', response_model=Pet)
async def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db, pet)
 