"""
Objects in a system communicate through a Mediator instead of directly with each other.
This reduces the dependencies between communicating objects, thereby reducing coupling.

Encapsulates how a set of objects interact.
"""


class ChatRoom(object):
    """Mediator class"""
    @staticmethod
    def display_message(user, message):
        return "[{} says]: {}".format(user, message)


class User(object):
    """A class whose instances want to interact with each other"""

    def __init__(self, name):
        self.name = name

    def say(self, message):
        return ChatRoom.display_message(self, message)

    def __str__(self):
        return self.name
