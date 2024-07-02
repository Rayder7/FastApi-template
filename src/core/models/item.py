from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


class Item(IntIdPkMixin, Base):
    """Шаблон создания модели"""
    name: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (
        UniqueConstraint('foo', 'bar'),
    )