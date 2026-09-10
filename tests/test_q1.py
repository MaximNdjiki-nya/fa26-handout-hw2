"""HW1 Question 1 Tests"""

ORIGINAL_CONTENT = '''"""HW1 Question 1

Tell us about your interest in computing!

This question is intentionally open-ended. To get full points on this question, 
modify the function below to print a sentence or two about your interests,
goals, or anything that brings you to this course.

You may rename the function, add comments, or make any other modifications.
The file must still work as a valid Python file after your modifications.

Getting your setup ready is the hardest part of the semester.
This question is designed to give you points for getting your GitHub and 
Pawtograder setup working, and making a successful submission."""

def print_meow() -> None:
    """Prints 'meow' to the console."""
    print("meow")
'''


def test_q1_contents() -> None:
    """Test that the contents of q1.py have been modified from the original content."""
    with open("src/q1.py", encoding="utf-8") as f:
        contents = f.read()
    assert contents != ORIGINAL_CONTENT
