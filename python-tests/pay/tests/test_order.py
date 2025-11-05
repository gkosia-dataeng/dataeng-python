from pay.order import Order, OrderLine
import pytest 
from pytest import MonkeyPatch


def test_line_total() -> None:
    line  = OrderLine(1, 1, 100)

    assert line.line_total == 100


def test_invalid_unit_price():
    with pytest.raises(ValueError):
        invalid_line = OrderLine(1, -1, 100)

def test_order_total() -> None:
    order = Order(1,  [OrderLine(1, 2, 100), OrderLine(2, 2, 100)])
    assert order.total == 400


def test_product_exists(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(OrderLine, 'check_product_id', False)

    line = OrderLine(1,2,100)

    assert line.check_product_id
