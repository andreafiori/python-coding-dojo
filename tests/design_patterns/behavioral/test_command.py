import pytest
from src.python_algorithms.design_patterns.behavioral.command import MenuItem, DeleteFileCommand, HideFileCommand

@pytest.fixture
def item1():
    """Provide a fresh item1 instance for each test."""
    return MenuItem(DeleteFileCommand())

@pytest.fixture
def item2():
    """Provide a fresh item2 instance for each test."""
    return MenuItem(HideFileCommand())

class TestChainingMethod:
    def test_deleting_test_file_value(self, item1):
        assert item1.on_do_press('test-file') == 'deleting test-file'

    def test_restore_test_file_value(self, item1):
        item1.on_do_press('test-file')
        assert item1.on_undo_press() == 'restoring test-file'

    def test_restoring_test_file_value_from_item2(self, item2):
        assert item2.on_do_press('test-file') == 'hiding test-file'

    def test_hiding_test_file_value_from_item2(self, item2):
        item2.on_do_press('test-file')
        assert item2.on_undo_press() == 'un-hiding test-file'
