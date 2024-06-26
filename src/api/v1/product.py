from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from db.schemas import ProductResponse

router = APIRouter()


@router.post("/products/", response_model=ProductResponse)
async def create_product(
    product,
    db: AsyncSession = Depends(get_db),
):
    pass


@router.post(
    "/products/{product_id}/aggregate",
    response_model=ProductResponse,
)
async def aggregate_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
):
    pass
