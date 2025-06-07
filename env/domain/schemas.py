from pydantic import BaseModel
from typing import Optional

class ListCreate(BaseModel):
    name: str

class ListOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Esto permite usar SQLAlchemy con Pydantic
