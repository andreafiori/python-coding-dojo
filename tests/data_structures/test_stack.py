import unittest
from python_algorithms.data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.stack.push(4)
        self.stack.push('dog')
        self.assertEqual(self.stack.peek(), 'dog')

    def test_size(self):
        self.stack.push(4)
        self.stack.push('dog')
        self.stack.push(True)
        self.assertEqual(self.stack.size(), 3)

    def test_pop(self):
        self.stack.push(4)
        self.stack.push('dog')
        self.stack.push(True)
        self.stack.push(8.4)
        self.assertEqual(self.stack.pop(), 8.4)
        self.assertEqual(self.stack.pop(), True)
        self.assertEqual(self.stack.pop(), 'dog')
