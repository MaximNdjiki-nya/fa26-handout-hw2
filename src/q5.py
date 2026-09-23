"""HW2 Question 5

Please implement the function below to match the documentation.
Make sure to reduce duplication of code as much as possible.
You may import code from other files using the syntax used for importing 
in the test files."""

def filter_lines_containing(input_filepath: str, output_filepath: str, keyword: str) -> None:
    """
    Read the file at input_filepath and output only the lines that contain the keyword
    (case-insensitive). Output the lines in their original order, maintaining punctuation, 
    capitalization, and the original line breaks, to a file at output_filepath. Ignore lines 
    that do not contain the keyword. If there is already a file at that location, overwrite it.

    Parameters:
        input_filepath : str
            The path to the input file to be read
        output_filepath : str
            The path to the output file to be written
        keyword : str
            The keyword to search for within the file lines
    """
    matching_lines = get_lines_containing(input_filepath, keyword)

    with open(output_filepath, "w", encoding="utf-8") as file:
        file.write(matching_lines)
