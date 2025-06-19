"""
File I/O operations for text processing.

Provides utility functions for reading text files with proper error handling.

"""

def text_to_string(filepath: str) -> str | None:
    """Reads a text file and returns it's content as a string. 
    
    Args:
        filepath (str): Path to the text file (relative or absolute).
    
    Returns:
        str: Content of the file as a single string.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file is not in UTF-8 encoding.
    
    Example:
        >>> text = text_to_string("data/example.txt")
    """

    try:
        with open(filepath, encoding="utf-8") as infile:
            return infile.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except UnicodeDecodeError:
        print(f"Error: File '{filepath}' is not UTF-8 encoded.")
        return None
    except Exception as e:
        print(f"Unexpected error while reading '{filepath}': {e}")
        return None