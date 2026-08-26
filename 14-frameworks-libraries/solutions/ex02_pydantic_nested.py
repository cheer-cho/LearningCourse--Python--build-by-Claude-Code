from pydantic import BaseModel, Field, TypeAdapter


class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


class Order(BaseModel):
    id: int
    items: list[Item]

    @property
    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)


def load_orders(json_text: str) -> list[Order]:
    return TypeAdapter(list[Order]).validate_json(json_text)
