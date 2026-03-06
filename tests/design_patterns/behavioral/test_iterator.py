import pytest

from python_algorithms.design_patterns.behavioral.iterator import count_to

@pytest.fixture
def generator_list():
    # Build a dictionary with the generator values
    generator_list = []
    for number in count_to(2):
        generator_list.append(number)
    return generator_list

class TestIterator:
    def test_generator(self, generator_list):
        assert generator_list == ['one', 'two']
