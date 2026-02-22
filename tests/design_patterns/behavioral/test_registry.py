import unittest

from src.python_algorithms.design_patterns.behavioral.registry import RegistryHolder, BaseRegisteredClass

class ClassRegistree(BaseRegisteredClass):
    def __init__(self, *args, **kwargs):
        pass

class RegistryTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_before_subclassing(self):
        self.assertEqual(sorted(RegistryHolder.REGISTRY), ['BaseRegisteredClass', 'ClassRegistree'])
