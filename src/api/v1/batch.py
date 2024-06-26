from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.schemas import BatchCreate, BatchUpdate, BatchResponse


router = APIRouter()


@router.post("/batches/", response_model=BatchResponse)
async def create_or_update_batch(
    batch: BatchCreate,
    db: AsyncSession = Depends(get_db),
):
    pass


@router.get("/batches/{batch_id}", response_model=BatchResponse)
async def get_batch(batch_id: int, db: AsyncSession = Depends(get_db)):
    pass


@router.patch("/batches/{batch_id}", response_model=BatchResponse)
async def update_batch(
    batch_id: int,
    batch_update: BatchUpdate,
    db: AsyncSession = Depends(get_db),
):
    pass


@router.get("/batches/", response_model=List[BatchResponse])
async def get_batches(
    limit: int = 10,
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
):
    pass
