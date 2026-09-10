"""HW2 Question 4 Tests"""

from unittest.mock import mock_open, patch, MagicMock, call
import sys

sys.path.append('.')
from src.q4 import filter_lines_containing

@patch("builtins.print")
def test_filter_lines_containing(mock_print: MagicMock) -> None:
    """Test that only lines containing the keyword are printed."""
    test_filepath = "test_file.txt"
    test_keyword = "keyword"
    test_content = """This is a line with the keyword.
This line does not have it.
Another keyword line."""
    mocked_open = mock_open(read_data=test_content)

    with patch("builtins.open", mocked_open):
        filter_lines_containing(test_filepath, test_keyword)

    mocked_open.assert_called_once_with(test_filepath, "r", encoding="utf-8")

    mock_print.assert_any_call("This is a line with the keyword.")
    mock_print.assert_any_call("Another keyword line.")
    assert call("This line does not have it.") not in mock_print.call_args_list
