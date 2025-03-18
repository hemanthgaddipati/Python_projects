'''
SIMPLE TEXT EDITOR:
    Write a program to create a simple text editor. This program allows users to open
    an existing text file or create a new one, edit the content, and then save the
    changes by typing the SAVE command.
    
    Optional Enhancements
        • Allow users to choose whether they want to overwrite the existing file content
        or append new text to the end of the file.
        • Add functionality to search for specific words or phrases in the text and
        replace them with new content.
'''

import os

def read_file(filename):
    """
    Reads the content of a specified file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file as a string.

    Raises:
        OSError: If the file cannot be opened or read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filename, content):
    """
    Writes content to a specified file.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write into the file.

    Raises:
        OSError: If the file cannot be opened or written to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def get_user_input():
    """
    Prompts the user to enter text line by line until the SAVE command is entered.

    Returns:
        str: The concatenated text entered by the user.
    """
    print('\nEnter your text (type SAVE on a new line to save and exit.)')
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    return '\n'.join(lines)


def main():
    """
    The main function to run the Simple Text Editor program.

    Features:
        - Prompts the user to open an existing file or create a new one.
        - Displays the content of the file if it exists.
        - Allows the user to edit the content and save changes by typing the SAVE command.

    Handles:
        - File creation and reading.
        - Writing user input to the file.
        - Exceptions for file-related errors.

    Returns:
        None
    """
    filename = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(filename):
            print(read_file(filename))
        else:
            write_file(filename, '')

        content = get_user_input()
        write_file(filename, content)
        print(f'{filename} saved.')
    except OSError:
        print(f'{filename} could not be opened.')

if __name__ == '__main__':
    main()
