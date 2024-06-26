from typing import Annotated
from datetime import datetime, date
from sqlalchemy import DateTime, ForeignKey, text
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


intpk = Annotated[int, mapped_column(primary_key=True)]
default_date = Annotated[
    datetime,
    mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('utc', now())"),
    ),
]


class Batch(Base):
    __tablename__ = 'batches'

    id: Mapped[intpk]
    status_closure: Mapped[bool] = mapped_column(default=False)
    task_representation: Mapped[str]
    line: Mapped[str]
    shift: Mapped[str]
    team: Mapped[str]
    batch_id: Mapped[int] = mapped_column(unique=True)
    batch_date: Mapped[date]
    nomenclature: Mapped[str | None] = mapped_column(nullable=True)
    ekn_code: Mapped[str | None] = mapped_column(nullable=True)
    rc_identifier: Mapped[str | None] = mapped_column(nullable=True)
    start_datetime: Mapped[default_date]
    end_datetime: Mapped[default_date]
    closed_at: Mapped[datetime | None] = mapped_column(nullable=True)


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[intpk]
    unique_code: Mapped[int] = mapped_column(unique=True, nullable=False)
    batch_id: Mapped[int] = mapped_column(
        ForeignKey('batches.batch_id', ondelete='CASCADE')
    )
    batch_date: Mapped[date]
    is_aggregated: Mapped[bool] = mapped_column(default=False)
    aggregated_at: Mapped[datetime] = mapped_column(nullable=True)
