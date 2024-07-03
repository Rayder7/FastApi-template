from typing import TYPE_CHECKING
from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy import Boolean

from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(IntIdPkMixin, Base, SQLAlchemyBaseUserTable[UserIdType]):
    is_staff: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
