import unittest
from src.online.leetcode.add_binary import AddBinary

class TestAddBinary(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(AddBinary.solution("11", "1"), "100")
