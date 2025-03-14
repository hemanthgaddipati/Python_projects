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
    password = input('Enter a password: ')
    strength = check_strength(password)

    if strength == 5:
        print('Password strength: Very Strong.')
    elif strength == 4:
        print('Password strength: Strong.')
    elif strength == 3:
        print('Password strength: Medium.')
    elif strength == 2:
        print('Password strength: Week.')
    else:
        print('Password strength: Very Week.')


if __name__ == '__main__':
    main()
