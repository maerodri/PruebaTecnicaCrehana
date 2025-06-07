from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from infrastructure.models import List

async def get_all_lists(db: AsyncSession):
    result = await db.execute(select(List))
    return result.scalars().all()

async def create_list(db: AsyncSession, name: str):
    new_list = List(name=name)
    db.add(new_list)
    await db.commit()
    await db.refresh(new_list)
    return new_list
