from dataclasses import dataclass



class OrderLine:

    def __init__ (self, product_id, unit_price, num_of_units):

        if unit_price < 0:
            raise ValueError(f"unit_price cannot be negative {unit_price=}")

        self.product_id = product_id
        self.unit_price = unit_price
        self.num_of_units = num_of_units


    def check_product_id(self) -> bool:
        # check if product id exists
        if self.product_id > 0:
            return True
        else:  
            return False

    @property
    def line_total(self):
        return self.num_of_units * self.unit_price


@dataclass
class Order:
    order_id: int
    order_lines: list[OrderLine]


    @property
    def total(self):
        return sum(line.line_total for line in self.order_lines)