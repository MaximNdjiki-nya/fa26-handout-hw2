"""HW2 Question 3

Please implement the function below to match the documentation."""

from typing import Optional

def get_max_num(prompt: str, end_indicator: str) -> Optional[float]:
    """
    Repeatedly prompt the user to enter numbers until they enter the end indicator.
    Keep track of the maximum number entered. Reject anything that isn't a valid
    number (catch the ValueError). Return the maximum number entered as a float, 
    or None if no valid numbers were entered.

    Parameters:
        prompt : str
            The prompt to be printed to ask the user to enter a number.
            Example: "Please enter a number: "
        end_indicator : str
            The string that indicates the user has finished entering numbers.
            Examples: "done" or "" (empty string)

    Returns:
        Optional[float]: The maximum number entered by the user, or None if no 
                valid numbers were entered.
    """
    pass
