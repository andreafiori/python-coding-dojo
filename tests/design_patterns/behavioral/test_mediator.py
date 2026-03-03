import unittest

from python_algorithms.design_patterns.behavioral.mediator import User, ChatRoom


class IteratorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.molly = User('Molly')
        self.mark = User('Mark')
        self.ethan = User('Ethan')

    def test_molly_says(self):
        msg = "Hi Team! Meeting at 3 PM today."
        self.assertEqual(self.molly.say(msg), '[Molly says]: '+msg)

    def test_mark_says(self):
        msg = "Roger that!"
        self.assertEqual(self.mark.say(msg), '[Mark says]: '+msg)

    def test_ethan_says(self):
        msg = "Alright."
        self.assertEqual(self.ethan.say(msg), '[Ethan says]: '+msg)
