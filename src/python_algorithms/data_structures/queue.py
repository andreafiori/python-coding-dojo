"""
Queue management
"""


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """
        Enqueue element
        :param item:
        :return:
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Dequeue element
        :return:
        """
        return self.items.pop()

    def size(self):
        """
        Get elements size
        :return: int
        """
        return len(self.items)
