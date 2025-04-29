from dataclasses import dataclass


@dataclass
class Drink:
    name: str
    price: float
    size: str
    description: str
    customization: str = " "
    