from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Item
from core.schemas.item import ItemCreate


async def get_all_items(session: AsyncSession) -> Sequence:
    stmt = select(Item).order_by(Item.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_item(session: AsyncSession, item_create: ItemCreate) -> Item:
    item = Item(**item_create.model_dump())
    session.add(item)
    await session.commit()
    # await session.refresh(item)
    return item
