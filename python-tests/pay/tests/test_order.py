from pay.order import Order, OrderLine



def test_line_amount() -> None:
    line  = OrderLine(1, 1, 100)

    assert line.line_amount == 100


def test_order_total() -> None:
    order = Order(1,  [OrderLine(1, 2, 100), OrderLine(2, 2, 100)])
    assert order.total == 401