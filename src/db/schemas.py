from datetime import datetime, date
from pydantic import BaseModel, Field


class BatchCreate(BaseModel):
    status_closure: bool = Field(..., alias="СтатусЗакрытия")
    task_representation: str = Field(..., alias="ПредставлениеЗаданияНаСмену")
    line: str = Field(..., alias="Линия")
    shift: str = Field(..., alias="Смена")
    team: str = Field(..., alias="Бригада")
    batch_id: int = Field(..., alias="НомерПартии")
    batch_date: date = Field(..., alias="ДатаПартии")
    nomenclature: str = Field(..., alias="Номенклатура")
    ekn_code: str = Field(..., alias="КодЕКН")
    rc_identifier: str = Field(..., alias="ИдентификаторРЦ")
    start_datetime: datetime = Field(..., alias="ДатаВремяНачалаСмены")
    end_datetime: datetime = Field(..., alias="ДатаВремяОкончанияСмены")

    class Config:
        allow_population_by_field_name = True


class BatchResponse(BaseModel):

    status_closure: bool
    task_representation: str
    line: str
    shift: str
    team: str
    batch_id: int
    batch_date: date
    nomenclature: str
    ekn_code: str
    rc_identifier: str
    start_datetime: datetime
    end_datetime: datetime
    closed_at: datetime | None

    class Config:
        orm_mode = True


class ProductResponse(BaseModel):
    unique_code: str
    batch_id: int
    batch_date: date
    is_aggregated: bool
    aggregated_at: datetime | None

    class Config:
        orm_mode = True
