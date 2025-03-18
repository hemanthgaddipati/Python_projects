'''
    Write a program to evaluate the strength of a password based on criteria like
    length, the inclusion of uppercase letters, numbers, and special characters. The program 
    will then categorize the password as Very Weak, Weak, Medium, Strong, or Very Strong.
    
    Optional Enhancements
        • After evaluating the password, give the user suggestions on how to make it
        stronger, such as adding more characters, including special symbols, or
        avoiding common words.

'''

from re import search

def check_strength(password):
    """
    Evaluates the strength of a given password based on specific criteria.

    Criteria:
        - Length of at least 8 characters.
        - Inclusion of lowercase letters.
        - Inclusion of uppercase letters.
        - Inclusion of numbers.
        - Inclusion of special characters (@, #, $, %, +, =, !).

    Args:
        password (str): The password to evaluate.

    Returns:
        int: A strength score ranging from 0 to 5, where:
             - 0: Very Weak
             - 1: Weak
             - 2: Weak
             - 3: Medium
             - 4: Strong
             - 5: Very Strong
    """
    strength = 0

    if len(password) >= 8:
        strength += 1
    if search('[a-z]', password):
        strength += 1
    if search('[A-Z]', password):
        strength += 1
    if search('[0-9]', password):
        strength += 1
    if search('[@#$%+=!]', password):
        strength += 1

    return strength

def main():
    """
    The main function to run the Password Strength Checker program. It prompts the user 
    to enter a password, evaluates its strength using the `check_strength` function, and 
    categorizes the password as Very Weak, Weak, Medium, Strong, or Very Strong.

    Handles:
        - Input from the user.
        - Displays the password strength category based on the score.
    """
    password = input('Enter a password: ')
    strength = check_strength(password)

    if strength == 5:
        print('Password strength: Very Strong.')
    elif strength == 4:
        print('Password strength: Strong.')
    elif strength == 3:
        print('Password strength: Medium.')
    elif strength == 2:
        print('Password strength: Weak.')
    else:
        print('Password strength: Very Weak.')


if __name__ == '__main__':
    main()
