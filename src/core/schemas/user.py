from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserBase:
    is_staff: bool


class UserRead(schemas.BaseUser[UserIdType], UserBase):
    pass


class UserCreate(schemas.BaseUserCreate, UserBase):
    pass


class UserUpdate(schemas.BaseUserUpdate, UserBase):
    pass
