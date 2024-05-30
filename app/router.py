from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Pets
from typing import List
import schemas as schemas

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[schemas.Pets])
async def get_pets(db: Session = Depends(get_db)):
    pets = db.query(Pets).all()
    return pets

@router.get("/{id}", response_model=schemas.Pets | None)
async def get_pet_by_id(id: int, db: Session = Depends(get_db)):
    pet = db.query(Pets).filter(Pets.id == id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail="Not found")
    return pet