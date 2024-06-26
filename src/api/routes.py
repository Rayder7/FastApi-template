from fastapi import APIRouter
from api.v1 import batch, product


api_router = APIRouter()
api_router.include_router(batch.router, prefix="/batches", tags=["batches"])
api_router.include_router(
    product.router,
    prefix="/products",
    tags=["products"],
)
