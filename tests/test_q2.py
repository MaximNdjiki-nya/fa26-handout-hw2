"""HW2 Question 2 Tests"""

from unittest.mock import MagicMock, patch
import sys

sys.path.append('.')
from src.q2 import get_positive_number

@patch('builtins.input', return_value='5')
def test_get_positive_number_first_try(_: MagicMock) -> None:
    """Test that get_positive_number returns the correct value on the first try."""
    assert get_positive_number() == 5.0

@patch('builtins.input', side_effect=['-1', '0', '5'])
def test_get_positive_number_third_try(_: MagicMock) -> None:
    """Test that get_positive_number returns the correct value after two negative tries."""
    assert get_positive_number() == 5.0

@patch('builtins.input', side_effect=['hello', '5'])
def test_get_positive_number_non_numerical_then_valid(_: MagicMock) -> None:
    """Test that get_positive_number returns the correct value after a non-numerical input."""
    assert get_positive_number() == 5.0
