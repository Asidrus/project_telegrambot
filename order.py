from dataclasses import dataclass, field
from enum import Enum


class OrderStatus(Enum):
    cooking = "cooking"
    onTheWay = "on the way"
    delivered = "delivered"


@dataclass
class Order:
    id: int = field(default=None)
    status: OrderStatus = field(default=None)
    address: str = field(default=None)
    phone: str = field(default=None)


order = Order()


if __name__ == "__main__":
    print(OrderStatus.onTheWay.value)