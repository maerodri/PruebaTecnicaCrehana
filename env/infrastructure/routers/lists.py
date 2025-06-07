from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database import SessionLocal
from infrastructure import repositories
from domain import schemas

router = APIRouter()

# Dependencia para obtener sesión de BD
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/", response_model=list[schemas.ListOut])
async def read_lists(db: AsyncSession = Depends(get_db)):
    return await repositories.get_all_lists(db)

@router.post("/", response_model=schemas.ListOut)
async def create_list(list_in: schemas.ListCreate, db: AsyncSession = Depends(get_db)):
    return await repositories.create_list(db, list_in.name)
