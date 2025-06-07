from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_tasks():
    return [{"id": 1, "title": "Ejemplo"}]