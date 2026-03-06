"""
Implementation of the state pattern

https://en.wikipedia.org/wiki/State_pattern

The state pattern is a behavioral software design pattern that allows an object to alter its behavior when its internal
 state changes. This pattern is close to the concept of finite-state machines.
 The state pattern can be interpreted as a strategy pattern, which is able to switch a strategy through invocations
 of methods defined in the pattern's interface.
"""


class State:

    """Base state. This is to share functionality"""

    def __init__(self):
        self.stations = None
        self.name = None

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        return "Scanning... Station is {} {}".format(self.stations[self.pos], self.name)


class AmState(State):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        self.radio.state = self.radio.fmstate
        return "Switching to FM"


class FmState(State):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        self.radio.state = self.radio.amstate
        return "Switching to AM"


class Radio:
    """A radio. It has a scan button, and an AM/FM toggle switch."""

    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        return self.state.toggle_amfm()

    def scan(self):
        return self.state.scan()
