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

# ask user for a file name
# if file exists
#   open it
#   Write its contents to the terminal
# else
#   create new file
# if file cannot be opened
#   Print Error
# Loop
#   Get user input
#   if input == 'SAVE'
#       break
# Write all the user input into the file

import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def get_user_input():
    print('\nEnter your text (type SAVE on a new line to save and exit.)')
    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    return '\n'.join(lines)


def main():
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