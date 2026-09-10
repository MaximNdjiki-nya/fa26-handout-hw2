"""HW1 Question 3

Your task for this question is to write tests for the provided function.
Please write tests in the file tests/test_q3.py.
Your tests are graded based on the number of cases covered."""


def capitalize_words(s: str) -> str:
    """Capitalizes the first letter of each word in a string.

    A word is defined as a sequence of characters separated by spaces.
    If a word starts with a non-letter character, the first letter after 
    that character is capitalized instead, and the non-letter character at
    the start of the word is left unchanged.

    Parameters
    ----------
    s : str
        The input string.

    Returns
    -------
    str
        A new string where the first letter of each word is uppercased
        and all other letters are unchanged.
    """
    result = ""
    index = 0
    capitalize_next = True
    while index < len(s):
        character = s[index]
        if character == " ":
            result += character
            capitalize_next = True
        elif capitalize_next and character.isalpha():
            result += character.upper()
            capitalize_next = False
        else:
            result += character
            if character.isalpha():
                capitalize_next = False
        index += 1
    return result
