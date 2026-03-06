import pytest

from python_algorithms.data_structures.date_utils import DateUtils

@pytest.fixture
def date_utils():
    """Provide DateUtils class reference."""
    return DateUtils

class TestDateUtils:
    """Test suite for DateUtils leap year logic."""

    @pytest.mark.parametrize("year,expected", [
        (2024, True),   # Divisible by 4, not by 100
        (2020, True),   # Divisible by 4, not by 100
        (2016, True),   # Divisible by 4, not by 100
        (2000, True),   # Divisible by 400
        (1996, True),   # Divisible by 4, not by 100

        (2023, False),  # Not divisible by 4
        (2022, False),  # Not divisible by 4
        (2021, False),  # Not divisible by 4

        (1900, False),  # Divisible by 100 but not 400
        (2100, False),  # Divisible by 100 but not 400
        (1800, False),  # Divisible by 100 but not 400

        (1600, True),   # Divisible by 400
        (2008, True),   # Divisible by 4, not by 100
    ])
    def test_is_leap_year_correctness(self, date_utils, year, expected):
        """Test leap year logic against Gregorian calendar rules."""
        assert date_utils.is_leap_year(year) == expected

    @pytest.mark.parametrize("year,expected", [
        (0, True),      # Year 0: divisible by 400
        (4, True),      # Smallest positive leap year
        (-4, True),     # Negative divisible by 400 (proleptic)
    ])
    def test_is_leap_year_edge_cases(self, date_utils, year, expected):
        """Test edge cases including year 0 and negatives."""
        assert date_utils.is_leap_year(year) == expected

    @pytest.mark.parametrize("year", [
        2017, 2019, 2021, 2025,  # Not divisible by 4
        1700, 1800, 1900, 2100,  # Century years not divisible by 400
    ])
    def test_non_leap_years(self, date_utils, year):
        """Verify common non-leap years return False."""
        assert not date_utils.is_leap_year(year)

    def test_year_zero_leap(self, date_utils):
        """Year 0 is leap year (divisible by 400) in proleptic Gregorian calendar."""
        assert date_utils.is_leap_year(0) is True

    # @pytest.mark.parametrize("div4_not100,century_div400,expected", [
    #     (True, True, True),    # 2000: div4+div400 → leap
    #     (True, False, True),   # 2024: div4+not100 → leap
    #     (False, True, True),   # Shouldn't happen, but tests logic flow
    #     (False, False, False), # 2023: neither → not leap
    # ])
    # def test_internal_logic_flow(self, date_utils, div4_not100, century_div400, expected):
    #     """Verify the nested conditional logic paths work correctly."""
    #     # This tests the actual decision paths in your code
    #     year = 2024 if div4_not100 else 2023
    #     if century_div400:
    #         year = 2000 if div4_not100 else 1900
    #     assert date_utils.is_leap_year(year) == expected

    def test_private_method_not_accessible(self, date_utils):
        """Verify private method cannot be accessed directly."""
        with pytest.raises(AttributeError):
            date_utils.__check_divisible_100_400(2024)
