"""HW2 Question 5 Tests"""

from unittest.mock import mock_open, patch
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

    # Accept either multiple write() calls (one per line) or a single combined write().
    written_text = "".join(call_args.args[0] for call_args in mocked_open().write.call_args_list)
    assert "This is a line with the keyword.\nAnother keyword line." in written_text
    assert "This line does not have it." not in written_text

def test_function_calls_get_lines_containing() -> None:
    """Test that filter_lines_containing calls get_lines_containing with the correct arguments."""
    test_input_filepath = "test_file.txt"
    test_output_filepath = "output_file.txt"
    test_keyword = "keyword"
    test_content = "This is a line with the keyword.\nAnother keyword line.\n"

    mocked_open = mock_open(read_data=test_content)
    with patch("builtins.open", mocked_open):
        with patch("src.q5.get_lines_containing", return_value=test_content) as mocked_get_lines:
            filter_lines_containing(test_input_filepath, test_output_filepath, test_keyword)

    mocked_get_lines.assert_called_once_with(test_input_filepath, test_keyword)
