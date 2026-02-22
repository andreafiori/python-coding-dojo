import pytest

from unittest.mock import patch, Mock
from src.python_algorithms.design_patterns.behavioral.observer import Data, DecimalViewer, HexViewer


@pytest.fixture
def observable():
    return Data('some data')

def test_attach_detach(observable):
    decimal_viewer = DecimalViewer()
    assert len(observable._observers) == 0

    observable.attach(decimal_viewer)
    assert decimal_viewer in observable._observers

    observable.detach(decimal_viewer)
    assert decimal_viewer not in observable._observers

def test_one_data_change_notifies_each_observer_once(observable):
    observable.attach(DecimalViewer())
    observable.attach(HexViewer())

    with patch('src.python_algorithms.design_patterns.behavioral.observer.DecimalViewer.update', new_callable=Mock()) as mocked_update:
        assert mocked_update.call_count == 0
        observable.data = 10
        assert mocked_update.call_count == 1

"""
>>> data1 = Data('Data 1')
>>> data2 = Data('Data 2')
>>> view1 = DecimalViewer()
>>> view2 = HexViewer()
>>> data1.attach(view1)
>>> data1.attach(view2)
>>> data2.attach(view2)
>>> data2.attach(view1)

>>> data1.data = 10
DecimalViewer: Subject Data 1 has data 10
HexViewer: Subject Data 1 has data 0xa

>>> data2.data = 15
HexViewer: Subject Data 2 has data 0xf
DecimalViewer: Subject Data 2 has data 15

>>> data1.data = 3
DecimalViewer: Subject Data 1 has data 3
HexViewer: Subject Data 1 has data 0x3

>>> data2.data = 5
HexViewer: Subject Data 2 has data 0x5
DecimalViewer: Subject Data 2 has data 5

# Detach HexViewer from data1 and data2
>>> data1.detach(view2)
>>> data2.detach(view2)

>>> data1.data = 10
DecimalViewer: Subject Data 1 has data 10

>>> data2.data = 15
DecimalViewer: Subject Data 2 has data 15
"""
