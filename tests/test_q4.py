"""HW2 Question 4 Tests"""

from unittest.mock import mock_open, patch
import sys

sys.path.append('.')
from src.q4 import get_lines_containing

def test_get_lines_containing() -> None:
    """Test that only lines containing the keyword are returned."""
    test_filepath = "test_file.txt"
    test_keyword = "keyword"
    test_content = """This is a line with the keyword.
This line does not have it.
Another keyword line."""
    mocked_open = mock_open(read_data=test_content)

    with patch("builtins.open", mocked_open):
        result = get_lines_containing(test_filepath, test_keyword)

    mocked_open.assert_called_once_with(test_filepath, "r", encoding="utf-8")

    assert "This is a line with the keyword.\nAnother keyword line." == result
