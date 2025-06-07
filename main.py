from fastapi import FastAPI
from infrastructure.database import engine, Base
from infrastructure.routers import lists


app = FastAPI(title="TODO API")

# Crear las tablas al iniciar la app
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(lists.router, prefix="/lists", tags=["Lists"])