import pytest

from python_algorithms.algorithms.strings.balanced_parentheses import BalancedParentheses

@pytest.fixture
def balanced_parentheses():
    """Provide a fresh BalancedParentheses instance for each test."""
    return BalancedParentheses()

class TestBalancedParenthesis:
    def test_check(self, balanced_parentheses):
        assert balanced_parentheses.check('((()))')

    def test_check_fails(self, balanced_parentheses):
        assert not balanced_parentheses.check('(()')