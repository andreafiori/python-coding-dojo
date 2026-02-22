from src.python_algorithms.algorithms.strings.string_util import StringUtil

class TestStringUtil:
    def test_is_palindrom_is_true(self):
        assert StringUtil.is_palindrome('deified')

    def test_is_palindrom_is_false(self):
        assert not StringUtil.is_palindrome('asso')

    def test_reverse(self):
        assert StringUtil.reverse('hello world') == 'dlrow olleh'
