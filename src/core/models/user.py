from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean

from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base, SQLAlchemyBaseUserTable[int]):
    is_staff: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
