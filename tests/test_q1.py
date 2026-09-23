"""HW2 Question 1 Tests"""
import sys

sys.path.append('.')

from src.q1 import combine_optional_strings

# Put your tests here
def test_q1() -> None:
    """test if function concatenates or not and if not prints None"""
    assert combine_optional_strings("Baker", "cookies") == "Bakercookies"

    assert combine_optional_strings("Hello ", "Max") == "HelloMax"

    assert combine_optional_strings("Hello") == "hello"

    assert combine_optional_strings(None, "Max") == "Max"

    assert combine_optional_strings() is None
 
