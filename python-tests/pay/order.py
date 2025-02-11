from dataclasses import dataclass


@dataclass
class OrderLine:
    product_id: int
    unit_price: float
    num_of_units: int = 1


    @property
    def line_amount(self):
        return self.num_of_units * self.unit_price


@dataclass
class Order:
    order_id: int
    order_lines: list[OrderLine]


    @property
    def total(self):
        return sum(line.line_amount for line in self.order_lines)