import unittest
import pytest

from src.python_algorithms.design_patterns.behavioral.state import Radio


class StateTest(unittest.TestCase):
    def setUp(self) -> None:
        self.radio = Radio()

    def test_actions(self):
        actions = [self.radio.scan] * 2 + [self.radio.toggle_amfm] + [self.radio.scan] * 2
        actions *= 2
        action_list = []
        for action in actions:
            action_list.append( action() )
        self.assertEqual(action_list, self._get_expected_actions())

    def _get_expected_actions(self):
        return [
            'Scanning... Station is 1380 AM',
            'Scanning... Station is 1510 AM',
            'Switching to FM',
            'Scanning... Station is 89.1 FM',
            'Scanning... Station is 103.9 FM',
            'Scanning... Station is 81.3 FM',
            'Scanning... Station is 89.1 FM',
            'Switching to AM',
            'Scanning... Station is 1250 AM',
            'Scanning... Station is 1380 AM'
        ]

@pytest.fixture
def radio():
    return Radio()

def test_initial_state(radio):
    assert radio.state.name == 'AM'

def test_initial_am_station(radio):
    initial_pos = radio.state.pos
    assert radio.state.stations[initial_pos] == '1250'

def test_toggle_amfm(radio):
    assert radio.state.name == 'AM'

    radio.toggle_amfm()
    assert radio.state.name == 'FM'

    radio.toggle_amfm()
    assert radio.state.name == 'AM'
