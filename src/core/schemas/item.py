from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    foo: int
    bar: int


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
