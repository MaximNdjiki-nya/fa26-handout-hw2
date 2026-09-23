"""HW2 Question 4

Please implement the function below to match the documentation."""

def get_lines_containing(filepath: str, keyword: str) -> str:
    """
    Read the file at filepath and return only the lines that contain the keyword
    (case-insensitive), in their original order, maintaining punctuation, capitalization, 
    and the original line breaks. The function returns the text as one large string, with 
    lines separated by the newline characters maintained from the original text. Ignore 
    lines that do not contain the keyword.

    For example, if the file contains the following lines:
        Hello World
        This is a test
        Another line with Test
    and the keyword is "test", the function would return this as a single string:
        This is a test
        Another line with Test

    Parameters:
        filepath : str
            The path to the file to be read
        keyword : str
            The keyword to search for within the file lines
    Returns:
        str
            The lines from the file that contain the keyword, in their original order.
    """
    result = ""

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            if keyword.lower() in line.lower():
                result += line

    return result
