"""HW2 Question 1

Please implement the function below to match the documentation.

This is the only question in this assignment where you are required to write tests.
Tests for all other questions are provided for you this time."""

from typing import Optional

def combine_optional_strings(str_a: Optional[str], str_b: Optional[str]) -> Optional[str]:
    """
    Concatenates two strings with a space in between if both are present.
    If only one string is present, return that one by itself. If both are None,
    return None.
    """
    result: Optional[str]
    if str_a is not None and str_b is not None:
        result = str_a + " " + str_b
    elif str_a is not None:
        result = str_a
    elif str_b is not  None:
        result = str_b
    else:
        result = None
    return result
