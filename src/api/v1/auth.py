from fastapi import APIRouter

from api.dependencies.auth.backend import auth_backend
from api.dependencies.auth.fastapi_users_router import fastapi_users
from core.config import settings


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=['Auth'],
)
router.include_router(router=fastapi_users.get_auth_router(auth_backend))