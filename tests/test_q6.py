"""HW2 Question 6 Tests"""

from unittest.mock import mock_open, patch
import sys

sys.path.append('.')
from src.q6 import play_madlibs

def test_play_madlibs() -> None:
    """Test that play_madlibs correctly prompts for placeholders and writes the output."""
    test_input_filepath = "test_file.txt"
    test_output_filepath = "output_file.txt"
    test_content = "I have a {adjective} dog."
    mocked_open = mock_open(read_data=test_content)

    with patch("builtins.open", mocked_open):
        with patch("builtins.input", return_value="fluffy"):
            play_madlibs(test_input_filepath, test_output_filepath)

    mocked_open.assert_any_call(test_input_filepath, "r", encoding="utf-8")
    mocked_open.assert_any_call(test_output_filepath, "w", encoding="utf-8")

    mocked_open().write.assert_any_call("I have a fluffy dog.")
