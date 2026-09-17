"""HW2 Question 3 Tests"""

from unittest.mock import patch, MagicMock
import sys

sys.path.append('.')
from src.q3 import get_max_num


@patch('builtins.input', side_effect=['1', '2', '3', ''])
def test_get_max_all_positive(_: MagicMock) -> None:
    """Test that get_max_num returns the maximum number when all inputs are valid and positive."""
    assert get_max_num("Please enter a number: ", "") == 3

@patch('builtins.input', side_effect=['-1', '-2', '-3', ''])
def test_get_max_num_all_negative(_: MagicMock) -> None:
    """Test that get_max_num correctly identifies the maximum among negative numbers."""
    assert get_max_num("Please enter a number: ", "") == -1

@patch('builtins.input', side_effect=['-1', '2', '-3', ''])
def test_get_max_num_mixed_numbers(_: MagicMock) -> None:
    """Test that get_max_num correctly identifies the maximum among mixed positive and 
    negative numbers."""
    assert get_max_num("Please enter a number: ", "") == 2

@patch('builtins.input', side_effect=['', ''])
def test_get_max_num_no_input(_: MagicMock) -> None:
    """Test that get_max_num returns None if no valid numbers were entered."""
    assert get_max_num("Please enter a number: ", "") is None

@patch('builtins.input', side_effect=['a', 'b', '3', ''])
def test_get_max_num_invalid_then_valid(_: MagicMock) -> None:
    """Test that get_max_num ignores invalid inputs before a valid number."""
    assert get_max_num("Please enter a number: ", "") == 3

@patch('builtins.input', side_effect=['1', '2', 'c', ''])
def test_get_max_num_valid_then_invalid(_: MagicMock) -> None:
    """Test that get_max_num ignores invalid inputs after valid numbers."""
    assert get_max_num("Please enter a number: ", "") == 2

@patch('builtins.input', side_effect=['a', 'b', 'c', ''])
def test_get_max_num_all_invalid(_: MagicMock) -> None:
    """Test that get_max_num returns None if all inputs are invalid."""
    assert get_max_num("Please enter a number: ", "") is None

@patch('builtins.input', side_effect=['-1', 'hello', '5', ''])
@patch('builtins.print')
def test_prompt_is_printed(mock_print: MagicMock, mock_input: MagicMock) -> None:
    """Test that the prompt string is sent to either input or print."""
    prompt = "Please enter a positive number: "
    get_max_num(prompt, "")

    sent_to_input = any(call.args and call.args[0] == prompt for call in mock_input.call_args_list)
    sent_to_print = any(call.args and call.args[0] == prompt for call in mock_print.call_args_list)

    assert sent_to_input or sent_to_print
