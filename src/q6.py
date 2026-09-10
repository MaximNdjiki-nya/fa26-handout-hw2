"""HW2 Question 6

Please implement the function below to match the documentation.

Then, write a story template with placeholders in story_with_placeholders.txt, 
and run this file to play the game!

This question is based on the game Mad Libs (https://en.wikipedia.org/wiki/Mad_Libs).
"""

def play_madlibs(template_filepath: str, output_filepath: str) -> None:
    """
    Read a Mad Libs template from `template_filepath`, prompt the user for words to 
    fill in the placeholders, and write the completed story to `output_filepath`.

    The template file should contain placeholders in the format {placeholder_name}.
    The user will be prompted to provide a word for each placeholder in this format:
        "Please provide a placeholder_name: "
    where `placeholder_name` is the text inside the curly braces.
    
    The user's response will be used to replace the corresponding placeholder in the template.
    For example, if the template file contains the line:
        "I have a {adjective} dog."
    then the program will prompt:
        "Please provide a adjective: "
    and if the user types "fluffy", then the resulting line written to the output file will be:
        "I have a fluffy dog."

    Whitespace, punctuation, and capitalization will be preserved for all non-placeholder text.
    """
    pass

if __name__ == "__main__":
    play_madlibs("story_with_placeholders.txt", "output_story.txt")
