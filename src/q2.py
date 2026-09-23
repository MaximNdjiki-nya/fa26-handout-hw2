"""HW2 Question 2

Please implement the function below to match the documentation."""

def get_positive_number(prompt: str) -> float:
    """
    Repeatedly prompt the user to enter a number until they enter one that 
    is greater than 0. Reject anything that isn't a valid number (catch the 
    ValueError) and anything <= 0. Return the number as a float.

    Parameters:
        prompt : str
            The prompt to be printed to ask the user to enter a positive number.
            Example: "Please enter a positive number: "

    Returns:
        float: A positive number entered by the user.
    """
    response = 0.0
    while response <= 0:
        try:
            response = float(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            response = 0.0
    return response

num = get_positive_number("Enter dat Numba: ")

print(num)