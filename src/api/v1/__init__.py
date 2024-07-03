from fastapi import APIRouter

from core.config import settings
from .items import router as items_router
from .auth import router as auth_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(items_router)
router.include_router(auth_router)

