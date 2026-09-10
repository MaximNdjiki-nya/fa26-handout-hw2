"""HW2 Question 5 Tests"""

from unittest.mock import mock_open, patch, call
import sys

sys.path.append('.')
from src.q5 import filter_lines_containing

def test_filter_lines_containing() -> None:
    """Test that only lines containing the keyword are written to the output file."""
    test_input_filepath = "test_file.txt"
    test_output_filepath = "output_file.txt"
    test_keyword = "keyword"
    test_content = """This is a line with the keyword.
This line does not have it.
Another keyword line."""
    mocked_open = mock_open(read_data=test_content)

    with patch("builtins.open", mocked_open):
        filter_lines_containing(test_input_filepath, test_output_filepath, test_keyword)

    mocked_open.assert_any_call(test_input_filepath, "r", encoding="utf-8")
    mocked_open.assert_any_call(test_output_filepath, "w", encoding="utf-8")

    mocked_open().write.assert_any_call("This is a line with the keyword.\n")
    mocked_open().write.assert_any_call("Another keyword line.\n")
    assert call("This line does not have it.\n") not in mocked_open().write.call_args_list
