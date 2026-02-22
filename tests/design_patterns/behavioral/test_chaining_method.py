import unittest
from src.python_algorithms.design_patterns.behavioral.chaining_method import Action, Person

class ChainingMethodTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person('Jack', Action('move'))
        self.action = self.person.do_action() # chaining object

    def test_get_amout(self):
        self.action.set_amount(5)
        self.assertEqual(self.action.get_amount(), 5)

    def test_action_stop(self):
        self.assertEqual(self.action.stop(), 'then stop')