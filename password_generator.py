'''
PASSWORD GENERATOR:
    Write a program to generate a random password based on user-specified criteria, such as 
    length, and whether to include uppercase letters, numbers, and special characters.
    
    Optional Enhancements
        • Modify the program so the user can specify how many passwords they want to generate 
          at one time. The program should then create and display all the passwords.
        • Add an option to save the generated passwords to a text file. This allows
          users to keep a record of their passwords for future reference.
'''
import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special):
    """
    Generates a random password based on the specified criteria.

    Args:
        length (int): The length of the password to be generated.
        include_uppercase (bool): Whether to include uppercase letters in the password.
        include_numbers (bool): Whether to include numbers in the password.
        include_special (bool): Whether to include special characters in the password.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the password length is too short for the specified criteria.
    """

    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError('Password length is too short for the specified criteria')

    password = ''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    for _ in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    """
    The main function to run the Password Generator program. It prompts the user for 
    password criteria (length, inclusion of uppercase letters, numbers, and special characters), 
    generates a password based on the input, and displays it.

    Handles:
        - Input validation for password length and criteria.
        - Exceptions for invalid input.
    """

    length = int(input('Enter Password length: '))
    include_uppercase = input('Include Uppercase letters? (y/n): ').lower() == 'y'
    include_numbers = input('Include Numbers? (y/n): ').lower() == 'y'
    include_special = input('Include Special characters? (y/n): ').lower() == 'y'

    try:
        password = generate_password(length, include_uppercase, include_numbers, include_special)
        print(f'Generated password: {password}')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
