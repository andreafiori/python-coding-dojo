import unittest
from src.python_algorithms.design_patterns.behavioral.chain_of_responsibility import ConcreteHandler0, ConcreteHandler1, ConcreteHandler2, FallbackHandler

class ChainOfResponsabilityTest(unittest.TestCase):
    def setUp(self) -> None:
        self.h0 = ConcreteHandler0()
        self.h1 = ConcreteHandler1()
        self.h2 = ConcreteHandler2(FallbackHandler())

        self.h0.successor = self.h1
        self.h1.successor = self.h2

    def test_request(self):
        requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
        for request in requests:
            self.h0.handle(request)
