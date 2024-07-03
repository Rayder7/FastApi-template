from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.crud.items import (
    get_all_items,
    create_item,
)
from core.config import settings
from core.models import (
    db_helper,
    Item,
)
from core.schemas.item import (
    ItemRead,
    ItemCreate,
)


router = APIRouter(
    prefix=settings.api.v1.items,
    tags=['Items'],
)


@router.get('', response_model=list[ItemRead])
async def get_items(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],):
    items = await get_all_items(session=session)
    return items


@router.post('', response_model=ItemRead)
async def add_item(
    item_create: ItemCreate,
    session: Annotated[
        AsyncSession,
        Depends(
            db_helper.session_getter
        ),
    ],
) -> Item:
    item = await create_item(session=session, item_create=item_create)
    return item
