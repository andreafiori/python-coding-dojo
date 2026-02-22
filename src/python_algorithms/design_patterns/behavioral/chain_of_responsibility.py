"""
*What is this pattern about?

The Chain of responsibility is an object oriented version of the
`if ... elif ... elif ... else ...` idiom, with the
benefit that the condition–action blocks can be dynamically rearranged
and reconfigured at runtime.

This pattern aims to decouple the senders of a request from its
receivers by allowing request to move through chained
receivers until it is handled.

Request receiver in simple form keeps a reference to a single successor.
As a variation some receivers may be capable of sending requests out
in several directions, forming a `tree of responsibility`.

*TL;DR
Allow a request to pass down a chain of receivers until it is handled.
"""

import abc


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        """
        Handle request and stop.
        If can't - call next handler in chain.

        As an alternative you might even in case of success call the next handler.
        """
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abc.abstractmethod
    def check_range(self, request):
        """Compare passed value to predefined interval"""


class ConcreteHandler0(Handler):
    """
    Each handler can be different.
    Be simple and static...
    """

    def check_range(self, request):
        """
        Check range
        :param request:
        :return:
        """

        if 0 <= request < 10:
            return "request {} handled in handler 0".format(request)


class ConcreteHandler1(Handler):
    """... With it's own internal state"""

    start, end = 10, 20

    def check_range(self, request):
        """
        Check range
        :param request:
        :return:
        """
        if self.start <= request < self.end:
            return "request {} handled in handler 1".format(request)


class ConcreteHandler2(Handler):
    """... With helper methods."""

    def check_range(self, request):
        """
        Check range
        :param request:
        :return:
        """
        start, end = self.get_interval_from_db()
        if start <= request < end:
            return "request {} handled in handler 2".format(request)

    @staticmethod
    def get_interval_from_db():
        return (20, 30)


class FallbackHandler(Handler):
    def check_range(self,  request):
        """
        Check range
        :param request:
        :return:
        """
        return("end of chain, no handler for {}".format(request))
