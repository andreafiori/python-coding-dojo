import unittest

from python_algorithms.design_patterns.behavioral.strategy import Order, on_sale_discount, ten_percent_discount


class StrategyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.order = Order(100)

    def test_price_After_discount(self):
        self.assertEqual(self.order.price_after_discount(), 100)

    def test_discount_strategy(self):
        order = Order(100, discount_strategy=ten_percent_discount)
        self.assertEqual(order.price_after_discount(), 90)

    def test_discount_strategy_discount_strategy(self):
        order = Order(1000, discount_strategy=on_sale_discount)
        self.assertEqual(order.price_after_discount(), 730.0)
