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

