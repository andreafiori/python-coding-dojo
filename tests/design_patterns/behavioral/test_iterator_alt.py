import unittest

from src.python_algorithms.design_patterns.behavioral.iterator_alt import NumberWords


class IteratorAltTest(unittest.TestCase):
    def test_number_words_two(self):
        self.assertEqual(_build_sample_dictionary(1, 2), ['one', 'two'])

    def test_number_words_five(self):
        self.assertEqual(_build_sample_dictionary(1, 5), ['one', 'two', 'three', 'four', 'five'])

def _build_sample_dictionary(start, stop):
    """
    Build a dictionary with the generator values
    :param start: int
    :param stop: int
    :return: dictionary
    """
    generator_list = []
    for number in NumberWords(start, stop):
        generator_list.append(number)
    return generator_list
